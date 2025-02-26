from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv() 

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM jobs")
    jobs = cur.fetchall()
    cur.close()
    return jsonify(jobs)

@app.route('/')
def home():
    return "Welcome to the Job Board API!"

if __name__ == '__main__':
    app.run(debug=True)
