#!/bin/bash

# Naredimo image
docker build Server/ -t server_sa_webcam
docker build Client/ -t client_sa_webcam

# # Naredimo network
docker network create webcam_net || true

# Zaženemo kontejnerje
docker run --rm -d -p 5000:80 --network webcam_net --name webcam_client client_sa_webcam

# Privileged damo, da lahko dostopa do kamere
docker run --privileged --rm -d -p 5001:5001 --network webcam_net --name webcam_server server_sa_webcam