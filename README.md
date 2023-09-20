This repo demonstrates how integration tests with pytests and a mysql DB can be set up.

A workflow file handles the testing in github actions.

Additionally, the tests can be run locally as follows


## How to run the tests locally

1. Start the docker-container with the mysql DB

`docker-compose up mock-mysql`

2. Once the DB is up and running (this was taking ~15 seconds on my machine):

`docker-compose up tests`

You can keep re-running the tests as you change the code; no need to restart the DB each time.

## Other useful things

The db is handled by a fixture defined in conftests.py

It creates all the tables before the tests, and then drops them all after the tests have been run. If we wanted to do this per-test or per-module, we can just alter the scope of the fixture (e.g. @pytest.fixture("module"))

Once you've started the DB locally, you can login to the mysql DB via the console to poke around if you want

`docker exec -it [name-of-running-docker-image] mysql -u test -p`

e.g.:

`docker exec -it integration-testing_mock-mysql_1 mysql -u test -p`


