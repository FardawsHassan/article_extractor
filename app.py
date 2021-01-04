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
            #url="https://newspaper.readthedocs.io/en/latest/"
            article = Article(url,keep_article_html=True)
            article.download()
            article.parse()
        except:
            return {               
                'messege':"Data not found.",
                'status':404
            }
        else:
            retJson = {
                "article": article.text,
                "status" : 200
            }
            return jsonify(retJson)
    def get(self):
        return 'You are trying to enter from a wrong way. you bad boy....'


api.add_resource(send,'/send')
api.add_resource(main,'/main')

if __name__ == '__main__':
    app.run(debug=True)