from flask import Flask
from flask import render_template

app = Flask(__name__)

#begin routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/colores-en-nahuatl')
def colores():
    return render_template('colores.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
#end routes

if __name__ == '__main__':
    app.run('0.0.0.0', 4000, debug=True)
    #app.run(host='0.0.0.0')
