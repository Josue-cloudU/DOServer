from django.contrib.auth.models import User
from rest_framework import serializers
from savings.models import Cundina
from .models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class SavingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cundina
        fields = "__all__"

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cundina
        fields = ["user", "descripcion", "cantahorro", "nparticipantes", "status"]

    def create(self, validated_data):
        cundina = Cundina(user=validated_data["user"], descripcion=validated_data["descripcion"], cantahorro=validated_data["cantahorro"], nparticipantes=validated_data["nparticipantes"], status=validated_data["status"])
        cundina.save()
        return cundina

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
