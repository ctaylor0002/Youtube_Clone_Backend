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
    # type_param = request.query_params.get('video_id')
    
    # comments = Comment.objects.all()

    # if type_param:
    #     comments = comments.filter(video_id__video_id=type_param)

    # serializer = CommentSerializer(comments, many=True)

    comments = Comment.objects.filter(video_id=video_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)