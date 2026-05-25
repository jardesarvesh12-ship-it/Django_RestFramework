from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        


# ModelSerializer used for converting Models / Database Table INTO JSON Format
# Meta class is used to provide metadata about the serializer
#  It provide built in get,post,put,patch,delete methods




# ********************* ModelSerializer Validation* *********************


# 3. Validators Level Validation
def start_with_r(value):
    if value['0'].lower() != 'r':
        raise serializers.ValidationError("Name must start with r")
    return value 


from rest_framework import serializer
class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']


# Fiels Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value 


#  2. Object Level Validation --> we can use validate to perform object level validation
def validate(self, data):
    nm = data.get('name')
    ct = data.get('city')
    if nm.lower() == 'Shav' and ct.lower() != 'Pune':
        raise serializers.ValidationError("City must be Pune")
    return data 