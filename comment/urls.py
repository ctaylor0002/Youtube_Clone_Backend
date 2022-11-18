from django.urls import path, include
from comment import views

urlpatterns = [
    path('<str:video_id>', views.get_comments_for_video),
]