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