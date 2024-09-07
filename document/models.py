from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/')
    #uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='uploaded_documents')



# added after login, signup functionality for dashboard
   
def __str__(self):
    return self.file.name