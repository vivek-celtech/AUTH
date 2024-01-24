from django.urls import path
from .views import AddContentView
from .views import CourseListAPI

urlpatterns = [
    
    path('add_course/', AddContentView.as_view(), name='add-content'),
    path('get_course/', CourseListAPI.as_view(), name='get_course'),
    
]