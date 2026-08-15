from flask import Flask
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    return "Hello from Flask + Redis!"

@app.route("/count")
def count():
    value = redis_client.incr("visits")
    return f"Visits: {value}"

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)
