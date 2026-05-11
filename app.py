from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return '<h1>Welcome to My App</h1>'

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO users (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        return '<h1>Success</h1>'
    return '''
        <form method="POST">
            <input id="name" name="name" placeholder="Enter name">
            <button id="submit-btn" type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
