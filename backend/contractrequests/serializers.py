from rest_framework import serializers
from .models import *
from django.db import models

class ContractRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractRequest
        fields = [
            'pk',
            'first_name',       
            'last_name',
            'email',
            'address',
            'city',
            'state',
            'zipcode',
            'ownership_type',
            'approved',
            'submited_date',
            'approved_date',
            'last_updated',
            'messages',
            'contracts'
        ]
    def get_contract_status(self,obj):
        if(obj.approved):
            return "approved"
        if(Message.objects.filter(contract__PK = obj.pk)):
            if(Message.objects.filter(contract__PK = obj.pk).last().is_admin_message == True):
                return "Waiting For Customer Response"
            if(Message.objects.filter(contract__PK = obj.pk).last().is_admin_message != True):
                return "Waiting For Admin Response"
        else:
            return "Request is processing"


class MessageSerializer(serializers.ModelSerializer):
    attachement = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="id_file_pair"
    )
    class Meta:
        model = Message
        fields = [
            'pk',
            'message_from',
            'attachement',
            'content',
            'sent_date',
        ]

class AttachementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'file',
            'upload_date'
        ]
 

        