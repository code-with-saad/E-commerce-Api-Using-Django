from django.shortcuts import render
from rest_framework.decorators import api_view
from cartitems.models import CartItem
from cartitems.serializers import CartItemSerializer
from rest_framework.response import Response

@api_view({'Get'})
def cartview(request):
    queryset = CartItem.objects.all()
    serializer = CartItemSerializer(queryset, many= True)
    return Response({'status': 200, 'payload': serializer.data})