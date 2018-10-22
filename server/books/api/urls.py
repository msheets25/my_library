from django.urls import path
from .views import bookAPIView

app_name = 'api-books'

urlpatterns = [
  path('', bookAPIView.as_view(), name='book-create'),
]
