# UniBar Back-End

## Standards
- UTC time is assumed to be the time format.

## Logging into AWS EC2
Use the AWS console to access the EC2 instance an open a terminal session to it.

## Running the server
1. Install the requirements: `sudo pip3 install --no-cache-dir -r server/requirements.txt`
2. Configure the following environment variables:
```
UNIBAR_DEPLOYMENT_NAME = <deployment_name>
UNIBAR_RDS_HOSTNAME = <rds_server_hostname>
UNIBAR_RDS_USERNAME = <rds_server_username>
UNIBAR_RDS_PASSWORD = <rds_server_password>
UNIBAR_RDS_PORT = <rds_server_port>
UNIBAR_RDS_DATABASE = <rds_server_database>
```
3. Start the server: `sudo -E python3 -m openapi_server` from the server directory
 - `sudo -E` runs the server as admin while keeping environment variables.

## Creating a database and tables
1. Fetch the UniBar back-end repository.
2. Connect to the MySQL server (see steps below)
3. Run the following SQL script: `database_scripts/create_database.sql`

## Deleting the database and tables
1. Fetch the UniBar back-end repository.
2. Connect to the MySQL server (see steps below)
3. Run the following SQL script: `database_scripts/delete_database.sql`

## Adding a new admin
1. Fetch the UniBar back-end repository.
2. Run the following bash script:
`./database_scripts/insert_new_admin <user> <password> <host> <admin_name>`
3. Record your admin's generated ID and token.

## Accessing GitHub from EC2
```
eval $(ssh-agent -s)
ssh-add ~/.ssh/github_rsa
git pull
```

## Generating Documentation and Flask server from openapi specs
https://github.com/OpenAPITools/openapi-generator/tree/master

Flask server: `openapi-generator generate -g python-flask -i index.yaml -o server/`
Documentation: `openapi-generator generate -i "server/openapi_server/openapi/openapi.yaml" -g markdown -o docs/`

### Installing and Connecting to MySQL
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html

```
sudo dnf update -y
sudo dnf install mariadb105-server
mysql -u<user> -p<password> -h<db_endpoint> -P<port,default:3306>
```