#!/bin/bash

export FLASK_APP='api.py'
export APP_SETTINGS='test_tric.config.Config'
export DATABASE_URL='postgresql://username:password@localhost/postgres'

flask db init
flask db migrate -m "initial"
flask db upgrade
# flask db downgrade
