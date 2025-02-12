from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import PatientProfile, HeartData


class PatientSerializer(serializers.ModelSerializer):
    user =serializers.StringRelatedField()
    class Meta:
        model = PatientProfile
        fields = ("id",'user', 'medical_record', )

class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password1 =serializers.CharField(write_only=True)

    class Meta:
        model =get_user_model()
        fields = ['username',"email","password","password1"]

    def validate(self, data):
        password = data.get("password")
        password1 =data.get("password1")
        if password!=password1:
            raise serializers.ValidationError({'error':"passwords do not match."})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        password1 =validated_data.pop("password1")
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password1)
        user.save()
        return user

class HeartRateSerializer(serializers.ModelSerializer):
    patient =serializers.StringRelatedField()

    class Meta:
        model = HeartData
        fields = ("id",'heart_rate', 'timestamp', 'patient', )


