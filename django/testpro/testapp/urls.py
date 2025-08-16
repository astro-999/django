from django.urls import path
from .import views
urlpatterns = [
    path("index",views.TestApiView.as_view()),
]