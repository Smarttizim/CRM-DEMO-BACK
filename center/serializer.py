from rest_framework import serializers
from .models import *
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"
    def create(self, validated_data):
        return Director.objects.create_user(username=validated_data['username'],password=validated_data['password'])
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"
    def create(self, validated_data):
        return Manager.objects.create_user(username=validated_data['username'],password=validated_data['password'])
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
    def create(self, validated_data):
        return Teacher.objects.create_user(username=validated_data['username'],password=validated_data['password'])