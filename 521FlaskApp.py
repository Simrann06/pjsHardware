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

        if username == "root" and password == "password":
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password!')
            return redirect(url_for('login'))


@app.route('/home', methods=['POST', 'GET'])

def home():

    if request.form.get('action1') == 'Check In Inventory':
        return redirect(url_for('checkin'))

    if request.form.get('action1') == 'Edit Inventory':
        return redirect(url_for('edit'))

    if request.form.get('action1') == 'Check Out Inventory':
        return redirect(url_for('checkout'))

    else: 
        return render_template('home.html') 

@app.route('/checkinInventory')
def checkin():
    return render_template('checkinInventory.html')

@app.route('/editInventory')
def edit():
    return render_template('editInventory.html')

@app.route('/checkoutInventory', methods=['POST'])
def checkout():

    input = request.form.get('text')
    if request.method == 'POST':

        serialNumber = input
        first_digit = int(str(input)[0])

        if first_digit == "3":
            remove_product_cellphone(serialNumber)

        if first_digit == "5":
            remove_product_laptop(serialNumber)

        if first_digit == "7":
            remove_product_tablet(serialNumber)

    else: 
       return render_template('checkoutInventory.html')



       
if __name__ == "__main__":
    # Launch the Flask dev server
    app.debug = True
    app.run()
