#!/bin/bash
# dis accept
curl -LsI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f1 --complement
