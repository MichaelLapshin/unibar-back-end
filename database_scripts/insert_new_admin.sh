#!/bin/bash

# Database connectivity
db_user=$1
db_password=$2
db_host=$3
db_port=3306

# Entry details
admin_id=$(uuidgen)
admin_name=$4
auth_token=$(openssl rand -hex 16) # 32 digit string
registered_time=$(date '+%Y-%m-%d %H:%M:%S')

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

fi
