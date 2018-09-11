from django.db import models
from django.core.validators import MaxValueValidator

# from phonenumber_field.modelfields import PhoneNumberField
#
# class Image(models.Model):
#     image = models.ImageField()
#     alt_text = models.CharField(max_length=100)

class CommonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    # phone = PhoneNumberField(blank=True)

    class Meta:
        abstract = True


class Teacher(CommonInfo):
    subject = models.CharField(max_length=50)

class Student(CommonInfo):
    avg_mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator])
    # quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)

class Class(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student)
    class Meta:
        verbose_name_plural = 'Classes'

#
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ManyToManyField(Teacher) #,related_name='quizzes',default=None
    student = models.ManyToManyField(Student)

    # student = models.ForeignKey(Student,related_name='quizzes') #,default=None,null=True
    # teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='quizzes',default=None)


class Question(models.Model):
    title = models.CharField(max_length=100)
    question_text = models.TextField()
    question_answer = models.TextField()
    # image = models.ManyToManyField(Image)
    # quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions')

class Choice(models.Model):
    text = models.TextField()
    # image = models.ManyToManyField(Image)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='choices')

