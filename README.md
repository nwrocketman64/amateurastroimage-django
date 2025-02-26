# Overview
This is the main codebase for the my Astrophotography website. The code here is made open-source under Apache License 2.0 and you are free to look at the code to either add any suggestments to improve the code or to copy it and use it as the base template for your website. This website includes features such as session and image uploads. The website is designed to run on any Linux server or Windows server.

# Installing
To install the website for running on your computer, you can clone the codebase either by using the GitHub website or through git. Once it is on your computer, to get the website running you must create an .env file and place it in the second astro_site folder next to settings.py
```
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
TIMEZONE=
SECRET_KEY=
DEBUG_SET=
```
Add all the database information, set the timezone, and set Debug to false. Run this code in the Python shell to generate a secret key.
```
from django.core.management.utils import get_random_secret_key  
print(get_random_secret_key())
```

# Configuring the Database and Creating the Super User
First, you'll need to run the migrate command to create the tables in the database.
```
python3 manage.py migrate --run-syncdb
```
Then, run this command to create the super user.
```
python3 manage.py createsuperuser
```
You can run the instance locally using this command.
```
python3 manage.py runserver
```

# Development Environment
I used [VS code](https://code.visualstudio.com/) as the main IDE for creating the source code. I used [MariaDB](https://mariadb.org/) in both the development and production. Microsoft Edge and Mozilla FireFox where the main web browser that I tested this website on.

# Libraries Used
The key libraries used in this project.

* [Python Django](https://www.djangoproject.com/) - The main backend web framework.
* [Django Cleanup](https://pypi.org/project/django-cleanup/) - Used to clean up images with records deleted from database.
* [Django Environ](https://pypi.org/project/django-environ/) - Used to load configurations into the enviroment.
* [Django ImageKit](https://pypi.org/project/django-imagekit/) - Used to create cached thumbnails of the image.
* [Django Simple Captcha](https://pypi.org/project/django-simple-captcha/) - Provided basic ReCaptcha for the contact form.
* [MySQL Client](https://pypi.org/project/mysqlclient/) - Provides a connection to the MariaDB database.
* [Normalize.css](https://necolas.github.io/normalize.css/) - It is used in the Pico.css framework.
* [Pico.css V2](https://picocss.com/) - The lightweight CSS framework that I used for the this website.
* [Pillow](https://pypi.org/project/pillow/) - Is used to add watermarks to the images.
* [PYTZ (Python Timezone)](https://pypi.org/project/pytz/) - Used to fix timezone issues in the code.

# Website Link
This is the link to active website deployed.

[Amateur Astro Image](https://www.amateurastroimage.com/)
