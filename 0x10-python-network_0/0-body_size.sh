#!/bin/bash
# temporary file
curl -I "$1" -s | grep Content-Length | cut -d ' ' -f2
