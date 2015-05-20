from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    type = models.CharField(max_length=40)

class Entry(models.Model):
    author = models.ForeignKey(User, related_name='entries')
    text = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "{}...".format(self.text[:20])

class Author(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")