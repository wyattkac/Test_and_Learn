"""Introduction
https://pythonprogramming.net/django-web-development-python-tutorial/
"""

# django-admin startproject mysite  # Create a new site called mysite
# python manage.py startapp main    # Create a new app called main
# python manage.py runserver        # Runs development server

# path("", include('main.urls')), (mysite/urls.py)
# create main/urls.py
    # from . import views
    # app_name = "main"
    # path("", views.homepage, name="homepage"),

# add the following to main/view.py
    # from django.http import HttpResponse
    # def homepage(request):
    #     return HttpResponse("Wow this is an <strong>awesome</strong> tutorial")
