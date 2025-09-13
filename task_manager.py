# task manager
import os
from datetime import date
user_file = 'user.txt'
task_file = 'task.txt'


def create_file():
  if not os.path.exists(user_file):
    with open(user_file,'w',encoding= 'utf8') as f: 
      f.write('username: admin\n password: adm1n')
  if not os.path.exists(task_file):
    with open(task_file,'w','utf8'):   
        pass