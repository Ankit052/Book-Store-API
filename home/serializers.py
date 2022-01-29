
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    # order = serializers.StringRelatedField(many= True,read_only = True )
    class Meta :
        model = User
        fields = ["id","user_name","age","city","phone_number","email","created_date"]
         

class CategorySerializer(serializers.ModelSerializer):
    # book_list = serializers.StringRelatedField(many=True, read_only =True)
    class Meta :
        model = Category
        fields =  ["id","name","created_date"]



class BookSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta :
        model = Book
        fields =  ["id","name","author_name","category","publish_date","price","created_date"]

    def to_representation(self, instance):
        data = super(BookSerializer, self).to_representation(instance)
        data["category"]=CategorySerializer(instance.category).data
        return data



class OrderSerializer(serializers.ModelSerializer):
    class Meta :
        model = Order
        fields =  ["ordered_by","book","ordered_date"]

    def to_representation(self, instance):
        data = super(OrderSerializer, self).to_representation(instance)
        data["ordered_by"]=UserSerializer(instance.ordered_by).data
        data["book"]=BookSerializer(instance.book.all(), many=True).data
        return data
