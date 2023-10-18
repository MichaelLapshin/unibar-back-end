import os

# Define global configuration variables
print("===== Server Configuration =====")

start_time = None

deployment_name = os.environ.get("UNIBAR_DEPLOYMENT_NAME")
print("Deployment name:", deployment_name)
assert(deployment_name)

# Configure database
rds_hostname = os.environ.get("UNIBAR_RDS_HOSTNAME")
rds_username = os.environ.get("UNIBAR_RDS_USERNAME")
rds_password = os.environ.get("UNIBAR_RDS_PASSWORD")
rds_port = os.environ.get("UNIBAR_RDS_PORT")
rds_database = os.environ.get("UNIBAR_RDS_DATABASE")

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
