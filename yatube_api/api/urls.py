from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments'
                   )

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path("v1/", include("djoser.urls.jwt"))
    # re_path(r"^jwt/create/?",
    #         views.TokenObtainPairView.as_view(),name="jwt-create"),
    # re_path(r"^jwt/refresh/?",
    #         views.TokenRefreshView.as_view(), name="jwt-refresh"),
    # re_path(r"^jwt/verify/?",
    #         views.TokenVerifyView.as_view(), name="jwt-verify"),
]
