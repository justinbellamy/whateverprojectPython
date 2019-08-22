# Getting Started with Python and Django

Django is a Web Application Framework that was originally released in July of 2005. Since then, it has evolved into a highly-scalable platform for serving up content on some of the highest-traffic websites on the internet, including: Instagram, Reddit and Disqus. 

#### Reasons to use Django
* Great Documentation
* Python
* Full Stack Framework
* Works as a typical database-backed web application

#### What version of Python do I have?
If you don't have python, download it [here](https://www.python.org/downloads/) and install it. Many systems already have Python installed. If you already have Python installed, use the following command to see what version you have:

```
$ python --version
```

Different versions of Django work with specific versions of Python. [See the compatibility chart](https://docs.djangoproject.com/en/dev/faq/install/#what-python-version-can-i-use-with-django).


#### Additional Python Environment Setup
In order to manage our environment and dependencies, we need to:

* Download the [pip](https://bootstrap.pypa.io/get-pip.py) install file `get-pip.py`, or [you can use a package manager to install for Linux distros](https://pip.pypa.io/en/stable/installing.html#using-os-package-managers).
* Install **pip** (as well as **setuptools**) by running the following in the command prompt:
```
$ python get-pip.py
```

* In addition, we should also set up `virtualenv` so that we don't have to install a system-wide version of Django. This allows each development instance to be tailor-made for the version of software being worked on. [See documentation](https://virtualenv.pypa.io/en/latest/userguide.html) for `virtualenv` to find out more.

Declare which directory will be used to store virtual environment settings using the following, and substituting `ENV` with the the name of the directory you want to create:
```
$ virtualenv ENV 
```

We can then begin using this virtual environment by activating it. The installation of Django in the following steps (and any additional packages we install later) will be stored in the `ENV` directory we created:
```
$ source ENV/bin/activate
```

At this point, your prompt will have a () at the front of it indicating that you are in virtual environment mode. If you named your folder something like `venv`, your prompt will have a `(venv)` in front of it.

Any time you want to exit the virtual environment, just type:

```
$ deactivate
```

For the rest of this tutorial, make sure your virtual environment is activated.

In addition to the `virtualenv` tool, [take a look](http://virtualenvwrapper.readthedocs.org/en/latest/) at the `virtualenvwrapper` tool for even more advanced management of virtual environments.

#### Install Django
First, make sure you have your `virtualenv` active. Install Django by running:

```
$ pip install django
```

We can then verify the version of Django installed by running the command:

```
$ python -c "import django; print(django.get_version())"
```
If this results in an error, revisit the steps above.

##### First Django Web Project
Now that we have the environment set up for Django, it's time to create our project.

#### Create new project
Go to the directory where you want to create the new project. Run the following command to create a new directory where the project will live, replacing *whateverproject* with your project's (and new directory) name:

```
$ django-admin startproject whateverproject
```

This creates the following skeleton application:

```
whateverproject/
    manage.py
    whateverproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

* `manage.py` - This is the command runner. You will never edit this. This is the command-line utility for interacting with the new project
* `__init__.py` - An special empty file that let's python know that this directory is really a package and can be imported
* `settings.py` - the settings and configuration of the new project
* `urls.py` - the URL mapper that handles URL dispatching
* `wsgi.py` - used as an entry point for a web server to serve this project. This is Web Server Gateway Interface (WSGI) compatible (Green Unicorn, CherryPy, uWSGI, mod_wsgi) 

#### How to run the development web server

Change to the project directory where `manage.py` is located...
```
$ cd whateverproject
```
... and run the following command:

```
$ python manage.py runserver
```

You may see a few warnings, but we will address those later. Point the URL in a web browser to http://127.0.0.1:8000/ and you should see a working page.

Press `CONTROL-C` on the keyboard to stop the web server.

##### Project vs Application
A Django project is is made up of one or more **Applications**. These applications can be developed and installed inside the Django project, and each one typically handles one type of activity, such as authentication, managing sessions, etc. We are going to create a basic application that handles a web request and returns data from a database.

#### How to create an application
First, make sure you are in the same directory as `manage.py`. We create a blank skeleton application by running the following command, passing a name in for our application. In this example, we're using the name `whateverapp`:
```
$ python manage.py startapp whateverapp
```

This creates the following in the file system:

```
whateverapp/
    __init__.py
    admin.py
    models.py
    tests.py
    views.py
    migrations/
        __init__.py
```

#### Installing the application
In `settings.py`, we let the project know that we want to use the newly created application by adding it to the bottom of the `INSTALL_APPS` entry like this:

```language-python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ...
    'whateverapp',
)
```

#### Handling URL routing
In the project's `urls.py` file, we write a regular expression (regex) that maps a **url** to a **view**. This tells Django to run the view code when a specific URL is called. So why do we use regex?

* Regex is very fast
* Regex is flexible
* Regex is used in abundance across various programming languages

Edit `urls.py` to include:  

```language-python
urlpatterns = [
    url(r'^$', 'whateverapp.views.index', name='index'),
]
```


* **url** is the function call which builds the url patterns
* **r'^$'** is the Python literal string representation for a regex
* **whateverapp.views.index** is the Python import string to get the view
* **name='index'** is the identifier we use for this url pattern

##### Views
A view is code that takes an HTTP Request object and returns an HTTP Response object.

In `whateverapp/views.py` add a `HttpResponse` handler to the `index` view by importing it into the file, then returning it:

```language-python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")
```

Make sure you are in the project's root directory where `manage.py` is located, then run the following command to start the server again:

```
$ python manage.py runserver
```

Point the URL in a web browser to http://127.0.0.1:8000/ and you should see the following on the page:

```
Hello world!
```

Press `CONTROL-C` on the keyboard to stop the web server.

#### Django Models
Database tables are represented in Python code using Models, which use Django's built-in ORM (Object-Relational Mapping). A model class is a database table and a model instance is a database table row. There's [extensive documentation](https://docs.djangoproject.com/en/1.8/topics/db/models/) on this subject matter, but for now lets basically keep in mind that:

* We need to access a data store/RDBMS (via SQLite, MySQL, PostgreSQL, etc.)
* We need to be able to Create/Read/Update/Delete (CRUD) data from the RDBMS

#### Setting Up a Database

When we first ran `runserver` in Part 1, Django created a free SQLite database for development so we will use this for this example. It is located in the project's root folder:

```
whateverproject/
    db.sqlite3
```

In `whateverproject/settings.py`, you can see the default database is already enabled:

```language-python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

#### Creating a Model
In `whateverapp/models.py` we do the following to create two models `City` and `Hotel`. We will have more than one Hotel in each City, so we set City as the `ForeignKey` (a standard *one-to-many* relationship):  

```language-python
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)


class Hotel(models.Model):
    name = models.CharField(max_length=64)
    room_charge = models.DecimalField(max_digits=6, decimal_places=2)
    rooms_available = models.BooleanField(default=False)
    rating = models.CharField(choices=(
        ('1', "1 Star"),
        ('2', "2 Stars"),
        ('3', "3 Stars"),
        ('4', "4 Stars"),
        ('5', "5 Stars")),
        max_length=1
    )
    city = models.ForeignKey("City")
```

* A table created in the database will be the **app name + _ + model** name... so, in this case: `whateverapp_person`
* The attributes become the columns of the table 
* Django will auto-create primary keys if we don't declare them ourselves

#### Database Migrations

We run the following command to create an initial migration

```
$ python manage.py makemigrations
```
Results:
```
Migrations for 'whateverapp':
  0001_initial.py:
    - Create model City
    - Create model Hotel
```

We then run the following command to scan through the Model objects in the project and create the database(s) for us:
```
$ python manage.py migrate
```

You should see something like this:
```
Operations to perform:
  Synchronize unmigrated apps: staticfiles, messages
  Apply all migrations: admin, whateverapp, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK
  Applying whateverapp.0001_initial... OK
```

#### Populating the Database using Fixtures

Now that we have the schema set up, we're going to populate the data model with some initial values using fixtures. Django takes [different formats](https://docs.djangoproject.com/en/1.8/howto/initial-data/), including XML, YAML and JSON.

Create the file `initial_data.json` in the `whateverapp` folder with the following JSON data in it: 

```language-javascript
[
	{
		"model": "whateverapp.city",
		"pk": 1,
		"fields": {
			"name" : "New York City"
		}
	},
	{
		"model": "whateverapp.city",
		"pk": 2,
		"fields": {
			"name" : "Los Angeles"
		}
	},
	{
	"model": "whateverapp.hotel",
		"pk": 1,
		"fields": {
			"name" : "Atlantic Hotel",
			"room_charge" : "199.95",
			"rooms_available" : "True",
			"rating" : "4",
			"city_id" : "1"
		}
	},
	{
	"model": "whateverapp.hotel",
		"pk": 2,
		"fields": {
			"name" : "Downtown Hotel",
			"room_charge" : "245.99",
			"rooms_available" : "False",
			"rating" : "5",
			"city_id" : "1"
		}
	},
	{
	"model": "whateverapp.hotel",
		"pk": 3,
		"fields": {
			"name" : "Pacific Hotel",
			"room_charge" : "101.00",
			"rooms_available" : "True",
			"rating" : "3",
			"city_id" : "2"
		}
	}
]
```

Import the data using the following command:

```
$ python manage.py loaddata whateverapp/initial_data.json
```

#### Django Views

We need to alter the `whateverapp/views.py` file in order to retrieve data from the database, and then have it available for the template to render the data (in this case, an HTML formatted page). You can see the previous `index` view function we created in Part 1. In this example, we are creating a `hotels` function to handle the request for cities and hotels.

```language-python
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import City
from .models import Hotel


def index(request):  
    return HttpResponse("Hello world!")


def hotels(request):
    cities_list = City.objects.order_by('name')
    hotels_list = Hotel.objects.order_by('name')
    template = loader.get_template('whateverapp/hotels.html')
    context = RequestContext(request, {
        'cities_list': cities_list,
        'hotels_list': hotels_list
    })
    return HttpResponse(template.render(context))
```

#### Templates
Templates are basically combinations of HTML and logic to output pages with data embedded in them. 

Let's create a directory to store a template for our *whateverapp* via:  
```
$ mkdir -p whateverapp/templates/whateverapp 
$ touch whateverapp/templates/whateverapp/hotels.html
```

In `hotels.html`, we're gonna retrieve the hotels in each city and list them:

```language-html
<html>
  <head>
    <title>Hotel Listing</title>
  </head>
  <body>
    <h1>All Hotels</h1>

    {% if cities_list %}
        <ul>
            {% for city in cities_list %}
                <li>{{ city.name }}
                    <ul><li>{{  city.hotel_set.all.count }} Hotels:</li>
                        <ul>
                         {% for hotel in city.hotel_set.all %}
                             <li>{{ hotel.name }}</li>
                             <ul>
                             <li>Rating: {{ hotel.rating }}</li>
                             <li>Room Charge: ${{ hotel.room_charge }}</li>
                             <li>Rooms Available? {{ hotel.rooms_available }}</li>
                             </ul>
                          {%  endfor %}
                        </ul>
                    </ul>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No cities are available.</p>
    {% endif %}

  </body>
</html>
```

Now if we re-launch the page in our browser and go to the `/hotels` page, we should see a nested list of Cities with their Hotels listed in HTML.

To launch the web server again, run the command:
```
$ python manage.py runserver
```

Point the URL in the web browser to http://127.0.0.1:8000/hotels and you should see an updated page with hotel information on it.

Now we have Django accessing and rendering data from a database in HTML.

#### Unit Testing Django Models
In order to create tests for `whateverapp`, we populate the `whateverapp/tests.py` with the tests we would like to run.

The this example, I'm using the library [factory_boy](https://pypi.python.org/pypi/factory_boy/) to create factory objects to use in our unit tests instead of fixtures, which are difficult to maintain over time. In this example, you can see how easy it is to handle complex structures, such as models, which are linked by foreign keys.

**./whateverproject/whateverapp/tests.py**

```language-python
from django.test import TestCase
from whateverapp.models import *
import factory


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = City

    name = "New York City"


class HotelFactory(factory.DjangoModelFactory):
    class Meta:
        model = Hotel

    name = "Omni",
    room_charge = 489.00
    rooms_available = True,
    rating = "5 Star"
    city = factory.SubFactory(CityFactory)


class HotelTestCase(TestCase):

    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_get_rating(self):
        city = CityFactory.create()
        hotel = HotelFactory.create()
        self.assertEqual(hotel.rating, "5 Star")
        self.assertEqual(hotel.city.name, city.name)
```

**Running the test:**
```
$ ./manage.py test whateverapp
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK

```
There are two tests in this example: 

* One is the extremely simple test `test_basic_addition` which demonstrates a test case that will pass.
* The second is `test_get_rating`, which is also really simple but demonstrates how we use factories to set up our testable objects. Notice how `factory.SubFactory(CityFactory)` is used to handle our foreign key relationship as well without the need for dealing with fixtures.