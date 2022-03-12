from dictionary.models import Source, Word
from dictionary.serializers import SourceSerializer, WordSerializer
from rest_framework import viewsets


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
