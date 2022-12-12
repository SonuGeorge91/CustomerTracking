from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter

accounts_router = DefaultRouter()

accounts_router.register('', views.UserProfile, basename='user-profile')

urlpatterns = []
urlpatterns += accounts_router.urls
