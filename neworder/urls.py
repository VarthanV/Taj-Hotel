from django.urls import path
from .import views
urlpatterns = [
    path('items/',views.ItemManipulationView.as_view())
]
