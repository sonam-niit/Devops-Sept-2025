#!/bin/bash

LOG_DIR="myapp"
LOG_FILE="app.log"
MAX_BACKUP=3

# Create diretcory if not exist
mkdir -p $LOG_DIR
## LOG ROTATION
# app.log --> app.log.1.gz --> app.log.2.gz 

for ((i=$MAX_BACKUP; i>0; i--)); do 
    if [ -f "$LOG_DIR/$LOG_FILE.$i.gz" ]; then 
        next=$((i+1))
        mv "$LOG_DIR/$LOG_FILE.$i.gz" "$LOG_DIR/$LOG_FILE.$next.gz"
    fi 
done 

# incase if no file then create empty log file
touch "$LOG_DIR/$LOG_FILE"

# Let'c compress log file
if [ -f "$LOG_DIR/$LOG_FILE" ]; then
    mv "$LOG_DIR/$LOG_FILE" "$LOG_DIR/$LOG_FILE.1"
    gzip "$LOG_DIR/$LOG_FILE.1"
fi

# Delete logs files beyond limit
if [ -f "$LOG_DIR/$LOG_FILE.$((MAX_BACKUP+1)).gz" ]; then
    rm "$LOG_DIR/$LOG_FILE.$((MAX_BACKUP+1)).gz"
fi 