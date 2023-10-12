#!/bin/bash

# Database connectivity
db_user=$1
db_password=$2
db_host=$3
db_port=3306

# Entry details
admin_id=$(uuidgen)
admin_name=$4
admin_token=$(openssl rand -hex 16) # 32 digit string
admin_time=$(date '+%Y-%m-%d %H:%M:%S')

if [[ $# -eq 4 ]]; then
    echo "INSERT INTO UniBar.Admins (admin_id, name, admin_token, registered_time) VALUES \
            ('$admin_id', '$admin_name', '$admin_token', '$admin_time');" \
            | mysql -u$db_user -p$db_password -h$db_host -P$db_port
    
    echo "=== New admin entry ==="
    echo admin_id: $admin_id
    echo admin_name: $admin_name
    echo admin_token: $admin_token
    echo admin_time: $admin_time
    echo "======================="
    echo "Warning: Record the above information! Your admin token is important and will not be displayed again."

fi
