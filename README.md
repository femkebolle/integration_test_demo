
# Running the tests locally

1. Start the docker-container with the mysql DB

`docker-compose up mock-mysql`

2. Once the DB is up and running

`docker-compose up local-tests`

3. optionally, login to the mysql DB via the console to poke around

`docker exec -it [name-of-running-docker-image] mysql -u test -p`

e.g.:
`docker exec -it integration-testing_mock-mysql_1 mysql -u test -p`


