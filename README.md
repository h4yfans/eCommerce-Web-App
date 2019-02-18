# eCommerce


# Installation
Clone the repository and create a virtual environment with **pipenv**

    $ git@github.com:h4yfans/eCommerce-Web-App.git
	$ cd eCommerce-Web-App
	$ pipenv install
	$ pipenv shell
	
If you are not using **pipenv**, type:

    $ pip install -r requirements.txt
    

	
After installed all packages, you have to migrations and create superuser
		

    python manage.py migrate
    python manage.py createsuperuser
    


Run project

    python manage.py runserver

   
