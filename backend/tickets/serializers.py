from rest_framework import serializers
from .models import *
from django.db import models

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'pk',
            'user',
            'description',
            'status',
            'submited_date',
            'closed_date',
            'last_updated',
            'user_name',
            'attachements',
            'messages'
        ]


class MessageSerializer(serializers.ModelSerializer):
    attachements = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="id_file_pair"
    )
    class Meta:
        model = Message
        fields = [
            'pk',
            'message_from',
            'attachements',
            'content',
            'sent_date',
        ]

class AttachementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachement
        fields = [
            'file',
            'upload_date'
        ]
 

        