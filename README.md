# Favicon-Finder

Notes about project:

This project utilizes Django for both the front and backend, and MySQL for data handling.
The DB was populated using a script that can be found in favicon_finder/utils. The resulting data was exported into a json file for viewing (favicon_data.json).

High-Level Overview of Typical Client-Server Interaction:

Users input a query into the search bar. On submit, an AJAX call is triggered (handled by Main.js) that sends the query to the backend. A Favicon object is instantiated. If the search term exists in the DB, the corresponding favicon URL is returned. Otherwise, the service attempts to find the Favicon for the URL-of-interest, input it into the DB, and return it. In the case where this is not possible, a notification is displayed to the user.

Instructions to deploy on your local machine:
1. Clone the repo into a directory of your choosing.
2. cd into the new directory (by default, 'Favicon-Finder').
3. To setup the DB (MySQL), create a database called Favicon in MySQL (note that it doesn't necessarily need to be given that name; this is just going off of the DB settings already present in the settings.py file). Similarly, update the username and password in the settings.py file for your local copy of MySQL.
4. set up the requisite tables, run migrations (python manage.py migrate).
5. run 'python manage.py runserver' from the command line.
6. go to localhost:8000 in your browser (note that I used Chrome throughout the development process) and you should be good to go.
