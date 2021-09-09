from flask import Flask
from celery import Celery

# app = Flask(__name__)

app = Celery(
    __name__,
    broker="redis://159.75.132.94:6379/0",
    backend="redis://159.75.132.94:6379/1"
)



# @app.route("/")
# def hello():
#     return "Hello, World!"



@app.task
def divide(x, y):
    import time
    time.sleep(5)
    return x / y