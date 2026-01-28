from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Fundraiser
from .serializers import FundraiserSerializer
from .models import Fundraiser, Pledge
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer

class FundraiserList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
       fundraisers = Fundraiser.objects.all()
       serializer = FundraiserSerializer(fundraisers, many=True)
       return Response(serializer.data)
   
    def post(self, request):
       serializer = FundraiserSerializer(data=request.data, context={"request": request})
       if serializer.is_valid():
           serializer.save(owner=request.user)
           return Response(
               serializer.data,
               status=status.HTTP_201_CREATED
           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )
   
class FundraiserDetail(APIView):
   def get(self, request, pk):
       fundraiser = get_object_or_404(Fundraiser, pk=pk)
       serializer = FundraiserDetailSerializer(fundraiser)
       return Response(serializer.data)
   
class PledgeList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
      pledges = Pledge.objects.all()
      serializer = PledgeSerializer(pledges, many=True)
      return Response(serializer.data)

    def post(self, request):
       serializer = PledgeSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(
             serializer.data,
              status=status.HTTP_201_CREATED
          )
       return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
      )