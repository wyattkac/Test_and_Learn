
# Django Web Development with Python
A Tutorial from [pythonprogramming.net](pythonprogramming.net), or [sentdex on YouTube](https://www.youtube.com/@sentdex)


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
Start by creating a superuser  
> python3 manage.py createsuperuser  

Navigate to `http://127.0.0.1:8000/admin`  
Here you can add groups and users, and modify your website  

To modifiy the website you first have to register your models  
go to `main/admin.py`  
add `from .models import Tutorial`  
add `admin.site.register(Tutorial)`  
If you wanted to only see certain fields, or change how fields are displayed, add:  

    class TutorialAdmin(admin.ModelAdmin):
      fields = ["tutorial_title",
                "tutorial_content",
                "tutorial_published",]
    admin.site.register(Tutorial, TutorialAdmin)

or, if you want to change how things are presented, add:  

    class TutorialAdmin(admin.ModelAdmin):
      fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
      ]
    admin.site.register(Tutorial, TutorialAdmin)

To add a default to a model's field (in this case making tutorial_published=now):  
Go to `main/models.py`  
add `from django.utils import timezone`  
change `tutorial_published = models.DateTimeField("date published")` to `tutorial_published = models.DateTimeField("date published", default=timezone.now)`  
And since you changed the models file, migrate

It's a pain to edit out of a text box, so let's install an editor  
HE USES TINYMCE4-LITE, WHICH IS NO LONGER SUPPORTED  
[Here is the django-tinymce page](https://pypi.org/project/django-tinymce/) and [here is a tutorial](https://www.geeksforgeeks.org/integrating-tinymce-with-django/)
> pip install django-tinymce

go to `mysite/settings.py`  
under `INSTALLED_APPS` add `'tinymce',`  
add:

    TINYMCE_DEFAULT_CONFIG = {
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 20,
        'selector': 'textarea',
        'theme': 'silver',
        'plugins': '''
                textcolor save link image media preview codesample contextmenu
                table code lists fullscreen  insertdatetime  nonbreaking
                contextmenu directionality searchreplace wordcount visualblocks
                visualchars code fullscreen autolink lists  charmap print  hr
                anchor pagebreak
                ''',
        'toolbar1': '''
                fullscreen preview bold italic underline | fontselect,
                fontsizeselect  | forecolor backcolor | alignleft alignright |
                aligncenter alignjustify | indent outdent | bullist numlist table |
               | link image media | codesample |
                ''',
        'toolbar2': '''
                visualblocks visualchars |
                charmap hr pagebreak nonbreaking anchor |  code |
                ''',
        'contextmenu': 'formats | link image',
        'menubar': True,
        'statusbar': True,
    }

go to `mysite/urls.py`
under `urlpatterns` add `path('tinymce/', include('tinymce.urls')),`

go to `main/admin.py`  
add `from django.db import models`  
add `from tinymce.widgets import TinyMCE`  
under `Class TutorialAdmin(admin.ModelAdmin):` add:  

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }



## [Video 4: Views and Templates](https://pythonprogramming.net/views-templates-django-tutorial/)
This is how most pages are served

go to `main/views.py`  
add:

    from .models import Tutorial

    def homepage(request):
      return render(request=request, 
                    template_name="main/home.html",
                    context={"tutorials": Tutorial.objects.all})

create `main/templates/main/home.html`  
NOTE: to refrence variable `{{ variable }}`  
NOTE: to do logic `{%  %}`  
NOTE: He pulled in CSS and Javascript with TINYMCE4
NOTE: Need to know html to style things
add:

    <body>
      {% for tut in tutorials %}
        <p>{{tut.tutorial_title}}</p>
        <p>{{tut.tutorial_published}}</p>
        <p>{{tut.tutorial_content|safe}}</p>
        <br><br>
      {% endfor %}
    </body>


## [Video 5: CSS](https://pythonprogramming.net/css-django-tutorial/)
