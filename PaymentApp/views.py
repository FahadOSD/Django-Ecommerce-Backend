from accounts.models import Product
from django.conf import settings
import stripe
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import PurchaseHistory
from .serializers import PurchaseHistorySerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

class PurchaseHistoryViewSet(viewsets.ModelViewSet):
    queryset = PurchaseHistory.objects.all()
    serializer_class = PurchaseHistorySerializer
    permission_classes = [IsAuthenticated]

class CreateCheckoutSessionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        YOUR_DOMAIN = f"{request.scheme}://{request.get_host()}"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price * 100,
                        'product_data': {
                            'name': product.name,
                            'images': [product.image] if product.image else [],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'product_id': product_id,
                'user_email': request.user.email,
            },
            mode='payment',
            success_url=YOUR_DOMAIN + f'/api/payment/success/{product_id}/',
            cancel_url=YOUR_DOMAIN + f'/api/payment/failed/{product_id}/',
        )
        return Response({'checkout_url': checkout_session.url})

@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except Exception:
            return Response(status=400)

        if event['type'] == 'checkout.session.async_payment_failed':
            session = event['data']['object']
            product_id = session['metadata']['product_id']
            get_product = Product.objects.get(id=product_id)
            PurchaseHistory.objects.create(product=get_product)

        elif event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            product_id = session['metadata']['product_id']
            get_product = Product.objects.get(id=product_id)
            PurchaseHistory.objects.create(product=get_product, purchase_success=True)

        return Response(status=200)
