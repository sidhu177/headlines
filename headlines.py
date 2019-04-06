import feedparser
from flask import Flask

app = Flask(__name__)

RSS_Feed = {'cbc':"https://www.cbc.ca/cmlink/rss-topstories",'ctv':"https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"}

@app.route("/")
@app.route("/cbc")
def cbc():
    return get_news('cbc')

@app.route("/ctv")
def ctv():
    return get_news('ctv')

def get_news(publication):
    feed = feedparser.parse(RSS_Feed[publication])
    first_article = feed['entries'][0]
    return """<html>
      <body>
           <h1> Top Headlines </h1>
           <b>{0}</b> <br/>
           <i>{1}</i> <br/>
           <p>{2}</p> <br/>
      </body>
    </html>""".format(first_article.get("title"), first_article.get("image"), first_article.get("description"))

if __name__=='__main__':
    app.run(port=5000)
