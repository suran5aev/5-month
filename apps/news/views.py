from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import News
from .serializers import NewsSerializer

# Create your views here.

class NewsViewSet(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CreateNewsAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class RetrieveNewsAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class UpdateNewsAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class DeleteNewsAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer