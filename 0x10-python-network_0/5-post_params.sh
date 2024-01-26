#!/bin/bash
# sends the response
curl -Ls -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"

