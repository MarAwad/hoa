from django.db import models
from datetime import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL
STATUS_TYPES = [
    (0,'Open'),
    (1,'Waiting for customer'),
    (2,'Closed')
]

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=4, choices=STATUS_TYPES, default=0)
    submited_date = models.DateTimeField(auto_now_add=True)
    closed_date = models.DateTimeField(default=None, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    @property
    def user_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Message(models.Model):
    message_from = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    Ticket = models.ForeignKey(Ticket,null=True, related_name="messages", on_delete=models.SET_NULL)
    @property
    def is_admin_message(self):
        return self.user.is_staff

class Attachement(models.Model):
    file = models.FileField(upload_to ='uploads/tickets/')
    upload_date =models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Ticket,null=True, related_name="attachements", on_delete=models.SET_NULL)
    message = models.ForeignKey(Message,null=True, related_name="attachements", on_delete=models.SET_NULL)
    
    @property
    def id_file_pair(self):
        return {
            'id':self.pk,
            'file':self.file.url
        }
    
