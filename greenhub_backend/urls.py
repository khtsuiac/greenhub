"""greenhub_backend URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include,path
from rest_framework import routers
from user_db import views as user_views
from restaurants_db import views as restaurant_views
from reward_db import views as reward_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'groups', user_views.GroupViewSet)
router.register(r'restaurant', restaurant_views.RestaurantViewSet,basename="restaurant")
router.register(r'reward',reward_views.RewardViewSet)

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('backend/',include(router.urls)),
    path('backend/api-auth/',include('rest_framework.urls', namespace='rest_framework'))
]