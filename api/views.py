from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import HeartData, PatientProfile
from api.serializers import (
    HeartRateSerializer,
    PatientSerializer,
    RegistrationSerializer,
)


class PatientView(ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = PatientProfile.objects.all()

    def perform_create(self, serializer):
        request = self.request
        serializer.save(user=request.user)


class PatientDetailView(RetrieveAPIView):
    serializer_class = PatientSerializer
    queryset = PatientProfile.objects.all()


class RegisterView(CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = get_user_model().objects.all()


class HeartDataView(APIView):
    def get(self, request, pk=None):
        queryset = HeartData.objects.all()
        serializer = HeartRateSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        serializer = HeartRateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not hasattr(request.user, "patient_profile"):
            return Response(
                {
                    "error": "Please create a patient profile before entering heart data."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save(patient=request.user.patient_profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class HeartDataDetailView(RetrieveAPIView):
    serializer_class = HeartRateSerializer
    queryset = HeartData.objects.all()
