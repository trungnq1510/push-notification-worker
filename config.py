DEBUG = True
TOPICS = {
    "ios": {
        "channel": "notification",
        "workers_module": "push-notification-workers",
        "num_of_worker": 2
    },
    "android": {
        "channel": "notification",
        "workers_module": "push-notification-workers",
        "num_of_worker": 2
    }
}
MAX_PROCESSED_MESSAGES_QUEUE = 200
NSQLOOKUPD_HTTP_ADDRESSES = "http://127.0.0.1:4161"

