from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import  *
from students.views import *
from courses.views import *
from payment.views import *
router = DefaultRouter()
router.register('director',DirectorViewset,basename='director')
router.register('manager',ManagerViewset)
router.register('teacher',TeacherViewset)
router.register('course',CourseViewset)
router.register('students',StudentViewset,basename='students')
router.register('rooms',RoomViewset)
router.register('groups',GroupsViewset)
router.register('test',TestViewset)
router.register('davomat',DavomatViewset)
router.register('payment',StudentPaymentViewset)
router.register('classroom',ClassRoomViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('info/<int:pk>/',StudentPaymentInfo.as_view()),
    path('paymenttype/',PaymentAbout.as_view()),
    path('group_student/',group_student, ),
   

]
