import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_Feed = {'cbc':"https://www.cbc.ca/cmlink/rss-topstories",'ctv':"https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"}

@app.route("/")
@app.route("/cbc")
def cbc():
    return get_news('cbc')

@app.route("/ctv")
def ctv():
    return get_news('ctv')

@app.route("/<publication>")
def get_news(publication="cbc"):
    feed = feedparser.parse(RSS_Feed[publication])
    first_article = feed['entries'][0]
    return render_template("home.html")


if __name__=='__main__':
    app.run(port=5000)
