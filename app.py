from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://35.239.5.57:27017/')
db = client['test_db']
collection = db['records']

@app.route('/')
def index():
    records = collection.find()
    return render_template('index.html', records=records)

@app.route('/add', methods=['POST'])
def add_record():
    data = request.form['data']
    collection.insert_one({'data': data})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
