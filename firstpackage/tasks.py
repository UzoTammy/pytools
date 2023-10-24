from celery import Celery

celery_app = Celery('firstpackage.tasks')


@celery_app.task
def minus(x, y):
    return x-y

