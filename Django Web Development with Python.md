
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

copy `mysite/urls.py` to `main/urls.py`

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
go to `main/models.py`  
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
We're using a CSS framework called [Materialize](https://materializecss.com/) so we have to do less design work  
This webpage has code for most of the things we'll want to do  

go to `main/templates/main/home.html`  
to begin using Materialize add:  

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

We'll want to use `extends` and `include` in our template for things like navbars (so when we change it we only have to change it one place)  
create `main/templates/main/header.html`  
put the header/footer/import statements in, and put the following where you want unique content to go (go to [here](https://pythonprogramming.net/css-django-tutorial/) to see the full code):  

    {% block content %}
    {% endblock %}

go to `main/templates/main/home.html`  
rewrite to say:  

    {% extends 'main/header.html' %}

    {% block content %}
    unique_content
    {% endblock %}

To personalize the color's, we'll need to download [Sass from Materialize](https://materializecss.com/getting-started.html), and a compiler like [Koala Sass](http://koala-app.com/)  
go to `materialize-src-v1.0.0/materialize-src/sass/components/_color-variables.scss`  
modifiy the colors to be whatever you like (they are in hex)  
compile in Koala  
put the created `materialize.css` into `main/static/main/css`  
go to `main/templates/main/header.html`  
replace `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">` with `<link rel="stylesheet" href="{% static "main/css/materialize.css" %}">`  


## [Video 6: User Registration](https://pythonprogramming.net/user-registration-django-tutorial/)
We'll use the built in user model since it's good enough for most use cases.

> python3 manage.py shell  
>> from django.contrib.auth.models import User  
>> dir(User)  

create main/templates/main/register.html  
add:  

    {% extends 'main/header.html' %}

    {% block content %}

      <form method="POST">
        {% csrf_token %}
        {{form.as_p}}
      </form>

      If you already have an account <a href="/login" target="blank"><strong>login</strong></a> instead.

    {% endblock %}

go to `main/views.py`  
add:  

    from django.contrib.auth.forms import UserCreationForm

    def register(request):
      form = UserCreationForm
      return render(request = request,
                    template_name = "main/register.html",
                    context={"form":form})

go to `main/urls.py`  
under `urlpatterns` add `path("register/", views.register, name="register"),`

It look weird when it goes all the way to the edge, to fix:  
go to `main/templates/main/header.html`  
And wrap the block content in a container like so:

    <div class="container">
      <br>
      {% block content %}
      {% endblock %}
    </div>

There's no way to submit the form, so insert a button  
go to `main/templates/main/register.html`  
And inside the form add `<button style="background-color:#F4EB16; color:blue" class="btn btn-outline-info" type="submit">Sign Up</button>`

Now to make it so the button does somthing  
go to `views.py`  
under `def register(request):` add:  

    from django.shortcuts import redirect
    from django.contrib.auth import logout, authenticate, login

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})


## [Video 7: Messages](https://pythonprogramming.net/messages-django-tutorial/)
go to `main/views.py`  
add `from django.contrib import messages`  
under `def register(request)` under `form.is_valid()` add `messages.success(request, f"New Account Created: {username}")`  
under `def register(request)` under `form.is_valid()` add `messages.info(request, f"You are now logged in as {username}")`  
under `def register(request)` under `for msg in form.error_messages` replace `print(form.error_messages[msg])` with `messages.error(request, f"{msg}: {form.error_messages[msg]}")`  

we probably want to handle messages sitewide, handle them under header  
go to `main/templates/main/header.html`  
above the container, add:  

    {% if messages %}
        {% for message in messages %}
            {% if message.tags == 'success'%}
                <script>M.toast({html: "{{message}}", classes: 'green rounded', displayLength:2000});</script>
            {% elif message.tags == 'info'%}
                <script>M.toast({html: "{{message}}", classes: 'blue rounded', displayLength:2000});</script>
            {% elif message.tags == 'warning'%}
                <script>M.toast({html: "{{message}}", classes: 'orange rounded', displayLength:10000});</script>
            {% elif message.tags == 'error'%}
                <script>M.toast({html: "{{message}}", classes: 'red rounded', displayLength:10000});</script>
            {% endif %}
        {% endfor %}
    {% endif %}

now add if statements to the navbar (go to [here](https://pythonprogramming.net/messages-django-tutorial/) to see the full code) to show login/logout depending on state

