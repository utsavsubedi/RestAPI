from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import MovieInfo
from .serializers import MovieSerializer

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


class movieView(viewsets.ModelViewSet):
    queryset = MovieInfo.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieInfo.objects.filter(genre='action')
    serializer_class = MovieSerializer