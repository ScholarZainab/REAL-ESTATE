# Backend: Django - /real_estate/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Property, Document
from .serializers import PropertySerializer, DocumentSerializer

class GetListings(APIView):
    def get(self, request):
        listings = Property.objects.all()
        serializer = PropertySerializer(listings, many=True)
        return Response(serializer.data)

class ListProperty(APIView):
    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Property listed successfully!'}, status=201)
        return Response(serializer.errors, status=400)

class UploadDocument(APIView):
    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Document uploaded successfully!'}, status=201)
        return Response(serializer.errors, status=400)
