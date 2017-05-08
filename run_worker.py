# -*- coding: utf-8 -*-
import config
from subprocess import call, Popen, PIPE
import requests
import urllib, urllib2
import httplib

def run():
    for topic_name, topic_option in config.TOPICS.iteritems():
        num_of_worker = topic_option.get("num_of_worker")
        topic = topic_name
        worker_module = topic_option.get("workers_module")
        channel = topic_option.get("channel")
        # create topic
        # create_url = config.NSQLOOKUPD_HTTP_ADDRESSES + "/topic/create?topic=%s" % topic
        # import pdb; pdb.set_trace();
        # response = requests.post(url=create_url)
        for i in range(0, num_of_worker):
            Popen(["python", "bootstrap.py", worker_module, topic, channel])


if __name__ == "__main__":
    run()