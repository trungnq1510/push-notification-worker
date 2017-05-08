# -*- coding: utf-8 -*-
import logging
from libs import Worker


class IosNotificationWorker(Worker):
    def push_handler(self, message):
        logging.info("%s", message.body)
        return True
