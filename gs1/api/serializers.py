from django import forms
from rest_framework import serializers
from .models import Student

# 1. Create Serializer for Student Model
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)  # read only means it is only for display read data.
    name = serializers.CharField(max_length = 100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)


# 2.  We use this because it helps User Input Handling , File Validation, Security
class StudentForm(forms.Form):
    id = serializers.IntegerField(read_only = True)  # read only means it is only for display read data.
    name = forms.CharField(max_length = 100)
    age = forms.IntegerField()
    city = forms.CharField(max_length = 100)



# 3. Model Serializer  used for conveting Models / Database Table INTO JSON Format
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','age','city']


#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Update Data >>>>>>
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)  # read only means it is only for display read data.
    name = serializers.CharField(max_length = 100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    def update(self, instance, validated_data): # instance:- represents the old data, validated_data:- represents the new data
        
        # Update fields
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)

        # Save the updated instance
        instance.save()
        return instance








#  Serializer Fields

# name = serializers.CharField(max_length=100)  # CharField

# roll = serializers.IntegerField()     # IntegerField

# price = serializers.FloatField() # FloatField --> for decimal numbers.

# is_active = serializers.BooleanField()  # BooleanField --> Used for True/False.

# email = serializers.EmailField()   #  EmailField --> Validates email addresses.

# website = serializers.URLField() # URLField --> Validates URLs.

# dob = serializers.DateField()  #  DateField --> Used for dates.

# time= serializers.TimeField()  #  TimeField ---> Used for time.

# created = serializers.DateTimeField()  # DateTimeField ---> Used for date and time.

# salary = serializers.DecimalField(max_digits=10, decimal_places=2) # DecimalField ---> Used for precise decimal values.

#gender = serializers.ChoiceField(choices=['Male', 'Female']) #ChoiceField - Used when values are fixed.

# file = serializers.FileField() #  FileField ---> Used for file uploads.

# image = serializers.ImageField()  # ImageField --> Used for image uploads.


## ListField ---> Used for lists/arrays.
#skills = serializers.ListField(
    # child=serializers.CharField()  ) 


# data = serializers.JSONField()    # JSONField ---> Used for JSON data.

# created_by = serializers.HiddenField(default="admin")  # HiddenField ---> Hidden from user input.

# id = serializers.ReadOnlyField() # ReadOnlyField


##  SerializerMethodField ---> Custom calculated field.
# full_name = serializers.SerializerMethodField()
# def get_full_name(self, obj):
#     return obj.first_name + obj.last_name


## PrimaryKeyRelatedField ---> Used for relationships.
# student = serializers.PrimaryKeyRelatedField(
#     queryset=Student.objects.all()           )


# # HyperlinkedIdentityField ---> Used for hyperlinks in APIs.
# url = serializers.HyperlinkedIdentityField(
#     view_name='student-detail'            )


# id = serializers.UUIDField()  # UUIDField ---> Used for UUID values.

# ip = serializers.IPAddressField() # IPAddressField ---> Used for IP addresses.

# phone = serializers.RegexField(regex=r'^\d{10}$')  # RegexField ---> Validates using regex pattern.

# slug = serializers.SlugField()  # SlugField ---> Used for slugs.

# DictField ---> Used for dictionary objects.
# data = serializers.DictField(
#     child=serializers.CharField() )



