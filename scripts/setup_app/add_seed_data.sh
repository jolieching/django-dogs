#!/bin/bash

# This script adds seed data
# https://en.wikipedia.org/wiki/Database_seeding

python manage.py loaddata dog_pics/seeds.yaml
