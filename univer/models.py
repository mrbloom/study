from django.db import models
from django.core.validators import MaxValueValidator

class CommonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)

    class Meta:
        abstract = True


class Teacher(CommonInfo):
    subject = models.CharField(max_length=50)

class Student(CommonInfo):
    avg_mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator])
    # quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=50)
    pass

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    pass