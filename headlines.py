import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_Feed = {'cbc':"https://www.cbc.ca/cmlink/rss-topstories",
             'ctv':"https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="cbc"):
    feed = feedparser.parse(RSS_Feed[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__=='__main__':
    app.run(port=5000)
