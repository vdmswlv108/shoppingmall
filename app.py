from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    addr_receive = request.form['addr_give']
    phone_receive = request.form['phone_give']

    order = {
        'name' : name_receive,
        'count' : count_receive,
        'addr' : addr_receive,
        'phone' : phone_receive
    }

    db.orders.insert_one(order)

    return jsonify({'result':'success', 'msg':'이 요청은 POST'})


@app.route('/order', methods=["GET"])
def read_order():
    orders = list(db.orders.find({}, {'_id':0}))
    return jsonify({'result':'success', 'orders':orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)