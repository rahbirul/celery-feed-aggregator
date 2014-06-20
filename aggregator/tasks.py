import requests
import feedparser

from celery import task, group
from celery.utils.log import get_task_logger

from mongo import get_client, MONGODB_DATABSE

logger = get_task_logger(__name__)


@task(soft_time_limit=10)
def download(url):
    logger.info("Retrieving feed %s" % url)
    response = requests.get(url)
    return response.text

@task
def parse(feed):
    parsed_feed = feedparser.parse(feed)
    logger.info("%d Entries found" % len(parsed_feed.entries))

    #store the items in parallel
    jobs = group(store.s(parsed_feed.feed, entry) for entry in parsed_feed.entries)
    jobs.apply_async()


@task
def store(feed, item):
    logger.info("Storing content %s (%s - %s)" % (item.link, feed.title, feed.subtitle))
    mongo_client = get_client()
    db = mongo_client[MONGODB_DATABSE]
    collection = db.content
    doc = {'link': item.link, 'title': item.title, 'summary': item.summary}

    collection.insert(doc)
