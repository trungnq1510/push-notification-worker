# -*- coding: utf-8 -*-
import nsq
import config
from libs.worker import load_worker
from tornado.options import options
import sys


def bootstrap(worker_module, topic, channel):
    worker = load_worker(worker_module, topic, channel)
    legacy = False
    try:
        from nsq import LegacyReader
    except ImportError:
        legacy = True
    if not legacy:
        # nsq 0.5+
        for name, handler in worker.handlers.iteritems():
            r = nsq.Reader(topic, "%s_%s" % (channel, name[0:-len("_handler")]),
                           message_handler=handler,
                           lookupd_http_addresses=config.NSQLOOKUPD_HTTP_ADDRESSES)

            # override default preprocess and validate method with worker's
            # method
            r.validate_message = worker.validate_message
            r.preprocess_message = worker.preprocess_message
    else:
        # nsq 0.4
        r = nsq.Reader(all_tasks=worker.handlers,
                       topic=topic,
                       channel=channel,
                       lookupd_http_addresses=config.NSQLOOKUPD_HTTP_ADDRESSES)

        r.validate_message = worker.validate_message
        r.preprocess_message = worker.preprocess_message

    options.parse_command_line()
    nsq.run()

if __name__ == "__main__":
    worker_module = sys.argv[1]
    topic = sys.argv[2]
    channel = sys.argv[3]
    bootstrap(worker_module=worker_module, topic=topic, channel=channel)
