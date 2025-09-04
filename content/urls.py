from django.urls import path
from .views import UploadFile


urlpatterns = [
    path('upload', UploadFile.as_view())
]