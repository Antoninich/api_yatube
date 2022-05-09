from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'api/v1/posts', PostViewSet, basename='posts')
router.register(
    r'api/v1/posts/(?P<post_pk>[0-9]+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(r'api/v1/groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),

]
