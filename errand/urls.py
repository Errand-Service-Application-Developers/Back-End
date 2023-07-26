from django.urls import path,include
from rest_framework_nested import routers
from .views import ListItemReviewViewSet, ItemCategoryViewSet, ListItemViewSet, UserViewSet,ReviewReplyViewSet,RequestViewSet


router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('tasks',ListItemViewSet)
router.register('categories', ItemCategoryViewSet)
router.register('requests',RequestViewSet)

task_router = routers.NestedDefaultRouter(router,'tasks',lookup = 'item')
task_router.register('reviews',ListItemReviewViewSet,basename='item-review')

review_router = routers.NestedDefaultRouter(task_router,'reviews',lookup = 'review')
review_router.register('replies',ReviewReplyViewSet,basename='review-reply')



urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(task_router.urls)),
    path(r'',include(review_router.urls))
]
