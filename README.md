# Django and Shield UI Integration Tutorial

## Setup the Django application

 * Create virtual environment
```
$ mkdir ShieldUIApp && cd ShieldUIApp
$ virtualenv env
```
 * Install Django and the Django REST Framework
```
$ ./env/bin/pip install django
$ ./env/bin/pip install djangorestframework
```
 * Clone the project []()
```
$ git clone https://github.com/shieldui/django-shieldui-integration
```
 * Setup the database
```
$ ./env/bin/python manage.py makemigrations
$ ./env/bin/python manage.py migrate
```
	* Seed the database
```
$ ./env/bin/python manage.py loaddata seed.json
```
  * Run the server
```
$ ./env/bin/python manage.py runserver
```

Visit http://localhost:8000/books/ to test that the [Shield UI jQuery Grid Component](https://www.shieldui.com/products/grid) integration works properly.

## License Information

The Shield UI Lite library is licensed under the MIT license, details of which can be found in the [LICENSE.txt](LICENSE.txt) file located in this folder.
The license applies ONLY to the source code of this repository and does not extend to any other Shield UI distribution or variant, or a third-party library used. 

For more details about Shield UI licensing, see the [Shield UI License Agreement](https://www.shieldui.com/eula) page at [www.shieldui.com](https://www.shieldui.com).
Shield UI Commercial support information can be found on [this page](https://www.shieldui.com/support.options)
