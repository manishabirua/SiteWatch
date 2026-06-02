from flask import Flask, render_template
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def dashboard():
    data = r.hgetall("sitewatch")
    sites = []
    for url, value in data.items():
        status, timestamp = value.split(" | ")
        sites.append({
            "url": url,
            "status": status,
            "timestamp": timestamp
        })
    return render_template('index.html', sites=sites)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
