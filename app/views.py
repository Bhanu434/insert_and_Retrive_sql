from django.shortcuts import render
from app.models import *
# Create your views here.
def display_emp(request):
    QLEO=Emp.objects.all()
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)
def display_dept(request):
    QLDO=Dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)
def display_salgrade(request):
    QLSO=Salgrade.objects.all()
    d={'QLSO':QLSO}
    return render(request,'display_salgrade.html',d)
def display_bonus(request):
    QLBO=Bonus.objects.all()
    d={'QLBO':QLBO}
    return render(request,'display_bonus.html',d)
def insert_dept(request):
    dno=int(input('Enter Deptno :- '))
    dn=input('Enter Dname :- ')
    l=input('Enter Loc :- ')
    DO=Dept.objects.get_or_create(Deptno=dno,Dname=dn,Loc=l)[0]
    DO.save()
    QLDO=Dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)
def insert_emp(request):
    eno=int(input('Enter Emp id :- '))
    en=input('Enter name :- ')
    j=input('Enter job :- ')
    m=int(input('Enter MGR  :- '))
    h=input('Enter Date :- ')
    s=int(input('Enter Salary  :- '))
    c=int(input('Enter Comm  :- '))
    dno=int(input('Enter dno  :- '))
    DO=Dept.objects.get(Deptno=dno)
    EO=Emp.objects.get_or_create(Empno=eno,Ename=en,Job=j,MGR=m,Hiredate=h,Salary=s,Comm=c,Deptno=DO)
    EO.save()
    QLEO=Emp.objects.all()
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)
def insert_salgrade(request):
    pk=int(input('Enter pk no :- '))
    g=int(input('Enter Grade :- '))
    l=int(input('Enter losal :- '))
    h=int(input('Enter hisal :- '))
    SO=Salgrade.objects.get_or_create(pk=pk,Grade=g,Losal=l,Hisal=h)[0]
    SO.save()
    QLSO=Salgrade.objects.all()
    d={'QLSO':QLSO}
    return render(request,'display_salgrade.html',d)

