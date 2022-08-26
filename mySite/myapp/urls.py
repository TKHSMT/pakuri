from django.urls import path, include
from .views import SampleAppList
 
 
urlpatterns = [
    path('list/', SampleAppList.as_view()),
]