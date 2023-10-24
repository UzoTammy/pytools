from celery import Celery

celery_app = Celery('firstpackage.tally')


@celery_app.task
def minus(x, y):
    return x-y

