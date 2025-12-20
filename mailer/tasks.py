from time import sleep
from celery import shared_task

@shared_task
def notify_users(message):
  print("in notify_users...")
  print(f'message: {message}')
  sleep(10)
  print("done!")