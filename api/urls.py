from django.urls import include, path
from rest_framework import routers
from api.views import ResearchPaperViewSet

router = routers.DefaultRouter()
router.register(r'papers', ResearchPaperViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]
