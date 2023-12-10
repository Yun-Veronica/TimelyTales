"""
URL configuration for timelytales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from posts import views as posts_views
from user import views as user_views
from  rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from django.conf import settings
from django.conf.urls.static import static

router= routers.DefaultRouter()
router.register(r'posts', posts_views.PostViewSet)
router.register(r'user', user_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', user_views.register_user, name='register'),
    path('login', user_views.login_view, name='login'),
    path('logout', user_views.logout_view, name='logout'),
    path('posts', posts_views.create_post, name='create_post'),
    path('user/<int:pk>/profile', user_views.user_profile, name='show profile'),
    # path('user/<int:pk>/subscriptions', user_views.subscriptions, name='show subscribed authors'),
    # path('posts/user/<int:pk>/', user_views.user_all_posts, name='show all posts of user'),

    # path('posts/<int:pk>/', posts_views.post, name='modify/delete/get specific post'),

    path('main/', posts_views.index, name='main_page'),

    path('drf-auth/', include("rest_framework.urls")),

    path('', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('posts/', include("posts.urls")),
#     path('user/', include("user.urls")),
# ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)