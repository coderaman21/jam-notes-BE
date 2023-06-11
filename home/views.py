from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user_id = '1').order_by('-updated_at')

    def create(self, request, *args, **kwargs):
        request.data['user'] = '1'
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data['user'] = '1'
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'success':'deleted'},status=status.HTTP_200_OK)