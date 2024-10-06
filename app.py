import django
import requests
import requests_cache
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def api_request():
    session = requests_cache.CachedSession('fruit_cache')

    url = "https://api.jwstapi.com/observation/jw02731002001_02107_00004_mirimage_o002?page=1&perPage=10"

    payload={}
    headers = {
        'X-API-KEY': '1a56a3a7-d082-4dec-8aa6-7ceeda672c5c'
    }

    response = session.request("GET", url, headers=headers, data=payload)
    results = response.json()

    print(results)

if __name__ == '__main__':
    app.run()
    api_request()