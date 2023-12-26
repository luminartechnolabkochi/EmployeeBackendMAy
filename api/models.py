from django.db import models

# Create your models here.
class Employee(models.Model):
    # name,age,salary,department,email
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    age=models.CharField(max_length=20)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.name
