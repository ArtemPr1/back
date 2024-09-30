from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    with open('data.txt', 'a') as f:
        f.write(f"{data['data']}\n")
    return 'Данные успешно сохранены!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
