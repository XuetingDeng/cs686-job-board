from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv() 

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 3306))

mysql = MySQL(app)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM jobs")
    rows = cur.fetchall()
    cur.close()
    # change array of array to array of objs
    jobs = []
    for row in rows:
        job = {
            "id": row[0],
            "title": row[1],
            "company": row[2],
            "link": row[3],
            "post_date": row[4]
        }
        jobs.append(job)
    return jsonify(jobs)

@app.route('/')
def home():
    return "Welcome to the Job Board API!"

if __name__ == '__main__':
    app.run(debug=True)
