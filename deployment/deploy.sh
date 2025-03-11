#!/bin/bash

# Stop the service if it's running
sudo systemctl stop twitter_id_service

# Copy the service file to systemd
sudo cp deployment/twitter_id_service.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Start the service
sudo systemctl start twitter_id_service

# Enable the service to start on boot
sudo systemctl enable twitter_id_service

# Check the status
sudo systemctl status twitter_id_service
