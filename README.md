[![Build Status](https://travis-ci.org/kdenno/iReporterREST.svg?branch=endpoints)](https://travis-ci.org/kdenno/iReporterREST)
# iReporterREST #

REST API for iReporter App. 

## Features ##
* Create  red-flag.
* Get  red-flag by id.
* Get all red-flags.
* Update red-flag by id
* Delete red-flag by id.

## Language and Tools Used ##
* Python 3.7
* Postman
* VSCode (IDE)

## Installation ##
Clone the project to your local machine from https://github.com/kdenno/iReporterREST.git

#### Set Up the Virtual Environment ###
In your terminal,
* Run pip install virtualenv to install virtualenv
* Run virtualenv env to create a virtual environment named env
* env/scripts/activate.bat to activate your virtual environment.

## Requirements ##
Chekout the requirements.txt file in the root folder of the project for the full list of the requirements to install.

## Running the Application ##
In your terminal, navigate to the root folder and run the python run.py command to start the server

#### Test out the Endpoints with postman ####

| Params        | Type          | Description                               |
| ------------- |:-------------:| ---------------------------------------:  |
| endpoint      | string        | iReporter API endpoint example: allflags  |
| id            | integer       | For GET and DELETE, request query string  |
| data          | json          | POST and PUT, data to be sent in JSON     |


| Method        | endpoint                     | output                                                  |
| ------------- |:----------------------------:| -------------------------------------------------------:|
| POST          | /api/v1/red-flags            | Returns a message on success with status code           |
| GET           | /api/v1/red-flags            | Returns a list of red flags on success with status code |
| PATCH         | /api/v1/red-flag/id/location | Returns message on success with status code             |
| DELETE        | /api/v1/red-flag/id          | Returns message on success with status code             |

# Versioning #
Version 1.0.0

 