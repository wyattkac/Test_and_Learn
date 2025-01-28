
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
add:  

    def homepage(request):
        return HttpResponse("Wow this is an <strong>awesome</strong> tutorial")


## [Video 2: Models](https://pythonprogramming.net/models-django-tutorial/)
Most of the value of Djano comes from the abstraction provided by models.

go to `main/models.py`  
add:

    class Tutorial(models.Model):
      tutorial_title = models.CharField(max_length=200)
      tutorial_content = models.TextField()
      tutorial_published = models.DateTimeField("date published")

    def __str__(self):
      return self.tutorial_title

Must install new apps before you can add models  
go to `mysite/settings.py`  
under `INSTALLED_APPS` add `'main.apps.MainConfig',`  


Every time you add/change a model you must migrate
> python3 manage.py makemigrations  
> python3 manage.py migrate  

To get a shell to manage the website (useful for troubleshooting)  
Example of using shell to insert data (NOT RECOMMENDED)  
> python3 manage.py shell  
>> from main.models import Tutorial  
>> from django.utils import timezone  
>> new_tutorial = Tutorial(tutorial_title="To be", tutorial_content="...or not to be", tutorial_published=timezone.now())  
>> new_tutorial.save()  
>> Tutorial.objects.all()


## [Video 3: Admin and Apps](https://pythonprogramming.net/admin-apps-django-tutorial/)
