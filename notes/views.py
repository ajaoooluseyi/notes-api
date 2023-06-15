from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)