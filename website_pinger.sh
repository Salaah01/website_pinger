#!/usr/bin/bash

# Try to ping the server, if it fails, then send out an email.
PING_FAILED=$(ping -c 1 $1 | grep "100% packet loss" | wc -l)
if [ $PING_FAILED -eq 1 ]; then
  ./send_email_alert.py "${@:2}"
fi
