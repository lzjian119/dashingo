# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('tasks',
             backend='redis://120.55.160.237:6379/1',
             broker='redis://120.55.160.237:6379/1')

@app.task
def add(x, y):
    return x + y