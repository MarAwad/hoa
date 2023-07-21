from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import *
from .serializers import ContractRequestSerializer, MessageSerializer, AttachementSerializer

class RequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = ContractRequest.objects.all()
    serializer_class = ContractRequestSerializer
    
    #def perform_create(self, serializer):
        #serializer.save()
    
request_list_create_view = RequestListCreateAPIView.as_view()



class RequestDetailAPIView(
    generics.RetrieveAPIView):
    queryset = ContractRequest.objects.all()
    serializer_class = ContractRequestSerializer
    lookup_field = 'pk'

request_detail_view = RequestDetailAPIView.as_view()

class RequestDetailAPIView(
    generics.RetrieveAPIView):
    queryset = ContractRequest.objects.all()
    serializer_class = ContractRequestSerializer
    lookup_field = 'pk'

request_detail_view = RequestDetailAPIView.as_view()


class RequestUpdateAPIView(generics.UpdateAPIView):
    queryset = ContractRequest.objects.all()
    serializer_class = ContractRequestSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

request_update_view = RequestUpdateAPIView.as_view()


class RequestDestroyAPIView(generics.DestroyAPIView):
    queryset = ContractRequest.objects.all()
    serializer_class = ContractRequestSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

request_destroy_view = RequestDestroyAPIView.as_view()


class MessagesListCreateAPIView(
    generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        requestId = self.kwargs['pk']
        if (ContractRequest.objects.filter(pk=requestId).first().messages):
            return ContractRequest.objects.filter(pk=requestId).first().messages.order_by('-sent_date')
        else:
            return []
    
    def perform_create(self,serializer):
        requestId = self.kwargs['pk']
        request = ContractRequest.objects.filter(pk=requestId).first()
        serializer.save(contract=request)
messages_list_view = MessagesListCreateAPIView.as_view()

class MessageDetailAPIView(
    generics.RetrieveAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        requestId = self.kwargs['requestId']
        request = ContractRequest.objects.filter(pk=requestId).first()
        return Message.objects.all().filter(contract=request)

messages_detail_view = MessageDetailAPIView.as_view()

class AttachementListCreateAPIView(
    generics.ListCreateAPIView):
    serializer_class = AttachementSerializer
    def get_queryset(self):
        requestId = self.kwargs["requestId"]
        messageId = self.kwargs["pk"]
        return ContractRequest.objects.filter(pk=requestId).first().messages.filter(pk=messageId).first().attachement
    def perform_create(self,serializer):
        requestId = self.kwargs["requestId"]
        messageId = self.kwargs['pk']
        message = ContractRequest.objects.filter(pk=requestId).first().messages.filter(pk=messageId).first()
        serializer.save(message_id=message)
    
attachement_list_create_view = AttachementListCreateAPIView.as_view()
        

