from django.urls import path, include
from django.conf import settings

from .views import (
    StatusAPIView,
    StatusAPIDetailView,
)
app_name = 'api-status'

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('<int:id>/', StatusAPIDetailView.as_view(), name='detail'),
]
