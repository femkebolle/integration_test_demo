This repo demonstrates how integration tests with pytests and a mysql DB can be set up.

A workflow file handles the testing in github actions.

Additionally, the tests can be run locally as follows


## How to run the tests locally

1. `docker-compose up tests`

This starts the mysql container automatically, waits for it to be available using the wait-for-it.sh shell script,
then runs the tests.

On subsequent runs, the mysql container will already be running so the tests will be quicker.

2. Once you're done testing, you can close down the mysql container:

`docker-compose down`

## Other useful things

1. The Database connection is handled by a fixture defined in conftests.py

It creates all the tables before the tests, and then drops them all after the tests have been run. If we wanted to do 
this per-test or per-module, we can just alter the scope of the fixture (e.g. @pytest.fixture("module"))

2. You can just start the mysql container on its own with:

`docker-compose up mock-mysql`

This can be handy if any issues with the wait-for-it.sh script arise.

3. Once you've started the DB container, you can log in to the mysql DB via the console to poke around if you want

`docker exec -it [name-of-running-docker-image] mysql -u test -p`

e.g.:

`docker exec -it integration-testing_mock-mysql_1 mysql -u test -p`

(You can find the name of the running mysql container with `docker ps`)
