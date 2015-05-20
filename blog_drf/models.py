from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Create your models here.
# related name is when you query and you want to find all related entries
#django gives you a shortcut to say give me all the entries for this user

class TagAPI(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class EntryAPI(models.Model):
    entry = models.ForeignKey(User, related_name='entries')
    body = models.TextField(),
    title = models.CharField(max_length=45, null=True)
    tags = models.ManyToManyField(TagAPI)

