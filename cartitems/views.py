from rest_framework.decorators import api_view
from cartitems.models import CartItem
from cartitems.serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CartItem
from .serializers import CartSerializer

# @api_view(['Get'])
# def cartview(request):
#     queryset = CartItem.objects.all()
#     serializer = CartSerializer(queryset, many= True)
#     return Response({'status': 200, 'payload': serializer.data})

# def post(request, *args, **kwargs):
#     data = {
#         'productid': request('productid'),
#         'price': request('price'),
#         'quantity': request('quantity'),
#         }
#     serializer = CartSerializer(data=data)
#     if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     todos = CartItem.objects.filter(user=request.user.id)
    #     serializer = CartSerializer(todos, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

# 2. Create
def post(self, request, *args, **kwargs):
        data = {
            'productid': request.data.get('productid'),
            'price': request.data.get('price'),
            'quantity': request('quantity'),
        }
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)