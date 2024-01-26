#!/bin/bash
# print
curl -so /dev/null -w "%{http_code}" "$1"
