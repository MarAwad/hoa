from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import TicketSerializer, MessageSerializer, AttachementSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
ticket_list_create_view = TicketListCreateView.as_view()

class TicketDetailView(generics.RetrieveAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
ticket_detail_view = TicketDetailView.as_view()

class MessagesListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        ticketId = self.kwargs['pk']
        return Ticket.objects.filter(pk=ticketId).first().messages
    def perform_create(self, serializer):
        ticketID = self.kwargs['pk']
        ticket = Ticket.objects.filter(pk=ticketID).first()
        serializer.save(Ticket=ticket)
messages_list_create_view = MessagesListCreateView.as_view()

class MessageDetailView(generics.RetrieveAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        ticketID = self.kwargs['ticket']
        return Ticket.objects.filter(pk=ticketID).first().messages
message_detail_view = MessageDetailView.as_view()

class AttachementListCreateView(generics.ListCreateAPIView):
    serializer_class = AttachementSerializer
    def get_queryset(self):
        ticketId = self.kwargs['ticket']
        messageId = self.kwargs['message']
        return Ticket.objects.filter(pk=ticketId).first().messages.filter(pk=messageId).first().attachements
    def perform_create(self, serializer):
        ticketId = self.kwargs['ticket']
        messageId = self.kwargs['message']
        message =  Ticket.objects.filter(pk=ticketId).first().messages.filter(pk=messageId).first()
        serializer.save(message=message)
attachement_list_create_view = AttachementListCreateView.as_view()

class ContractAttachementListCreateView(generics.ListCreateAPIView):
    serializer_class = AttachementSerializer
    def get_queryset(self):
        ticketId = self.kwargs['ticket']
        return Ticket.objects.filter(pk=ticketId).first().attachements
    def perform_create(self, serializer):
        ticketId = self.kwargs['ticket']
        ticket =  Ticket.objects.filter(pk=ticketId).first()
        serializer.save(ticket=ticket)
contract_attachement_list_view = ContractAttachementListCreateView.as_view()
    