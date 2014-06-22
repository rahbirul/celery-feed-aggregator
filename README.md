# celery-feed-aggregator

A Sample app for demonstrating the use of Celery (as part of the talk given in PyCon Dhaka 2014).

## What does it do?

It downloads and parses a set of RSS feeds in parallel, extracts the content and stores them in MongoDB.

## Perquisites 

1. RabbitMQ
2. MongoDB
3. Python 2.5+

## Set up

1. [Install RabbitMQ](http://www.rabbitmq.com/download.html)
2. [Install MongoDB](http://docs.mongodb.org/manual/installation/)
3. Clone the repo on the local machine: `git clone git@github.com:rubayeet/celery-feed-aggregator.git`
4. Install the required libraries (preferably in a `virtualenv`):
    `pip install -r requirements.txt`
5. Queue up the RSS feeds: `python feeds.py`
6. Run the Celery worker: `celery worker -Q download,parse,store -c 10 -l INFO`

### Vagrant Based Setup

If you have Vagrant installed in your local machine, the project includes spec for a 64 bit Ubuntu 12.04 VM which will 
automatically install the required services and librarie. So you can skip steps 1 to 4 by just typing `vagrant up` in 
your repo.