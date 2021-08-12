from rest_framework import viewsets
from api.serializers import ResearchPaperSerializer
from api.models import ResearchPaper

class ResearchPaperViewSet(viewsets.ModelViewSet):
    """Create a View to the API."""
    queryset = ResearchPaper.objects.all()
    serializer_class = ResearchPaperSerializer
