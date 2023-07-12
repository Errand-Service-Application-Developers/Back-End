from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from .models import ListItem,ItemCategory,ItemReview



class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','username','email','phone','post_count']

    post_count = serializers.IntegerField(read_only = True)
    



class UserCreateSerializer(BaseUserCreateSerializer):
  
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','email','phone','password']
        

class ItemCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ItemCategory
        fields = ['id', 'name', 'icon', 'backgroundColor', 'color']



class ListItemReviewSerializer(serializers.ModelSerializer):
    
    date_created = serializers.DateTimeField(read_only = True)
    user = UserSerializer(read_only = True)
    item_id = serializers.IntegerField(read_only = True)
    class Meta:
        model = ItemReview
        fields = ['id', 'message', 'item_id','user', 'date_created']


class PostReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    item_id = serializers.IntegerField()
   
    class Meta:
        model = ItemReview
        fields = ['message','item_id','user_id']


class ListItemSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only = True)
    reviews = ListItemReviewSerializer(many=True, read_only=True)

    
    class Meta: 
        model = ListItem
        fields = ['id', 'title', 'description','price', 'category', 'user_id', 'date_created','reviews']
    


