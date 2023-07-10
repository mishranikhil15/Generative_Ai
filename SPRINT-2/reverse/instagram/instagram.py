from flask import request,Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])

def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__=='__main__'
    app.run()        