from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sunrise')
def sunrise():
    print('sunrise')
    return app.send_static_file('pix/sunrise.mp4')

@app.route('/<path:path>')
def static_proxy(path):
    print(path)
    # send_static_file will guess the correct MIME type
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
