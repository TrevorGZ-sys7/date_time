from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def home():

    now = datetime.now()

    date_time = now.strftime('%d/%m/%Y: %H-%M-%S')
    return render_template('index.html', date_time=date_time)

if __name__ == '__main__':
    app.run(debug=True)



