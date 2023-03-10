from rest_framework import serializers
from .models import StudentPayment
class StudentPaymentSerializer(serializers.ModelSerializer):
    sana =  serializers.SerializerMethodField()
    def get_sana(self,obj):
        return (obj.date).strftime('%d %b, %Y')
    class Meta:
        model = StudentPayment
        fields = '__all__'
        depth=1
