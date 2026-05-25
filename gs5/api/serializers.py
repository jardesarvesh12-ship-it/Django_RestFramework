from rest_framework import serializers
from .models import Student

# 3. Validators Level Validation
def start_with_r(value):
    if value['0'].lower() != 'r':
        raise serializers.ValidationError("Name must start with r")
    return value 


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators = [start_with_r])
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



# 1. Field level validation --> it is used to validate a single field at the time of POST data 
def valid_roll(self, value):
    if value >= 200:
        raise serializers.ValidationError("Seat full")
        return value



#  2. Object Level Validation --> we can use validate to perform object level validation
def validate(self, data):
    nm = data.get('name')
    ct = data.get('city')
    if nm.lower() == 'Shav' and ct.lower() != 'Pune':
        raise serializers.ValidationError("City must be Pune")
    return data 
