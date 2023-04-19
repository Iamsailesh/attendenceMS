from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
   # return HttpResponse("this is homepage")
   return   render (request, "index.html")

def profile(request):
   return   render (request, "profile.html")
   

def setting(request):
   return   render (request, "setting.html")
   

def classes(request):
   return   render (request, "classes.html")


def logout(request):
   return HttpResponse("this is classes")