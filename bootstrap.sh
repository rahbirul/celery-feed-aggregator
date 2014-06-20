#!/usr/bin/env bash

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
sudo apt-get update
sudo apt-get -y install mongodb-org

sudo sh -c "echo 'deb http://www.rabbitmq.com/debian/ testing main' >> /etc/apt/sources.list"
wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc
sudo apt-get update
sudo apt-get -y install rabbitmq-server

wget http://python-distribute.org/distribute_setup.py
sudo python distribute_setup.py
sudo easy_install pip

sudo pip install virtualenv

virtualenv ~/celery_aggregator

source ~/celery_aggregator/bin/activate
pip install -r /vagrant/requirements.txt