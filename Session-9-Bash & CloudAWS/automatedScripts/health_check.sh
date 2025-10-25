#!/bin/bash

echo "Health Check Report - $(date)"

echo ""
echo "Memory Usage"
free -h | awk '/Mem:/ {print "Used: "$3" / Total: "$2" ("$3/$2*100"% used)" }'

echo ""
echo "Disk Usage"
df -h --total | grep 'total' | awk '{print "Used: "$3" / Total: "$2"("$5" used)"}'

echo ""
echo "CPU Load"
uptime
