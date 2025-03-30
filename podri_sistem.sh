#!/bin/bash

docker rm -f webcam_client webcam_server
docker rmi -f client_sa_webcam server_sa_webcam
docker network rm webcam_net