from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="home"),
    path('abc', views.about,name="about"),
    path('cdf', views.show,name="show"),
    path('cdf', views.show,name="show"),
    path('demo', views.demo,name="demo"),
    path('dept', views.dept,name="dept"),
    path('doct', views.doct,name="doct"),
    path('book', views.booking,name="book"),
    
]