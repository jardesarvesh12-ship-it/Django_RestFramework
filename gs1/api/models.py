from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    city = models.CharField(max_length=100)




# this is used to display the name of the student in the admin panel when we display this model in the admin panel. 
    def __str__(self):
        return self.name
    


##

#     id = models.BigIntegerField()          # very large integer num
#     rating = models.SmallIntegerField()     #small integer numbers
#     quantity = models.PositiveIntegerField() # +ve integer fields
#     level = models.PositiveSmallIntegerField() # +ve smaller int


#     cgpa = models.FloatField()  # Decimal numbers
#     salary = models.DecimalField(max_digits = 10, decimal_places=2) # store decimal values  (max_digits = 10, decimal_places=2)

#     is_active = models.BooleanField() # True/False

# # ----> Date and Time Fields
#     o_date = models.DateField() # store Only Date  (YYYY-MM-DD)
#     o_time = models.TimeField() # store only time  (HH:MM:SS)
#     date_time = models.DateTimeField() # store date + time
#     created_at = models.DateTimeField(auto_now_add=True)  # runs only once
#     updated_at = models.DateTimeField(auto_now=True)      # runs every time you save/update the object


# #  ----> File & Media Fields

#     file = models.FileField(upload_to='files/')
#     image = models.ImageField(upload_to='images/')



# # ---->  Email / URL Fields
#     e_mail = models.EmailField() # Stores email addresses (Built in validation)
#     url = models.URLField() # Stores website URLs (Validates proper URL format)
#     slug = models.SlugField() # Used for SEO-friendly URLs (clean, readable links) , unique=True for unique URLs


# #------------------> Special Fields

#     UUIDField = modelsUUIDField()
#     # Stores universally unique identifiers (UUIDs)
#     # Useful for secure, non-guessable IDs instead of integers
#     # (e.g., 550e8400-e29b-41d4-a716-446655440000)

#     JSONField = models.JSONField()
#     # Stores JSON data (dict/list) directly in the database
#     # Very useful for flexible or dynamic data
#     # e.g {"name": "Sarvesh", "skills": ["AI", "Django"]}

#     BinaryField = models.BinaryField()
#     # Stores raw binary data (bytes)
#     # Rarely used in practice (files are usually handled with FileField)
#     # e.g file, images, encrypted data, audio, video files

#     GenericIPAddressField = models.GenericIPAddressField()
#     # Stores IPv4 or IPv6 addresses (IP addresses of clients)
#     # Automatically detects and stores either format
#     # Useful for logs, analytics, security, and geographic data

# #  ----------> Relationship Fields


# # All of these are used in Django to connect models (tables).
#     ForeignKey = models.ForeignKey() # Many to one request
#     ManyToManyField = models.ManyToManyField()  # Many to Many
#     OneToOneField = models.OneToOneField()

