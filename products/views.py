from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


class ProductAPIView(APIView):
    authentication_classes = TokenAuthentication
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})

    def post(self, request):
        product = request.data.get('product')
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response({"success": "Product successfully created"})
        else:
            return Response({"error": serializer.errors})
