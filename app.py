from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import os
from datetime import datetime

DB_PATH = os.environ.get('BEWERBUNG_DB_PATH', 'data/bewerbungen.db')

app = Flask(__name__, static_folder='static', static_url_path='')


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db_connection()
    create_sql = (
        'CREATE TABLE IF NOT EXISTS applications ('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'title TEXT NOT NULL, '
        'url TEXT NOT NULL, '
        'description TEXT, '
        'type TEXT, '
        'feedback TEXT, '
        'done INTEGER NOT NULL DEFAULT 0, '
        'created_at TEXT NOT NULL'
        ')'
    )
    conn.execute(create_sql)
    conn.commit()
    conn.close()


@app.route('/api/applications', methods=['GET'])
def list_applications():
    conn = get_db_connection()
    select_sql = (
        'SELECT id, title, url, description, type, feedback, done, created_at '
        'FROM applications ORDER BY id DESC'
    )
    rows = conn.execute(select_sql).fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])


@app.route('/api/applications', methods=['POST'])
def create_application():
    payload = request.get_json(force=True) or {}
    title = (payload.get('title') or '').strip()
    url = (payload.get('url') or '').strip()
    description = (payload.get('description') or '').strip()
    type_ = (payload.get('type') or '').strip()
    feedback = (payload.get('feedback') or '').strip()

    if not title or not url:
        return jsonify({'error': 'title and url are required'}), 400

    conn = get_db_connection()
    now = datetime.utcnow().isoformat(timespec='seconds')
    insert_sql = (
        'INSERT INTO applications '
        '(title, url, description, type, feedback, done, created_at) '
        'VALUES (?, ?, ?, ?, ?, 0, ?)'
    )
    cur = conn.execute(insert_sql, (title, url, description, type_, feedback, now))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return jsonify({'id': new_id}), 201


@app.route('/api/applications/<int:app_id>', methods=['PUT'])
def update_application(app_id):
    payload = request.get_json(force=True) or {}
    allowed_fields = ('title', 'url', 'description', 'type', 'feedback', 'done')
    updates = {}
    for key in allowed_fields:
        if key in payload:
            updates[key] = payload.get(key)

    if not updates:
        return jsonify({'error': 'no fields to update'}), 400

    conn = get_db_connection()
    row = conn.execute('SELECT id FROM applications WHERE id = ?', (app_id,)).fetchone()
    if not row:
        conn.close()
        return jsonify({'error': 'not found'}), 404

    set_parts = []
    values = []
    for key, value in updates.items():
        if key == 'done':
            value = 1 if value else 0
        set_parts.append(key + ' = ?')
        values.append(value)
    values.append(app_id)

    update_sql = 'UPDATE applications SET ' + ', '.join(set_parts) + ' WHERE id = ?'
    conn.execute(update_sql, values)
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/applications/<int:app_id>', methods=['DELETE'])
def delete_application(app_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM applications WHERE id = ?', (app_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})


@app.route('/')
@app.route('/index.html')
def index():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
