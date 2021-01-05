from flask import Flask, request, render_template, jsonify
from flask_restful import Api, Resource
from newspaper import Article

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    return render_template("index.html")

class main(Resource):
    def get(self):
        return render_template('index.html')


class send(Resource):
    def post(self):
        try:
            data = request.form
            url = data['messege']
            article = Article(url,keep_article_html=True,request_timeout=10000,fetch_images=True,MIN_WORD_COUNT=70,browser_user_agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",MAX_TEXT=100000000,MAX_TITLE=500)
            article.download()
            article.parse()
            retJson = {
                "article-url": url,
                "article-title": article.title,
                "article-text": article.text,
                "article-html": article.html,
                "status" : 200
            }
            return jsonify(retJson)
        except:
            return {               
                'messege':"Data not found.",
                'status':404
            }
            
    def get(self):
        return 'You are trying to enter from a wrong way. you bad boy....'


api.add_resource(send,'/send')
api.add_resource(main,'/main')

if __name__ == '__main__':
    app.run(host='0.0.0.0',bug=True)
