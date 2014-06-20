BROKER_URL = 'amqp://guest:guest@localhost:5672//'

CELERY_IMPORTS = ('tasks', )

#CELERY_ALWAYS_EAGER = True

CELERY_CREATE_MISSING_QUEUES = True

CELERY_TASK_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['pickle', ]

CELERY_ROUTES = {
                    'tasks.download': {'queue': 'download'},
                    'tasks.parse': {'queue': 'parse'},
                    'tasks.store': {'queue': 'store'},
                }