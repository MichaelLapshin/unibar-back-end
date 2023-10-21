#!/bin/bash

# Entry details
admin_id=$(uuidgen)
admin_name=$1
auth_token=$(openssl rand -hex 16) # 32 digit string
registered_time=$(date '+%Y-%m-%d %H:%M:%S')

# Database connectivity
db_user="${2:-$UNIBAR_RDS_USER}"
db_password="${3:-$UNIBAR_RDS_PASSWORD}"
db_host="${4:-$UNIBAR_RDS_HOSTNAME}"
db_port="${5:-$UNIBAR_RDS_PORT}"

if [[ $# -eq 4 ]]; then
    echo "INSERT INTO UniBar.Admins (admin_id, name, auth_token, registered_time) VALUES \
            ('$admin_id', '$admin_name', '$auth_token', '$registered_time');" \
            | mysql -u$db_user -p$db_password -h$db_host -P$db_port
    
    echo "=== New admin entry ==="
    echo admin_id: $admin_id
    echo admin_name: $admin_name
    echo auth_token: $auth_token
    echo registered_time: $registered_time
    echo "======================="
    echo "Warning: Record the above information! Your admin token is important and will not be displayed again."
else
    echo "Invalid input. Use: './insert_new_admin <admin_name> <db_user> <db_password> <db_host> <db_port>' OR ./insert_new_admin <admin_name>"
fi
