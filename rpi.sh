#!/bin/bash
screen -d -m -S db bash -c 'python writetojson.py'
python jsontest.py