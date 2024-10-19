from rest_framework import generics
from .models import MedicalCenter, WalkChallenge
from .serializers import MedicalCenterSerializer, WalkChallengeSerializer

# Medical Center Views
class MedicalCenterListCreate(generics.ListCreateAPIView):
    queryset = MedicalCenter.objects.all()
    serializer_class = MedicalCenterSerializer

class MedicalCenterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalCenter.objects.all()
    serializer_class = MedicalCenterSerializer

# Walk Challenge Views
class WalkChallengeListCreate(generics.ListCreateAPIView):
    queryset = WalkChallenge.objects.all()
    serializer_class = WalkChallengeSerializer

class WalkChallengeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WalkChallenge.objects.all()
    serializer_class = WalkChallengeSerializer


