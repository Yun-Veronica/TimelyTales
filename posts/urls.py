from django.urls import path, include


# from . import views
#
#
#
# urlpatterns = [
#     # path("", views.index, name="index"),
#     # path("api/v1/postslist", views.PostAPIView.as_view(), name="api"),
#     # path("api/v1/postslist", views.PostList.as_view(), name="api"),
#     # path("api/v1/postslist/<int:pk>/", views.PostAPIView.as_view(), name="api")
#     # path("api/v1/postslist/<int:pk>/", views.PostDetailView.as_view(), name="api")
#
#     path("api/v1/postslist", views.PostViewSet.as_view({"get":"list"})),
#     path("api/v1/postslist/<int:pk>/", views.PostViewSet.as_view({"put":"update"}))
#
# ]