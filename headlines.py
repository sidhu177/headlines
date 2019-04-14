import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
from urllib.request import urlopen
import urllib

app = Flask(__name__)

RSS_Feed = {'cbc':"https://www.cbc.ca/cmlink/rss-topstories",
             'ctv':"https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"}

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_Feed:
        publication = "cbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_Feed[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__=='__main__':
    app.run(port=5000)
