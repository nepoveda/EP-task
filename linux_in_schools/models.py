from django.db import models
from ckeditor.fields import RichTextField

def article_upload_to(instance, filename):
    return 'pdf_list/{}'.format(filename)

class Article(models.Model):
    header = models.CharField(max_length=128)
    text = RichTextField()
    publisth_date = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=256)
    list_picture = models.ImageField(upload_to=article_upload_to, blank=True, null=True)

    def __str__(self):
        return 'Article: {}'.format(self.header)
