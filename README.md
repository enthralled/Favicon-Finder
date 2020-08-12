# Favicon-Finder

Notes about project:

This project utilizes Django for both the front and backend, and MySQL for data handling.
The DB was populated using a script that can be found in favicon_finder/utils. The resulting data was exported into a json file for viewing (favicon_data.json).

High-Level Overview of Typical Client-Server Interaction:

Users input a query into the search bar (e.g., github.com). On submit, an AJAX call is triggered (handled by Main.js) that sends the query to the backend. A Favicon object is instantiated. If the Favicon object exists in the DB, the corresponding favicon URL is returned. Otherwise, the service attempts to find the Favicon for the URL-of-interest, input it into the DB, and return it. In the case where this is not possible, a notification is displayed to the user.

If 'get fresh' is checked off, the service grabs the Favicon from the relevant site, inputs it into the DB, and returns it, regardless of whether or not it was already present in the DB in the first place (essentially, grabbing a 'fresh' version of the favicon).
