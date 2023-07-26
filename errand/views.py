from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, ItemCategorySerializer, ListItemSerializer, ListItemReviewSerializer, PostReviewSerializer,ReviewReplySerializer,PostReplySerializer,RequestSerializer,PostRequestSerializer
from .models import User, ItemCategory, ListItem,ItemReview,ReviewReply,Request


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
    
    
    @action(detail=True, methods = ['GET','DELETE'])
    def ownedrequests(self,request,pk):
        if request.method == 'GET':
            queryset = Request.objects.select_related('owner','task','requester').filter(owner_id = pk).order_by('-date_created')
            serializer = RequestSerializer(queryset,many = True)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            Request.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods = ['GET'])
    def sentrequests(self,request,pk):
        if request.method == 'GET':
            queryset = Request.objects.select_related('owner','task','requester').filter(requester_id = pk).order_by('-date_created')
            serializer = RequestSerializer(queryset,many = True)
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
        return ReviewReply.objects.prefetch_related('user').filter(review_id = self.kwargs['review_pk']).order_by('-date_created')


class RequestViewSet(ModelViewSet):
    http_method_names = ['get','post','delete','patch']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostRequestSerializer
        return RequestSerializer
    queryset = Request.objects.select_related('task','owner').all().order_by('-date_created')