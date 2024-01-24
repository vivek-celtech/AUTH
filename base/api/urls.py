from django.urls import path
from . import views
from .views import MyTokenObtainPairView , signup
from rest_framework_simplejwt.views import TokenRefreshView




""" 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

 """
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
#    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#    path('notes/', views.getRoutes),

    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', signup, name='signup'),
]
