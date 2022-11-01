from mongotr.models import Payment
from rest_framework import serializers


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'