from celery import Celery

app = Celery('tasks', broker='pyamqp://', backend='rpc://')

@app.task
def add(x, y):
    return x + y


@app.task
def divide(x, y):
    return x/y