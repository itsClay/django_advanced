from rest_framework import serializers
from blog_drf.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
