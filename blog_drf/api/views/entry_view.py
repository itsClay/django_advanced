from rest_framework.generics import ListCreateAPIView
from blog_drf.api.serializers.entry_serializer import EntrySerializer


class EntryView(ListCreateAPIView):
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.all()