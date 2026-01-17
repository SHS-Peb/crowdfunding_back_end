
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Fundraiser
from .serializers import FundraiserSerializer

class FundraiserList(APIView):

   def get(self, request):
       fundraisers = Fundraiser.objects.all()
       serializer = FundraiserSerializer(fundraisers, many=True)
       return Response(serializer.data)