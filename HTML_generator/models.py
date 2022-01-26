from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Content(models.Model):
    text = RichTextField(blank=True, null=True)