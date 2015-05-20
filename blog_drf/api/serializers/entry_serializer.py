from rest_framework import serializers
from blog_drf.models import EntryAPI

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryAPI
