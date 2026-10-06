from django.db.models import Model
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.utils import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

# Create your views here.
#api  view
class GoodMorning(View):
    def get(self,request):
        data={"message":"good morning"}
        return JsonResponse(data)
class HelloWorld(View):
    def get(self,request):
        data = {"message": "hello world"}
        return JsonResponse(data)
class GoodEvening(View):
    def get(self,request):
        data = {"message": "good evening"}
        return JsonResponse(data)

class UserDetails(View):
    def get(self,request):
        data=[
            {'name':'arun','age':20,'place':'ekm'},
            {'name': 'arun', 'age': 20, 'place': 'ekm'},
            {'name': 'arun', 'age': 20, 'place': 'ekm'}

        ]
        return JsonResponse(data,safe=False)

from myapp.models import Student

class StudentList(View):
    def get(self,request):
        s=Student.objects.all().values()
        print(s)
        print(type(s))
        data=list(s)
        print(data)
        print(type(data))
        return JsonResponse(list(s),safe=False)
from json import loads
#api view for creating a new student record
@method_decorator(csrf_exempt,name='dispatch')
class StudentCreate(View):
    def post(self,request):
        data=loads(request.body)#converts json data into python native types
        r=data['roll_no']
        n=data['name']
        a=data['age']
        p=data['place']
        m=data['marks']
        s=Student.objects.create(roll_no=r,name=n,age=a,place=p,marks=m)
        s.save()
        return JsonResponse({"message":"inserted data successfully"})
#api view for reading specific record
class StudentDetail(View):
    def post(self,request,i):
        s=list(Student.objects.filter(id=i).values())
        if s:
          return JsonResponse(s,safe=False)
        else:
            return JsonResponse({"message":"no results"})

@method_decorator(csrf_exempt,name="dispatch")
class StudentDelete(View):
    def delete(self,request,i):
        s=Student.objects.get(id=i)
        s.delete()
        return JsonResponse({"message":"deleted successfully"})

import  json
@method_decorator(csrf_exempt,name="dispatch")
class Studentfullupdate(View):
    def put(self,request,i):
        #request.body-data coming from client app
        data=json.loads(request.body)#loads used to translate coming json data into python native/dictionary
        print(data)
        try:
            s=Student.objects.get(id=i)
            s.roll_no=data['roll_no']
            s.name=data['name']
            s.age=data['age']
            s.place=data['place']
            s.marks=data['marks']
            s.save()
            return JsonResponse({"message":"updated successfully"})
        except:
            return JsonResponse({"message":"no student data"})

@method_decorator(csrf_exempt,name="dispatch")
class Studentpartialupdate(View):
    def patch(self,request,i):
        data=json.loads(request.body)
        try:
            s=Student.objects.get(id=i)
            if 'roll_no' in data:
                s.roll_no=data['roll_no']
            if 'name' in data:
                s.name=data['name']
            if 'age' in data:
                s.age=data['age']
            if 'place' in data:
                s.place=data['place']
            if 'marks' in data:
                s.marks=data['marks']
            s.save()

            return JsonResponse({"mesage":"updated partially"})
        except:
            return JsonResponse({"message":"no student data"})
