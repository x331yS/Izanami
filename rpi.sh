#!/bin/bash
screen -d -m -S db bash -c 'python writetojson.py'
echo "Database Listener Launched"
python jsontest.py