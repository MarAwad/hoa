from django.db import models
from datetime import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

OWNERSHIP_TYPES = [
    (0,"Own"),
    (1,"Rent"),
    (2,"Temp")
    ]

class ContractRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null= True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    ownership_type = models.CharField(max_length=4, choices=OWNERSHIP_TYPES)
    approved = models.BooleanField(default=False)
    submited_date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(default=None, null=True)
    last_updated = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message_from = models.CharField(max_length=200)
    content = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    contract = models.ForeignKey(ContractRequest,null=True, related_name="messages", on_delete=models.SET_NULL)
    is_admin_message = models.BooleanField(default=False)
    

class Contract(models.Model):
    file = models.FileField(upload_to ='uploads/')
    upload_date =models.DateTimeField(auto_now_add=True)
    contract_request = models.ForeignKey(ContractRequest,null=True, related_name="contracts", on_delete=models.SET_NULL)
    message_id = models.ForeignKey(Message,null=True, related_name="attachement", on_delete=models.SET_NULL)
    
    @property
    def id_file_pair(self):
        return {
            'id':self.pk,
            'file':self.file.url
        }
      
