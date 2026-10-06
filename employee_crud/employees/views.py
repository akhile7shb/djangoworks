from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from employees.models import Employee
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class EmployeeList(View):
    def get(self,request):
        data=Employee.objects.all().values()
        s=list(data)

        return JsonResponse(s,safe=False)

from json import loads

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCreate(View):
    def post(self,request):
        data = loads(request.body)
        eid=data['empid']
        n=data['name']
        a=data['age']
        p=data['place']
        g=data['gender']
        s=data['salary']
        j=data['joining_date']
        d=data['designation']

        s=Employee.objects.create(empid=eid,name=n,age=a,place=p,gender=g,salary=s,joining_date=j,designation=d)
        s.save()

        return JsonResponse({"message":"Inserted data Succesfully"})


class EmployeeRetrieve(View):
    def get(self,request,i):
        s=list(Employee.objects.filter(empid=i).values())
        if s:
            return JsonResponse(s,safe=False)
        else:
            return JsonResponse({"message":"No Employee Data"})


@method_decorator(csrf_exempt,name='dispatch')
class EmployeeFullUpdate(View):
    def put(self,request,i):
        data=loads(request.body)
        try:
            s=Employee.objects.get(empid=i)
            s.empid=data['empid']
            s.name=data['name']
            s.age=data['age']
            s.place=data['place']
            s.gender=data['gender']
            s.salary=data['salary']
            s.joining_date=data['joining_date']
            s.designation=data['designation']
            s.save()

            return JsonResponse({"message":"Successfully Updated"})

        except:
            return JsonResponse({"message":"No Employee Data"})

@method_decorator(csrf_exempt,name='dispatch')
class EmployeePartialUpdate(View):
    def patch(self,request,i):
        data=loads(request.body)

        try:
            s=Employee.objects.get(empid=i)

            if 'empid' in data:
                s.empid = data['empid']
            if 'name' in data:
                s.name = data['name']
            if 'age' in data:
                s.age = data['age']
            if 'place' in data:
                s.place = data['place']
            if 'gender' in data:
                s.gender = data['gender']
            if 'salary' in data:
                s.salary = data['salary']
            if 'joining_date' in data:
                s.joining_date = data['joining_date']
            if 'designation' in data:
                s.designation = data['designation']

            s.save()

            return JsonResponse({"message": "Successfully Updated"})

        except:
            return JsonResponse({"message": "No Employee Data"})

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeDelete(View):
    def delete(self,request,i):
        s=Employee.objects.get(empid=i)
        s.delete()

        return JsonResponse({"Message":"Deleted Successfully"})