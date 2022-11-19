from rest_framework import serializers
from .models import Reply

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['text', 'user_id', 'comment_id']
        depth = 1