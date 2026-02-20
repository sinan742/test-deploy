from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=200)

    def __str__(self):
        return self.place

class Course(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='cor')   