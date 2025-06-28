from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PurchaseHistoryViewSet, 
    CreateCheckoutSessionAPIView, 
    StripeWebhookAPIView
    )

router = DefaultRouter()
router.register(r'purchase-history', PurchaseHistoryViewSet, basename='purchasehistory')

urlpatterns = [
    path('', include(router.urls)),
    path('checkout/<int:product_id>/', CreateCheckoutSessionAPIView.as_view(), name='checkout'),
    path('stripe/webhook/', StripeWebhookAPIView.as_view(), name='stripe-webhook'),
]
