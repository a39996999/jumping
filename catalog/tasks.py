from __future__ import absolute_import, unicode_literals
from celery import shared_task
from multiprocessing import current_process
from .models import student

import sys
import os
from jumpy import counter

def  ansbile():
    current_process()._config = {'semprefix': '/mp'}
    
@shared_task
def task_count(username, Filename):
    current_process()._config = {'semprefix': '/mp'}
    out_path = 'Video_out/'+username
    if not (os.path.isdir(out_path)):
        os.mkdir(out_path)
    else:
        return;
    score = counter.Counting(username+'/'+Filename)
    student.objects.filter(std_No=username).update(score=Int(score))
    return score