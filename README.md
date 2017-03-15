Can be used in combination with virtual environment, so as to have local libraries (and python versions). 
All the following commands are to be run from the root directory of the project, where this README is situated.
Once virtualenv is installed on your computer, use with command: "source mainSite/bin/activate".
Import models and libraries with "python manage.py makemigrations" and "python manage.py migrate".
Run the server using "python manage.py runserver 127.0.0.1:8000". Note: this tells the server the listen to port 8000 on localhost.
The web page is then accessible from nearly every browser at the address "localhost:8000" or "127.0.0.1:8000".
