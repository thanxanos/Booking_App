from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Room, OccupiedDate, User
from .serializers import RoomSerializer, OccupiedDateSerializer, UserSerializer
# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'rooms': reverse('room-list', request=request, format=format)
  })


class RoomList(generics.ListCreateAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveDestroyAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer

class OccupiedDatesList(generics.ListCreateAPIView):
  queryset = OccupiedDate.objects.all()
  serializer_class = OccupiedDateSerializer
  
  def get_queryset(self):
    user = self.request.user
    if not user.is_superuser and not user.is_staff:
      return OccupiedDate.objects.filter(user=user)
    
    return super().get_queryset()

class OccupiedDatesDetail(generics.RetrieveDestroyAPIView):
  queryset = OccupiedDate.objects.all()
  serializer_class = OccupiedDateSerializer

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_queryset(self):
    return super().get_queryset()

class OccupiedDatesDetail(generics.RetrieveDestroyAPIView):
  queryset = OccupiedDate.objects.all()
  serializer_class = OccupiedDateSerializer