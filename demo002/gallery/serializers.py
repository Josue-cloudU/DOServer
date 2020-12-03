from django.contrib.auth.models import User
from rest_framework import serializers
from gallery.models import Item
from .models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["user", "category", "description", "status"]

    def create(self, validated_data):
        item = Item(user=validated_data["user"],category=validated_data["category"], description=validated_data["description"], status=validated_data["status"])
        item.save()
        return item

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

class ItemNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ItemCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "description", "status", "timestamp")
