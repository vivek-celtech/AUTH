from django.urls import path
from .views import AddContentView
from .views import CourseListAPI

urlpatterns = [
    
    path('AddContent/', AddContentView.as_view(), name='add-content'),
    path('get_courses/', CourseListAPI.as_view(), name='get_course'),
    
]


