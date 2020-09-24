# Steps of Create Django_CRUD

-----(To start a project)------#

## in the terminal

- 1 - mkdir 'some folder name'
- 2 - cd 'some folder name '
- 3 - poetry init -n
- 4 - poetry add django
- 5 - poetry add --dev black
- 6 - poetry shell
- 7 - django-admin startproject 'project_name_project' .  (don't forget the dot)
- 8 - python manage.py startapp 'project_name'
- 9 - mkdir templates (folder for HTML files)
- 10 - mkdir static (folder for CSS files)
- 11 - touch templates/base.html templates/home.html templates/details.html templates/create.html templates/update.html templates/delete.html (HTML files)

**********************************

## To run on localhost

----(To run on localhost)------#

### in  terminal

- 1 - python manage.py runserver

**********************************

## setup files inside the project

### project/settings.py

---(setup files inside the project)---#

- 1 -    import os
- 2 -  INSTALLED_APPS=[  'app_name.apps.App_nameConfig']
- 3 -  TEMPLATES=['DIRS':[os.path.join(BASE_DIR,'templates')]
- 4 - STATICFILES_DIRS  = [os.path.join(BASE_DIR,'static')]

**********************************

### project/urls.py

-- project/urls.py

- 1 - import django.urls import path,include
- 2 - urlpatterns=[
  path('name_app/',include("name_app.urls")),
]

**********************************

### create a urls.py

-->in app_name folder create a urls.py file

**********************************

### app_name/urls.py

-- app_name/urls.py

from django.urls import path
from .views import HomeView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns =[
        path('home',HomeView.as_view(),name='home'),
        path('post/<int:pk>',BlogDetailView.as_view(),name='Blog_details'),
        path('post/new',BlogCreateView.as_view(),name='create_view'),
        path('post/<int:pk>/update',BlogUpdateView.as_view(),name='update_view'),
        path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='delete_view')
]

**********************************

### app_name/views.py

-- app_name/views.py

from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

class HomeView(ListView):
    template_name='home.html'
    model = Post

class BlogDetailView(DetailView):
    template_name = 'details.html'
    model = Post

class  BlogCreateView(CreateView):
    template_name = 'create.html'
    model = Post
    fields = ['title','author','body']

class BlogUpdateView(UpdateView):
    template_name = 'update.html'
    model = Post
    fields = ['title','author','body']

class BlogDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('home')

**********************************

### app_name/models.py

-- app_name/models.py

from django.urls import reverse
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    body = models.TextField(blank=True)

    def __str__(self): 
        return self.title 
    
    def get_absolute_url(self):
        return reverse('home')

**********************************

### app_name/admin.py

-- app_name/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)

**********************************

### in a terminal

--> in the terminal
    python manage.py makemigration
    python manage.py migrate

    python manage.py createsuperuser 
     //give a username/email/password 
     
    to access the admin page run the server 
    python manage.py runserver
    in the url adress --> 127.0.0.1:8000/admin 
    log in using ur username and password 
    you can fill data to your new created table (the one we named post)

**********************************

### templates/base.html

-- templates/base.html

    ```
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>
            {% block title%}
            {% endblock title%}
        </title>
    </head>

    <body>
        <header>
            {% block header %}
            {% endblock header %}
        </header>

        <main>
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'create_view' %}">Create</a>

            {% block main %}
            {% endblock main %}
        </main>

        <footer>
            {% block footer %}
            {% endblock footer %}
        </footer>

    </body>

    </html>
    ```
**********************************

### templates/home.html

-- templates/home.html

    `
        {% extends 'base.html' %}
        {% block title %}
            Home page
        {% endblock title %}
        {% block header %}
            <h1> Home Page </h1>
        {% endblock header %}

        {% block main %}
        <ul>
            {% for post in object_list%}
            <li>
                <a href="{%url 'Blog_details' post.pk %}">{{post.title}}</a>

            </li>
            {% endfor %}
        </ul>
        {% endblock main %}

        {% block footer %}

        Django @ 2020

        {% endblock footer %}
    `

**********************************

### templates/details.html

-- templates/details.html

    ```
        {% extends 'base.html'%}
        {% block title %}
        details
        {% endblock title %}
        {% block main %}
        <h2>Details</h2>
        <h4>{{ post.title }}</h4>
        <h4>{{ post.author }}</h4>
        <h4>{{ post.body }}</h4>

        <a href="{% url 'update_view' post.pk %}">Update</a>
        <a href="{% url 'delete_view' post.pk %}">Delete</a>

        {% endblock main %}
    ```

**********************************

### templates/update.html

-- templates/update.html

    ```
        <h2>Update</h2>

        <form action="" method="POST">
            {% csrf_token %}
            {{form.as_p}}

            <input type='submit' value='UPDATE'>
        </form>
    ```
**********************************

### templates/delete.html

-- templates/delete.html

    ```
    <h2>Delete Post</h2>

    <form action="" method="POST">
        {% csrf_token %}

        <p>Are you sure you want to delete {{ post.title }}?</p>
        <input type="submit" value="OK">
        <button><a href="{% url 'Blog_details' post.pk %}">Cancel</a></button>
    </form>
    ```
**********************************

### project_name/tests.py

-- project_name/tests.py
    since we have models now we cant used the SimpleTestCase
    its TestCase now

    ```
    from django.test import TestCase
    from django.urls import reverse
    # Create your tests here.
    class PostTests(TestCase):
        def test_home_page_status_code(self):
          expected = 200
          url = reverse('home')
          response = self.client.get(url)
          actual = response.status_code 
          self.assertEquals(expected,actual)
        def test_home_page_template(self):
          url = reverse('home')
          response = self.client.get(url)
          actual = 'home.html'
          self.assertTemplateUsed(response, actual)
    ```

**********************************

### in a-terminal

--> in the terminal
python manage.py test
