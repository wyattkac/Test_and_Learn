
# Django Web Development with Python

## [Video 1: Introduction](https://pythonprogramming.net/django-web-development-python-tutorial/)

[This is the Django homepage.](https://www.djangoproject.com/) Check it out for documentation. They also have a good tutorial.  
Django is a high inital investment, but allows for a modular project that is easy to modify.  

Begin by installing django  
> pip install django  

Now create the website  
> django-admin startproject *mysite*  

Create a new app
> cd mysite  
  python3 manage.py startapp *main*  

And start the server  
> python3 manage.py runserver  

Copy `mysite/urls.py` to `main/urls.py`

go to `mysite/urls.py`  
add `from django.urls import include`  
add `path('', include('main.urls')),`  

go to `main/urls.py`  
remove `from django.contrib import admin`  
remove `path('admin/', admin.site.urls),`  
add `path("", views.homepage, name="homepage"),`  
add `from . import views`  
add `app_name = "main"` (this will be useful for automatically creating URLs)  

go to `main/views.py`  
add `from django.http import render`  
add `from django.http import HttpResponse`  

add  

    def homepage(request):
        return HttpResponse("Wow this is an <strong>awesome</strong> tutorial")


## [Video 2: Models](https://pythonprogramming.net/models-django-tutorial/)
