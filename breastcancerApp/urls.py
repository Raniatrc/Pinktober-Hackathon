from django.urls import path
from .views import MedicalCenterListCreate, MedicalCenterRetrieveUpdateDestroy, WalkChallengeListCreate, WalkChallengeRetrieveUpdateDestroy

urlpatterns = [
    # Medical Center URLs
    path('medicalcenters/', MedicalCenterListCreate.as_view(), name='medicalcenter-list-create'),
    path('medicalcenters/<int:pk>/', MedicalCenterRetrieveUpdateDestroy.as_view(), name='medicalcenter-detail'),

    # Walk Challenge URLs
    path('walkchallenges/', WalkChallengeListCreate.as_view(), name='walkchallenge-list-create'),
    path('walkchallenges/<int:pk>/', WalkChallengeRetrieveUpdateDestroy.as_view(), name='walkchallenge-detail'),
]
