from datetime import datetime

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import requests

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.test


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detail/<idx>')
def detail(idx):
    return render_template("detail.html", word=idx)

@app.route('/post', methods=['POST'])
def save_post():
    url_receive = request.form['url_give']
    pw_receive = request.form['pw_give']
    comment_receive = request.form['comment_give']

    doc = {
        'url': url_receive,
        'pw': pw_receive,
        'comment': comment_receive
    }

    db.articles.insert_one(doc)

    return jsonify({'msg': '저장이 완료되었습니다!'})


@app.route('/post', methods=['GET'])
def get_post():
    posts = 0
		// todo
    return jsonify({"posts": posts})


@app.route('/post', methods=['DELETE'])
def delete_post():
    idx = request.args.get('idx')
    db.test.delete_one({'idx': int(idx)})
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)