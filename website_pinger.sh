#!/usr/bin/bash

# Try to curl the server, if it fails, then send out an email.
RESPONSE_CODE=$(curl -s -o /dev/null -I -w "%{http_code}" $1)
if [ $RESPONSE_CODE -ne 200 ]; then
  ./send_email_alert.py "${@:2}"
fi
