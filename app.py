import variable as var
import webbrowser
from flask import Flask, render_template
app = Flask(__name__)


def compute_message():
    return var.shape()
    
@app.route('/')
def index():
    my_variable = compute_message()
    #my_variable = "square"

    if my_variable=="round":
        return render_template('roundmain.html', variable=my_variable)
    if my_variable=="square":
        return render_template('squaremain.html', variable=my_variable)
    if my_variable=="heart":
        return render_template('heartmain.html', variable=my_variable)
    if my_variable=="oval":
        return render_template('ovalmain.html', variable=my_variable)
    

if __name__ == '__main__':
    app.run(debug=True)
    webbrowser.open('http://127.0.0.1:5000/')
