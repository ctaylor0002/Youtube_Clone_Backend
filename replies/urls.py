from django.urls import path, include
from replies import views

urlpatterns = [
    path('<int:pk>/', views.post_reply),
   
]