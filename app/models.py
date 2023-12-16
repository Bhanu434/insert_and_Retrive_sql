from django.db import models

# Create your models here.
class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100,unique=True)
    Loc=models.CharField(max_length=100)
    def __str__(self):
        return self.Dname
    
class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    MGR=models.IntegerField()
    Hiredate=models.DateField()
    Salary=models.IntegerField()
    Comm=models.IntegerField(null=True)
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.Ename
class Salgrade(models.Model):
    Grade=models.IntegerField()
    Losal=models.IntegerField()
    Hisal=models.IntegerField()
    def __str__(self):
        return self.Grade
class Bonus(models.Model):
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    sal=models.IntegerField(null=True)
    def __str__(self):
        return self.job

