from flask import Flask, render_template, request, redirect

# Defining our Flask App
app = Flask(__name__)

"""
Notice the @app.route() decorators above the functions below. These essentially
create the different urls/links for the web app.
"""

# This is the HomePage with the URL "/"
@app.route('/')
def hello():
    # Flask automatically looks for html templates in folders named 'templates'
    # This renders the home page defined in the index.html file
    return render_template('index.html')

# This is the DemoPage with the URL "/tables"
@app.route('/tables')
def display_table():
    # Flask automatically looks for html templates in folders named 'templates'
    # This renders the home page defined in the index.html file
    return render_template('SampleDGWorksTable.html')

@app.route('/basics')
def basics():
    return render_template('basics_table.html')

@app.route('/csc')
def csc():
    return render_template('csc_table.html')


# This is what causes the web app to run
if __name__ == '__main__':
    app.run(debug=True)
