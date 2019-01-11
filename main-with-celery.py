import time

from celery import Celery

app = Celery("main-with-celery", broker="amqp://guest:guest@localhost:5672/")

@app.task
def sleep_asyncrhrously():
    time.sleep(20)
    print("20 detik selesai")

print("... Mulai")

sleep_asyncrhrously.delay()

print("... Akhir aplikasi sederhana")