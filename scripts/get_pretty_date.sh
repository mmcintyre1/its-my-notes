#!/bin/bash

# get the date in the desired format
date_formatted=$(date +"%F %T.%6N")

# copy the formatted date to the clipboard using clip.exe
echo -n "$date_formatted" | clip.exe

echo "Formatted date copied to clipboard."