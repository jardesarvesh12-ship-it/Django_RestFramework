from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)



    def create(self, validated_data):                     # this is used to save data 
        return Student.objects.create(**validated_data)   # ** is used to unpack the data
 # goto >> gs3 >>>> myapp.py >>>> and write function to save data 



# goto gs3 >> api >> write code for update in serializer.py 
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance 