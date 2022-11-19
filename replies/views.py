from rest_framework import status
from rest_framework.response import Response
from .models import Reply
from .serializers import ReplySerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_reply(request, pk):
    if request.method == 'POST':
        #updated_request = {'text':(request.data['text']), 'comment_id': pk}

       

        serializer = ReplySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, comment_id = pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
