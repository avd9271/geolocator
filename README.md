# geolocator
A basic geolocator program developed as a sample problem for interviewing purposes

This program provides a simple web api that takes in an address and spits out the state that the address is from.

The general flow can be seen below:

- user inputs an address through web-api call
- python uses geopy to transform address to latitude and longitude
- lat / lon are compared against geo-data previously loaded into a postgresql instance
- python gets the state from the lat / lon comparison
- python serves the output to the user

The pieces of the project are as follows:

**PYTHON**
The application that hosts the web endpoints is written in python-flask. This piece of the project is responsible for taking user input and returning results.

**POSTGRESQL**
The python application compares against data loaded into a postgis-enabled postgresql instance. This holds geodata on each individual state.

**DOCKER**
The Dockerfile and docker_start.sh files contain instructions on how to wrap up the project into a Docker container for portability.


The whole project in it's entirety can be built using the provided dockerfile.

The dockerfile will install the postgis-enabled postgresql server from scratch. The file containing state data will be uploaded to the postgresql server upon starting the docker container.


# How to run:

have docker installed on your machine.

run the command: 

`docker build -t yourusername/postgresgeolocator .`

since this is building postgresql from scratch, you may have to wait 5-10 min depending on your machine's internet connection.

once you have your container built run the command:

`docker run -p 80:80 --name yourcontainername yourusername/postgresgeolocator`

once the service is up and running, you can use the internal ip of the docker container to access the application.

use the `/find-state-of-lat-lon` endpoint with url parameter `address` to input an address and get a state as a response.

e.g. `my-docker-ip/find-state-of-lat-lon?address="My address"`

---- NOTES ----

PROJECT HICCUPS:

The problem prompt asked for the use of Google's api for finding the latitude and longitude of an address. I stuck with geopy because the google maps api required billing information and I wanted to steer away from that.

Currently both the python application and the postgresql server are running through the same Dockerfile. Ideally this shouldn't be the case. You would ideally want to have these in two different containers and then have them be organized through Docker Compose. I didn't get enough time really to get this set up as I spent too much time doing the postgresql install from scratch.

The geo data is loaded on container run, which could cause issues if the process is shut down and then ran again (re-loading the same data twice at that point). Didn't have much time to double back and investigate.

There are docker images out there of postgis-enabled postgresql server instances. I opted to build one from scratch as this was my first time working with Docker. Many headaches later, I got it to work, but it probably would have been smarter to use one of the pre-existing images.

In a non-interview setting, I would normally have way more test cases. Currently there is no 'tests' folder in my repo. Note that this is generally bad practice, but again there was a bit of a time crunch.

-----------------
