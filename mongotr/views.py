from django.shortcuts import render
from django.http import HttpResponse
from mongotr.models import Payment
from mongotr.serializers import PaymentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def getEndpoints(request):
    """ lst = [{'hello':'hello'}] """
    return HttpResponse("HEllo world")


@api_view(['POST'])
def createPayment(request):
    data = request.data
    print(data)
    print(request.user)
    cashBacks = int(data['cashback'])
    pay = int(data['payment'])
    
    PayedAmount = pay-cashBacks
    print(PayedAmount)
    print(cashBacks)

    payment= Payment.objects.create(user=request.user,payment=pay,
    cashback=cashBacks,amountPayed=PayedAmount
    )
    serializers=PaymentSerializers(payment,many=False) 
    return Response("Data submitted successfully")

@api_view(['GET'])
def getPayments(request):
    payment= Payment.objects.all()
    serializers=PaymentSerializers(payment,many=True)
    return Response(serializers.data)
