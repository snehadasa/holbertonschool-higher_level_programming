#!/bin/bash
# cript that sends a JSON POST request to a URL, and displays the body
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
