from django.db import models
# Create your models here.
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _
from students.models import Student
from center.models import Teacher
from django.db.models import *
from center.models import *
class Course(models.Model):
    name = models.CharField(max_length=100,help_text=_("Enter course name"),verbose_name=_("Course name"))
    cost = models.CharField(max_length=600,verbose_name=_("Cost"),help_text=_("Enter cost"))
    @property
    def student_count(self):
        results = self.groups.all()
        summa = 0
        for result in results:
            summa +=len(result.student.all())
        return summa
    @property
    def group_count(self):
        results = self.groups.all()
        return len(results)
    
    
        
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Courses"
        verbose_name = " Course "
        verbose_name_plural = " Courses "
    
class Room(models.Model):
    name = models.CharField(max_length=500,verbose_name=_("Room name"))
    student_count = models.IntegerField(verbose_name=_("Students Count"))
    @property
    def group_count(self):
        results = self.groups.all()
        return len(results)
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Rooms"
        verbose_name = " Room "
        verbose_name_plural = " Rooms "
    
class Groups(models.Model):
    class Education(models.TextChoices):
        ONLINE = 'online','Online'
        OFFLINE = 'offline','Offline'
    day = (
        # ('Sun','Sun'),
        ('Mon','Mon'),
        ('Tue','Tue'),
        ('Wed','Wed'),
        ('Thu','Thu'),
        ('Fri','Fri'),
        ('Sat','Sat'),
        ('Sun','Sun')
    )
    class Status(models.TextChoices):
        ACTIVE = 'active','Active'
        WAITING = 'waiting','Waiting'
    name = models.CharField(max_length=100,verbose_name=_("Group name"))
    course = models.ForeignKey(Course,related_name='groups',on_delete=models.SET_NULL,null=True,blank=True)
    education = models.CharField(max_length=10,choices=Education.choices,null=True,blank=True)
    day =  MultiSelectField(max_length=100,choices=day,null=True,blank=True)
    student = models.ManyToManyField(Student,related_name='groups')
    room =models.ForeignKey(Room,related_name='groups',on_delete=models.SET_NULL,null=True,blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True,related_name='teacher')
    status = models.CharField(max_length=10,choices=Status.choices,null=True,blank=True)
    start = models.DateField(null=True,blank=True)
    finish = models.DateField(null=True,blank=True)
    start_lesson = models.TimeField(null=True,blank=True)
    finish_lesson = models.TimeField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='groupuser')
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Groups"
        verbose_name = " Group "
        verbose_name_plural = " Groups "
    
class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student,related_name='classes')
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='classuser')
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Class Room"
        verbose_name = " Class Room "
        verbose_name_plural = " Class Room "
    

