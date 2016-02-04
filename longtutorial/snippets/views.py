from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

# This method is to go one step furthen from the mixin clases from before.
# REST framework provides a set of already mixed-in generic views
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer