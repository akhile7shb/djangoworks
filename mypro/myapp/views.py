from multiprocessing import context

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# def home(request):
#     return HttpResponse("first page")
# def index(request):
#     return HttpResponse("second page")

from django.views import View
# class First(View):
#     def get(self,request):
#         return  HttpResponse("""
#         <h1>first page</h1>
#         <h1>hello</h1>
#         """)
# class Second(View):
#     def get(self,request):
#         return  HttpResponse("<h1>second page</h1>")
from myapp.models import Person
class First(View):
    def get(self,request):
        # data=[{"name":"amal","age":21,"place":"ekm"},
        #       {"name": "amal", "age": 21, "place": "ekm"},
        #       {"name": "amal", "age": 21, "place": "ekm"}]
        data=Person.objects.all()
        context={'data':data}
        return render(request,'first.html',context)

class Second(View):
    def get(self,request):
        data = [{"name": "arun", "age": 23, "place": "tvm"},
        {"name": "arun", "age": 23, "place": "tvm"},
        {"name": "arun", "age": 23, "place": "tvm"}]
        context = {'data': data}
        return render(request,'second.html',context)
from myapp.models import Movie
class Movie_list(View):
    def get(self,request):
        m = Movie.objects.all()
        print(m)
        context = {'movies': m}
        return render(request, 'movie list.html',context)

class Add_movie(View):
    def get(self,request):
        return render(request,'add movie.html')

    def post(self, request):
        print(request.POST)
        data=request.POST
        n=data['n']
        d=data['d']
        y=data['y']
        print(n,d,y)
        m=Movie.objects.create(name=n,director=d,year=y)
        m.save()
        return render(request,'add movie.html')


