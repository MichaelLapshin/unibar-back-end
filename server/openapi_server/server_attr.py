import os
import dotenv

dotenv.load_dotenv()

# Define global configuration variables
print("===== Server Configuration =====")

start_time = None

deployment_name = os.getenv("UNIBAR_DEPLOYMENT_NAME")
print("Deployment name:", deployment_name)
assert(deployment_name)

is_prod = (os.getenv("UNIBAR_DEPLOYMENT_TYPE") == "prod")

# Configure database
rds_hostname = os.getenv("UNIBAR_RDS_HOSTNAME")
rds_username = os.getenv("UNIBAR_RDS_USERNAME")
rds_password = os.getenv("UNIBAR_RDS_PASSWORD")
rds_port = int(os.getenv("UNIBAR_RDS_PORT"))
rds_database = os.getenv("UNIBAR_RDS_DATABASE")

print("=== RDS Config ===")
print("hostname: ", rds_hostname)
print("username: ", rds_username)
print("password: ", "<redacted>")
print("port: ", rds_port)
print("database: ", rds_database)

assert(rds_hostname)
assert(rds_username)
assert(rds_password)
assert(rds_port)
assert(rds_database)

print("============================")
