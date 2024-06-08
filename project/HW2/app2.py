from flask import Flask, render_template, request, make_response,session, redirect, url_for
app = Flask(__name__)
app.secret_key ='5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221269e4'

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('hello'))
        
    else:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        session['e-mail'] = request.form.get('e-mail')
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return redirect(url_for('logout'))
    return render_template('hello.html', name=session['username'])

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)