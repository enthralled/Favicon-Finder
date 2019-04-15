# Favicon-Finder

Notes about project:

This project utilizes Django for both the front and backend, and MySQL for data handling.
The DB was populated using a script that can be found in favicon_finder/utils. The resulting data was exported into a json file for viewing (favicon_data.json).

Instructions to deploy on your local machine:
1. Clone the repo into a directory of your choosing.
2. cd into the new directory (by default, 'Favicon-Finder).
3. run 'python manage.py runserver' from the command line.
4. go to localhost:8000 in your browser (Note that I used Chrome throughout the development process) and you should be good to go.
