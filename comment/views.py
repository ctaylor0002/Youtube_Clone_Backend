from rest_framework import status
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404

# New Imports
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def get_comments_for_video(request, video_id):
    
    if request.type == "GET":
        comments = Comment.objects.filter(video_id=video_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create a Protected Route
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment_for_video(request, video_id):
    print('User ', f"{request.user.id} {request.user.email} {request.user.username}")

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)