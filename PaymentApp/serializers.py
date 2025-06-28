from rest_framework import serializers
from .models import PurchaseHistory

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = '__all__' 