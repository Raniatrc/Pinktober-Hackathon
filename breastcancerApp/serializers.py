from rest_framework import serializers
from .models import MedicalCenter, WalkChallenge

class MedicalCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCenter
        fields = '__all__'

class WalkChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkChallenge
        fields = '__all__'
