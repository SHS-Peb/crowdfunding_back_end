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

    def patch(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)

    # allow owner OR admin/staff
        if fundraiser.owner != request.user and not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = FundraiserSerializer(
            fundraiser,
            data=request.data,
            partial=True,
            context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)

    # allow owner OR admin/staff
        if fundraiser.owner != request.user and not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        fundraiser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   
   
class PledgeList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
      pledges = Pledge.objects.all()
      serializer = PledgeSerializer(pledges, many=True)
      return Response(serializer.data)

    def post(self, request):
       serializer = PledgeSerializer(data=request.data, context={"request": request})
       if serializer.is_valid():
           serializer.save(supporter=request.user)
           return Response(
             serializer.data,
              status=status.HTTP_201_CREATED
          )
       return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
      )
    
class PledgeDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, pk):
        pledge = get_object_or_404(Pledge, pk=pk)

        if pledge.supporter != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
