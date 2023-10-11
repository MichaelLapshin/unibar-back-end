# UniBar Back-End

## Accessing GitHub from EC2
```
eval $(ssh-agent -s)
ssh-add ~/.ssh/github_rsa
git pull
```

## Generating Flask server from OpenApi documentation
https://github.com/OpenAPITools/openapi-generator/tree/master

## Connecting to the DB from EC2
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html

### Installing the mysql cli
```
sudo dnf update -y
sudo dnf install mariadb105-server
mysql -u<user> -p<password> -h<db_endpoint> -P<port,default:3306>
```