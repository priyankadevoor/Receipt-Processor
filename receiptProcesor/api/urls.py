from django.urls import path
from .views import process_receipt, get_points

urlpatterns = [
    path("receipts/process", process_receipt, name='process_receipt'),
    path("receipts/<str:receipt_id>/points", get_points, name='get_points')
]
