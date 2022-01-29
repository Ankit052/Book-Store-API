from django.urls import path,include
from home import views
from .views import *
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'user',views.UserViewSet, basename='user')
router.register(r'category',views.CategoryViewSet, basename='category')
router.register(r'book',views.BookViewSet, basename='book')
router.register(r'order',views.OrderViewSet, basename='order')




urlpatterns = [

    path('', include(router.urls))

]
