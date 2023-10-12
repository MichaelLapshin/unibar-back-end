# UniBar Back-End

## Creating a database and tables
1. Fetch the UniBar back-end repository.
2. Connect to the MySQL server (see steps below)
3. Run the following SQL script: `database/create_database.sql`

## Deleting the database and tables
1. Fetch the UniBar back-end repository.
2. Connect to the MySQL server (see steps below)
3. Run the following SQL script: `database/delete_database.sql`

## Accessing GitHub from EC2
```
eval $(ssh-agent -s)
ssh-add ~/.ssh/github_rsa
git pull
```

## Generating Flask server from OpenApi documentation
https://github.com/OpenAPITools/openapi-generator/tree/master

`openapi-generator generate -g python-flask -i index.yaml -o <output_dir>`

### Installing and Connecting to MySQL
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html


```
sudo dnf update -y
sudo dnf install mariadb105-server
mysql -u<user> -p<password> -h<db_endpoint> -P<port,default:3306>
```