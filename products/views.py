from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from products.serializers import ProductSerializer
from products.models import Product

class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available products from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific product by passing in the id of the product to update"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific product from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
