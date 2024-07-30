from django.urls import path
from apps.news.views import CreateNewsAPIView, RetrieveNewsAPIView, UpdateNewsAPIView, DeleteNewsAPIView, NewsViewSet

urlpatterns = [
    path('', NewsViewSet.as_view(), name="api_news"),
    path('create/', CreateNewsAPIView.as_view(), name="api_news_create"),
    path('<int:pk>/', RetrieveNewsAPIView.as_view(), name="api_news_detail"),
    path('update/<int:pk>/', UpdateNewsAPIView.as_view(), name="api_news_update"),
    path('destroy/<int:pk>/', DeleteNewsAPIView.as_view(), name="api_news_destroy"),
]