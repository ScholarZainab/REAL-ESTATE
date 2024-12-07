# Backend: Django - /real_estate/urls.py
from django.urls import path
from .views import ListProperty, GetListings, UploadDocument

urlpatterns = [
    path('listings/', GetListings.as_view(), name='get_listings'),
    path('listings/create/', ListProperty.as_view(), name='list_property'),
    path('document/upload/', UploadDocument.as_view(), name='upload_document'),
]
