from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, ItemCategorySerializer, ListItemSerializer, ListItemReviewSerializer, PostReviewSerializer,ReviewReplySerializer,PostReplySerializer
from .models import User, ItemCategory, ListItem,ItemReview,ReviewReply


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.annotate(post_count =Count('items')).all()

    @action(detail=False, methods=['GET'])
    def me(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    @action(detail=True,methods=['GET'])
    def reviews(self,request,pk):
        queryset = ItemReview.objects.filter(user_id = pk).order_by('-date_created')
        serializer = ListItemReviewSerializer(queryset,many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET'])
    def history(self,request,pk):
        queryset =  ListItem.objects.filter(user_id = pk).prefetch_related('reviews').order_by('-date_created')
        serializer = ListItemSerializer(queryset,many=True)
        return Response(serializer.data)
        


class ItemCategoryViewSet(ModelViewSet):
    serializer_class = ItemCategorySerializer
    queryset = ItemCategory.objects.all()


class ListItemViewSet(ModelViewSet):
    serializer_class = ListItemSerializer
    queryset = ListItem.objects.select_related('user').prefetch_related('reviews').order_by('-date_created').all()

        
class ListItemReviewViewSet(ModelViewSet):
    http_method_names = ['get','post','delete',]
    def get_queryset(self):
        return ItemReview.objects.prefetch_related('replies').filter(item_id = self.kwargs['item_pk']).order_by('-date_created')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostReviewSerializer
        return ListItemReviewSerializer

class ReviewReplyViewSet(ModelViewSet):
    http_method_names = ['get','post','delete',]
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostReplySerializer
        return ReviewReplySerializer
    
    def get_queryset(self):
        return ReviewReply.objects.select_related('user').filter(review_id = self.kwargs['review_pk']).order_by('-date_created')
    