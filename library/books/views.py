from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views import View

from myapp.models import Books

class Home(View):
    def get(self,request):
        return render(request,'<h1>welcome home</h1>')

class Add_book(View):
    def get(self,request):
        return render(request,'addbook.html')
    def post(self,request):
        data=request.POST
        t=data['t']
        a=data['a']
        p=data['p']
        l=data['l']
        pr=data['pa']
        b=Books.objects.create(title=t,author=a,price=p,lang=l,pages=pr)
        b.save()
class View_book(View):
    def get(self, request):
        books=Books.objects.all()
        context={'books':books}
        return render(request,'viewbooks.html',context)









