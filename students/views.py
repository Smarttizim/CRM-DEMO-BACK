from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from courses.models import Groups
import json
from payment.models import StudentPayment
from courses.permissions import IsManagerandDirectorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import * 
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import *
import codecs
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
fs = FileSystemStorage(location='tmp/')
from rest_framework.decorators import action
class TestViewset(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES["file"]
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)
        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        results_list = []
        for id_, row in enumerate(reader):
            (
                test_kodi,
                fan_nomi,
                talaba,
                telefon_raqam,
                savollar_soni,
                togri_javoblar
            ) = row
            results_list.append(
                Test(
                    test_kodi=test_kodi,
                    fan_nomi=fan_nomi,
                    talaba=talaba,
                    telefon_raqam=telefon_raqam,
                    savollar_soni=savollar_soni,
                    togri_javoblar=togri_javoblar,
                )
            )
        print(results_list)
        Test.objects.bulk_create(results_list)
        return Response("Successfully upload the data")
    @action(detail=False, methods=['POST'])
    def upload_data_with_validation(self, request):
        file = request.FILES.get("file")
        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        results_list = []
        for row in serializer.data:
            results_list.append(
                Test(
                    test_kodi=row["test_kodi"],
                    fan_nomi=row["fan_nomi"],
                    talaba=row["talaba"],
                    telefon_raqam = row['telefon_raqam'],
                    savollar_soni=row["savollar_soni"],
                    togri_javoblar=row["togri_javoblar"],

                )
            )
        Test.objects.bulk_create(results_list)
        return Response("Successfully upload the data")

class StudentViewset(ModelViewSet):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        student = Student.objects.create(name=data['name'],phone=data['phone'],user=request.user,parent=data.get('parent',None),birth=data.get('birth',None),added=data.get('added',None),father_name=data.get('father_name'),mother_name=data.get('mother_name',None),language=data.get('language',None),address=data.get('address',None),email=data.get('email',None))
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        student_object = self.get_object()
        data = request.data
        student_object.name = data.get('name',student_object.name)  
        student_object.birth = data.get('birth',student_object.birth)
        student_object.parent = data.get('parent',student_object.parent)
        student_object.address = data.get('address',student_object.address)
        student_object.email = data.get('email',student_object.email)
        student_object.father_name = data.get('father_name',student_object.father_name)
        student_object.mother_name = data.get('mother_name',student_object.mother_name)
        student_object.language = data.get('language',student_object.language)
        student_object.save()
        serializer = StudentSerializer(student_object)
        return Response(serializer.data)
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class DavomatViewset(ModelViewSet):
    queryset =  Davomat.objects.all()
    serializer_class = Davomatserializer
    def create(self, request, *args, **kwargs):
        data = request.data
        if 'students' in data:
            for student in data['students']:
                try:
                    talaba = Student.objects.get(id=student['id'])
                    print(talaba.name)
                    Davomat.objects.create(student=talaba,status=student.get('status',True),description=student.get('description','Sabab korsatilmagan'))
                except Student.DoesNotExist:
                    pass
            return Response("Davomat olindi!")
        else:
            return Response('Student Doesnt Found')
    def partial_update(self, request, *args, **kwargs):
        davomat_data = self.get_object()
        data = request.data
        if 'students' in data:
           for student in data['students']:
                try:
                    student = Student.objects.get(id=student['id'])
                    davomat_data.student =student
                    davomat_data.description = student.get('description',davomat_data.description)
                    davomat_data.status = student.get('status',davomat_data.status)
                    davomat_data.date = student.get('date',davomat_data.date)
                    serializer = Davomatserializer(davomat_data)
                    return Response(serializer.data)
                except Student.DoesNotExist:
                    return Response('Student not found')
        else:
            return Response('student field required')
    def update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
class StudentPaymentInfo(APIView):
    def get(self,request,pk):
        payments = []
        student  = Student.objects.get(id=pk)
        payment_students =StudentPayment.objects.filter(student=student)
        for group in student.groups.all():
            payment =payment_students.filter(group=Groups.objects.get(id=group.id)).last()
            if payment is not None:
                info ={}
                info['id'] = payment.id
                info['student_id'] = payment.student.id
                info['student_name']=payment.student.name
                info['cost'] = payment.cost
                info['date'] = payment.date
                info ['group'] = payment.group.name
                info['user'] = payment.user.username 
                payments.append(info)
        return Response(payments,status=status.HTTP_200_OK)
          
