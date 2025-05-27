#!/bin/bash

curl -d "service_name=corrector&state_type=1" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://localhost:5000/state/new
