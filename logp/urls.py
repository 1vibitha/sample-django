from django.urls import path
from .import views

urlpatterns = [
    path('signin', views.signin,name="signin"),
    path('reg', views.register,name="register"),
    path('', views.login,name="log"),
    path('logout', views.logout,name="logout"),
    path('viewall', views.viewall,name="viewall"),
    path('updatereg/<str:pk>/', views.updatereg,name="updatereg"),

    
]