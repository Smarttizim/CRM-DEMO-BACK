from rest_framework import serializers,status,fields
from .models import *
from rest_framework.response import Response
from center.serializer import *
from students.models import Student
class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))
# from students.serializer import StudentSerializer
class CourseSerializer(serializers.ModelSerializer):
    students_count= serializers.SerializerMethodField()
    groups_count = serializers.SerializerMethodField()
    def get_students_count(self, obj):
        return obj.student_count
    def get_groups_count(self, obj):
        return obj.group_count
    class Meta:
        model = Course
        fields = ['id','name','cost','students_count','groups_count']
        read_only_fields = ['id','students_count','groups_count']
class RoomSerializer(serializers.ModelSerializer):
    groups_count = serializers.SerializerMethodField()
    def get_groups_count(self, obj):
        return obj.group_count
    class Meta:
        model = Room
        fields = ['id','name','student_count','groups_count']
        read_only_fields = ['id','groups_count']
class GroupSerializer(serializers.ModelSerializer):
    # continue_time = serializers.SerializerMethodField()
    # def get_continue_time(self, obj):
    #     return (obj.finish - obj.start).days
   
    class Meta:
        model = Groups
        fields = '__all__'
        # read_only_fields = ['continue_time']
        depth=1
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
        depth=1
    