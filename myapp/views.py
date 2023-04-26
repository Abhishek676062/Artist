from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from myapp.models import Work, Artist
from myapp.serializers import WorkSerializer, UserSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')


class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Work.objects.all()
        artist_name = self.request.query_params.get('artist', None)
        work_type = self.request.query_params.get('work_type', None)
        if artist_name is not None:
            queryset = queryset.filter(artist__name__icontains=artist_name)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)
        return queryset

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
