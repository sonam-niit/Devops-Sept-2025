#!/bin/bash

echo "Update Packages"
sudo apt update -y
echo "Upgrade all Packages"
sudo apt upgrade -y
echo "remove absolute packages"
sudo apt autoremove -y

echo "Your System is Up to Date"