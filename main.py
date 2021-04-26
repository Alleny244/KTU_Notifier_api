# set FLASK_APP=app.py
# flask run
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import lxml
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        html = requests.get(
            "https://ktu.edu.in/eu/core/announcements.htm").text

    soup = BeautifulSoup(html, 'lxml')
    notifications = soup.find_all("tr")
    original = ""
    with open("count.txt", "r") as f:
        original = f.read()

        original = int(float(original))

    length = len(notifications)
    print(length)
    l = []
    if length == original:
        lists = notifications[0:7]

        for notification in lists:
            d = {}
            d['notification_head'] = notification.li.b.text
            date = notification.td.strong.text
            d['dte'] = "Time : "+date
            links = notification.a['href']
            d['link'] = "https://ktu.edu.in/"+links
            d['updated'] = False
            l.append(d)

    else:
        with open("count.txt", "w") as f:
            f.write(str(length))

        lists = notifications[0:7]
        for notification in lists:

            d = {}
            d['notification_head'] = notification.li.b.text
            date = notification.td.strong.text
            d['dte'] = "Time : "+date
            links = notification.a['href']
            d['link'] = "https://ktu.edu.in/"+links
            d['updated'] = True
            l.append(d)

    return jsonify(l)


if __name__ == '__main__':
    app.run()
