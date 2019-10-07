from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

def pdf_upload_to(instance, filename):
    return 'pdf_list/{}'.format(filename)

class PDFDocument(models.Model):
    filename = models.CharField(max_length=126)
    pdf_file = models.FileField(upload_to=pdf_upload_to,
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
