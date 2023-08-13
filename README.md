# Cegeka-Task

## Requirements:
Please write a Python Flask application that presents your CV data:
- As a JSON REST API with endpoints GET /personal, GET /experience, GET /education, ...
- As a Flask CLI command that prints the data to the console

The CV data can be hard-coded in the code or read from disk. You do not need to integrate with any database. Please include a README file on how to start the REST API and how to execute the CLI command.

## Starting the app
While not necessary, it is highly recommended to create and use a virtual environment:
```sh
python -m venv .venv
```
Activation is different based on operating system.

Flask must be installed first:
```sh
pip install -r requirements.txt
```
In order to run the flask app locally, run the following command:
```sh
flask --app resume run
```

In order to use the CLI command, run the following command:
```sh
flask --app resume get_resume
```

## Endpoints documentation
1. `GET` `/personal` --> returns the personal section of the resume, in json format.
2. `GET` `/experience` --> returns the experience section of the resume, in json format.
3. `GET` `/education` --> returns the education section of the resume, in json format.
4. `GET` `/extra` --> returns the extra section of the resume, in json format.
5. `GET` `/all` --> returns the all section of the resume, in json format.

All endpoints require the ```?resume=<file_name>``` argument. It currently defaults to the only resume available, but if you are to provide it with a different name it would return a 404 Response with an error message.

## CLI command documentation
The CLI command supports 2 options:

1. `--section`  --> The section to retrieve. Possible options are : `personal`, `experience`, `education`, `extra`, `all`. If not provided, defaults to `all`. If an invalid section is requested, the command will return a `400 Response `with an error message.
2.  `--resume` --> The file name of the resume to retrieve. It currently defaults to the only resume available, but if you are to provide it with a different name it would return a `404 Response` with an error message.

Usage examples:
- `flask --app resume get_resume` --> returns the entire resume with status code 200.
- `flask --app resume get_resume --section personal` --> returns only the personal section with status 200.
- `flask --app resume get_resume -- resume <file_name>` --> will return the entire resume called `file_name`. Currently this does not exist so it will return a `404 Response`.
- `flask --app resume get_resume --section invalid_section` --> this will return a `400 Response`.

## Limitations
The application uses a hard coded resume in a somewhat weird format parsed with regular expressions. In a real life situation we will assume that the parsed resume data is stored in a database and we only have to retrieve and return it.

Due to time constraints unit tests have not been implemented, but the functions were written with separation of concerns in mind so they should be unit testable.
