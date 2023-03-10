from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from center.models import Teacher
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManagerandDirectorOrReadOnly
class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [IsManagerandDirectorOrReadOnly]
class RoomViewset(ModelViewSet):
    queryset =  Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsManagerandDirectorOrReadOnly]
class GroupsViewset(ModelViewSet):
    queryset =  Groups.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [IsManagerandDirectorOrReadOnly]
    def create(self, request, *args, **kwargs):
        data = request.data
        group = Groups.objects.create(name=data['name'],education=data.get('education',None),status=data.get('status',None),start=data.get('start',None),start_lesson=data.get('start_lesson',None),finish=data.get('finish',None),finish_lesson=data.get('finish_lesson',None),user=request.user,day=data.get('day',None))
        group.save()
        if 'teacher' in data:
                teachers = data['teacher']
                try:
                    teacher = Teacher.objects.get(id=teachers)
                    group.teacher = teacher
                except Teacher.DoesNotExist:
                    pass
        if 'room' in data:
                room = data['room']
                try:
                    xona = Room.objects.get(id=room)
                    group.room = xona
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
                course = data['course']
                try:
                    courses = Course.objects.get(id=course)
                    group.course = courses
                except Course.DoesNotExist:
                    pass
        if 'students' in data:
            for student in data['students']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group.student.add(xona)
                except Student.DoesNotExist:
                    pass
        group.save()
        serializer = GroupSerializer(group)
        return Response(serializer.data)
    def partial_update(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        if 'teacher' in data:
                teachers = data['teacher']
                try:
                    teacher = Teacher.objects.get(id=teachers)
                    group_object.teacher= teacher
                except Teacher.DoesNotExist:
                    pass
        if 'room' in data:
                room = data['room']
                try:
                    xona = Room.objects.get(id=room)
                    group_object.room = xona
                except Room.DoesNotExist:
                    pass
        if 'course' in data:
                course = data['course']
                try:
                    courses = Course.objects.get(id=course)
                    group_object.course=courses
                except Course.DoesNotExist:
                    pass
        if 'students' in data:
            for student in data['students']:
                try:
                    xona = Student.objects.get(id=student['id'])
                    group_object.student.add(xona)
                except Student.DoesNotExist:
                    pass
        group_object.education=data.get('education',group_object.education)
        group_object.status=data.get('status',group_object.status)
        group_object.start=data.get('start',group_object.start)
        group_object.finish=data.get('finish',group_object.finish)
        group_object.day = data.get('day',group_object.day)
        group_object.start_lesson = data.get('start_lesson', group_object.start_lesson)
        group_object.finish_lesson = data.get('finish_lesson', group_object.finish_lesson)
        group_object.user=data.get(request.user,group_object.user)
        group_object.save()
        serializer = GroupSerializer(group_object)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        return self.partial_update(request,*args,**kwargs)
    def destroy(self, request, *args, **kwargs):
        group_object = self.get_object()
        data = request.data
        if 'id' in data:
            Groups.objects.filter(id=id).delete()
            return Response('Group deleted!')
        else:
            if 'teacher' in data:
                teachers = data['teacher']
                try:
                    xona = Teacher.objects.get(id=teachers)
                    group_object.teacher = None
                except Teacher.DoesNotExist:
                    pass
            if 'room' in data:
                for room in data['room']:
                    try:
                        xona = Room.objects.get(id=room)
                        group_object.room = None
                    except Room.DoesNotExist:
                        pass
            if 'course' in data:
                for course in data['course']:
                    try:
                        xona = Course.objects.get(id=course)
                        group_object.course=None
                    except Course.DoesNotExist:
                        pass
            if 'students' in data:
                for student in data['students']:
                    try:
                        xona = Student.objects.get(id=student['id'])
                        group_object.student.remove(xona)
                    except Student.DoesNotExist:
                        pass
            group_object.save()
            serializer = GroupSerializer(group_object)
            return Response(serializer.data)

class ClassRoomViewset(ModelViewSet):
    queryset=ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsManagerandDirectorOrReadOnly]
    def create(self, request, *args, **kwargs):
        data = request.data
        group = ClassRoom.objects.create(name=data['name'],user=request.user)
        group.save()
        if 'students' in data:
            for student in data['students']:
                try:
                    talaba = Student.objects.get(id=student['id'])
                    group.student.add(talaba)
                except Student.DoesNotExist:
                    pass
        serializer = ClassRoomSerializer(group)
        return Response(serializer.data)
    def partial_update(self, request, *args, **kwargs):
        class_object = self.get_object()
        data = request.data
        if 'students' in data:
            for student in data['students']:
                try:
                    talaba = Student.objects.get(id=student['id'])
                    class_object.student.add(talaba)
                except Student.DoesNotExist:
                    pass
        class_object.name = data.get('name',class_object.name)
        class_object.user=data.get(request.user,class_object.user)
        class_object.save()
        serializer = ClassRoomSerializer(class_object)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        return self.partial_update(request,*args,**kwargs)
    def destroy(self, request, *args, **kwargs):
        class_object = self.get_object()
        data = request.data
        if 'id' in data:
            ClassRoom.objects.filter(id=data['id']).delete()
            return Response('Class Deleted!')
        else:
            if 'students' in data:
                for student in data['students']:
                    try:
                        talaba = Student.objects.get(id=student['id'])
                        class_object.student.remove(talaba)
                    except Student.DoesNotExist:
                        pass
            class_object.save()
            serializer = ClassRoomSerializer(class_object)
            return Response(serializer.data)
                
        
                
        
