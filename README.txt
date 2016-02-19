Author: Karolina Blumke 
Application name: Planner

I. Copy the source code

	a. unzip code package: planner.zip

		or

	b. git clone https://akallabeth@bitbucket.org/akallabeth/day-planner.git

II. Environment preparation

	To run Planner you must prepare Virtual environment.

		a. To get Virtualenv:

			* To install globally with pip (if you have pip 1.3 or greater installed globally):

				$ [sudo] pip install virtualenv

			* Or to get the latest unreleased dev version:

				$ [sudo] pip install https://github.com/pypa/virtualenv/tarball/develop

		b. create Virtualenv
			
			virtualenv -p python3.5 ENV

			ENV - name for your virtualenv

		c. activate Virtualenv

			$ source ENV/bin/activate 
			
			and go to the project folder: ../planner/

			

*** Instructions below require activate virtualenv!!! ***		

III. Install requirements:

	Activate virtualenv, go to project folder (../planner/requirements.txt) and run:

		$ pip install -r requirements.txt

IV. Setting up database

	Go to project folder (../planner/manage.py) and run:

		$ python manage.py migrate

V. Setting static files

	Go to project folder (../planner/manage.py) and run:

		$ python manage.py collectstatic

VI. Run server/application:
	
	$ python manage.py runserver

	and go to the link given in the terminal (usually http://127.0.0.1:8000/)

VII. Run automatic tests

	To run tests go to project folder (../planner/manage.py) and run:

		$ python manage.py test


VIII. Issues

If you have any issues with my application, please contact me:

karolina.blumke@gmail.com