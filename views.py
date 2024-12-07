# real_estate/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Property, Solicitor
from .serializers import PropertySerializer, SolicitorSerializer

class FeaturedListings(APIView):
    def get(self, request):
        featured = Property.objects.filter(category__in=['Platinum', 'Gold']).order_by('category')
        serializer = PropertySerializer(featured, many=True)
        return Response(serializer.data)

class SolicitorList(APIView):
    def get(self, request):
        solicitors = Solicitor.objects.filter(verified=True)
        serializer = SolicitorSerializer(solicitors, many=True)
        return Response(serializer.data)
