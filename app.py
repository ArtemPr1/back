from flask import Flask, request, send_from_directory

app = Flask(__name__, static_folder='../front', static_url_path='')

# Обслуживание главной страницы
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

# Обслуживание CSS и JS
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(app.static_folder + '/css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(app.static_folder + '/js', filename)

# Маршрут для приёма данных с фронтенда
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    with open('data.txt', 'a') as f:
        f.write(f"{data['data']}\n")
    return 'Данные успешно сохранены!', 200

# Запуск сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
