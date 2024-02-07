from django.shortcuts import render

# Create your views here.

from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1987)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=1981,deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(job='MANAGER')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gte=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[:5]
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__month='12',hiredate__day='17')   #date
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__startswith='A')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(job__endswith='MAN')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)

    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='CHICAGO')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname__contains='R')

    EMPOBJECTS=Emp.objects.select_related('deptno').order_by(Length('ename'))
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__regex=r'\w{6}')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__regex=r'^A')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(Q(job='MANAGER') & Q(sal__gt=2000))
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(Q(job='ANALYST') | Q(hiredate__year=1987))
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__contains='R')
    
    #EMPOBJECTS=Emp.objects.select_related('deptno').all()

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    empmgro=Emp.objects.select_related('mgr').all()
    empmgro=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    empmgro=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    empmgro=Emp.objects.select_related('mgr').filter(mgr__isnull=False,mgr__ename='BLAKE')
    empmgro=Emp.objects.select_related('mgr').order_by(Length('ename'))
    empmgro=Emp.objects.select_related('mgr').filter(ename__regex=r'^A')
    empmgro=Emp.objects.select_related('mgr').filter(ename__regex=r'\w{5}')
    empmgro=Emp.objects.select_related('mgr').filter(job__endswith='MAN')
    empmgro=Emp.objects.select_related('mgr').filter(hiredate__month='12')
    empmgro=Emp.objects.select_related('mgr').filter(job='ANALYST')
    empmgro=Emp.objects.select_related('mgr').all()[:3]
    empmgro=Emp.objects.select_related('mgr').filter(comm__isnull=False)
    empmgro=Emp.objects.select_related('mgr').filter(hiredate__year=1981)
    empmgro=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    empmgro=Emp.objects.select_related('mgr').filter(Q(job='MANAGER') & Q(sal__gt=2000))
    empmgro=Emp.objects.select_related('mgr').filter(mgr__ename__regex=r'E$')

    d={'empmgro':empmgro}
    return render(request,'selfjoins.html',d)

def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(job='MANAGER') & Q(sal__gt=2000))
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=1981)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH') | Q(mgr__ename='JONES'))
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__regex=r'\w{10}')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__deptno=20) | Q(deptno__dlocation='DALLAS'))
    emd=Emp.objects.select_related('deptno','mgr').all()[:6]
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation__contains='Y')

    emd=Emp.objects.select_related('deptno','mgr').filter(ename__startswith='A')
    emd=Emp.objects.select_related('deptno','mgr').filter(job__endswith='MAN')
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=1981,deptno=10)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='MANAGER')
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__month='12')
    emd=Emp.objects.select_related('deptno','mgr').filter(job='CLERK')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=False,mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__deptno=10) | Q(ename='ALLEN'))

    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dlocation='BOSTON') | Q(sal__gte=3000))
    emd=Emp.objects.select_related('deptno','mgr').order_by(Length('deptno__dname'))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__regex=r'S$')
    emd=Emp.objects.select_related('deptno','mgr').order_by('ename')
    emd=Emp.objects.select_related('deptno','mgr').order_by('-deptno__dname')
    emd=Emp.objects.select_related('deptno','mgr').order_by(Length('deptno__dname').desc())
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno__deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='SALES') | Q(ename='ALLEN'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__deptno=10) & Q(mgr__ename='KING'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(sal__gt=3000) | Q(ename='ALLEN'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(hiredate__month=4) | Q(job='MANAGER'))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation__startswith='NE')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__regex=r'^R\w{7}')
    emd=Emp.objects.select_related('deptno','mgr').order_by('deptno__dlocation')

    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)

def emp_salgrade(request):
    EO=Emp.objects.all()
    SO=Salgrade.objects.all()
    
    # Retrieving the data of employees who belong to Grade 4

    SO=Salgrade.objects.filter(grade=4)                                #[grade4 SalgradeObjects] 
    EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))

    # Retrieving the data of employees who belong to Grade 3,4

    SO=Salgrade.objects.filter(grade__in=(3,4))
    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))


    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)