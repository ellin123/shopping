from flask import Flask, send_file

app = Flask(__name__,static_url_path='/assets',static_folder='assets')

@app.route('/commodity/index')
def index():
    #首页
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)