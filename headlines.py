import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
import urllib
import urllib2

app = Flask(__name__)

RSS_Feed = {'cbc':"https://www.cbc.ca/cmlink/rss-topstories",
             'ctv':"https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="cbc"):
    feed = feedparser.parse(RSS_Feed[publication])
    return render_template("home.html", articles=feed['entries'])

def get_rate(frm,to):
    return (to_rate/frm_rate,parsed.keys())

if __name__=='__main__':
    app.run(port=5000)
