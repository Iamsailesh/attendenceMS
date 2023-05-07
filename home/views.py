from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(request):
   # return HttpResponse("this is homepage")
   return   render (request, "ams/dashboard.html")

def profile(request):
   return   render (request, "users/profile.html")
   

def setting(request):
   return   render (request, "users/setting.html")
   




def login(request):
   return HttpResponse("this is classes")


def logout(request):
   return HttpResponse("this is classes")