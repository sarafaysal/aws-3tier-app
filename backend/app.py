from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB_HOST = "10.0.135.150"
DB_NAME = "myappdb"
DB_USER = "postgres"
DB_PASSWORD = "iamsara0515"

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.get_json()
    text_input = data.get('text')

    if not text_input:
        return jsonify({"error": "No text provided"}), 400

    now = datetime.now()

    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO entries (text_input, created_at) VALUES (%s, %s)",
        (text_input, now)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Inserted successfully", "time": str(now)}), 200

@app.route('/entries', methods=['GET'])
def get_entries():
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()
    cur.execute("SELECT id, text_input, created_at FROM entries ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = [{"id": r[0], "text": r[1], "created_at": str(r[2])} for r in rows]
    return jsonify(result), 200

@app.route('/entries', methods=['DELETE'])
def clear_entries():
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()
    cur.execute("DELETE FROM entries")
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "All entries cleared"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
