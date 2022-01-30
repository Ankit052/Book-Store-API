from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django.db.models import Count

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'category__name']
    
    
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        if self.request.GET.get('sort'):
            queryset = queryset.order_by(self.request.GET.get('sort'))
        return queryset