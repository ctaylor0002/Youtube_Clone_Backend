from rest_framework import status
from rest_framework.response import Response
from .models import Reply
from .serializers import ReplySerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def reply_list(request, pk):

    if request.method == 'POST':

        serializer = ReplySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user, comment_id = pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif(request.method == 'GET'):
        replies = Reply.objects.filter(comment_id=pk)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

