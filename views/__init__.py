from VetLife import app

@app.route('/')
@app.route('/index')

def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
