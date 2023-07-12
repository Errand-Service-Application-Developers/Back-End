from django.urls import path,include
from rest_framework_nested import routers
from .views import ListItemReviewViewSet, ItemCategoryViewSet, ListItemViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('tasks',ListItemViewSet)
router.register('categories', ItemCategoryViewSet)

task_router = routers.NestedDefaultRouter(router,'tasks',lookup = 'item')
task_router.register('reviews',ListItemReviewViewSet,basename='item-review')



urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(task_router.urls)),
]
