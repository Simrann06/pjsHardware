from flask import *
from pythonDBMS521 import *
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Qsdf(*&l;"w897uyg'

@app.route('/')
def to_home():
    return render_template('homePage.html')


@app.route('/login', methods=['GET', 'POST']) 

def login(): 

    if request.method=='GET': 
        return render_template('login521.html')
    else: 
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "password":
            return redirect(url_for('admin'))
        if username == "manager" and password == "password":
            return redirect(url_for('manager'))

        else:
            flash('Incorrect username or password!')
            return redirect(url_for('login'))


@app.route('/adminHome')
def admin():
    return render_template('adminHome.html')

@app.route('/InventoryManagerHome')
def manager():
    return render_template('InventoryManagerHome.html')

       
if __name__ == "__main__":
    # Launch the Flask dev server
    app.debug = True
    app.run()
