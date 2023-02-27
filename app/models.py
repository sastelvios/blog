from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    cover = models.ImageField(upload_to='posts')
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



