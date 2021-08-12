from rest_framework import serializers
from api.models import ResearchPaper

class ResearchPaperSerializer(serializers.ModelSerializer):
    """Serialize the models -- serializers will convert the ResearchPaper
       model into JSON to return, by the API, to the user."""
    class Meta:
        model = ResearchPaper
        fields = ('title', 'author', 'summary')
