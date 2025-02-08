from django.urls import path
from .views import predict_performance

urlpatterns = [
    path("", predict_performance, name="predict_performance"),
]
