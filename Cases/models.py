from django.db import models

# Create your models here.
class Case(models.Model):
    pdf=models.FileField(upload_to='cases/pdfs/')
    


    def __str__(self):
        return self.pdf