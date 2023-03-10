from rest_framework import serializers,fields
from .models import Student,Davomat,Test
from courses.serializer import GroupSerializer,ClassRoomSerializer
from center.serializer import ManagerSerializer
from center.models import User
from payment.serializer import StudentPaymentSerializer
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Test
        fields ='__all__'
class Davomatserializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'
        depth=1
class StudentSerializer(serializers.ModelSerializer):
    davomat =Davomatserializer(many=True,read_only=True)
    # last_payment = serializers.SerializerMethodField()
    payment = StudentPaymentSerializer(many=True,read_only=True)
    groups = GroupSerializer(many=True,read_only=True)
    classes = ClassRoomSerializer(many=True,read_only=True)
    def get_last_payment(self, obj):
        return obj.tolov
    class Meta:
        model = Student
        fields ="__all__"
        read_only_fields = ['id', 'user','payment','groups','classes']
