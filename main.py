"""
- parsing dictionaries in jinja
- API (applicaiton program interface)
- simple app
    -bootstrap
    -homepage
    -client page
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/klientai')
def show_clients():
    clients = [
        {'id': 1,'name':"CompanyName1"},
        {'id': 2, 'name': "CompanyName2"},
        {'id': 3, 'name': "CompanyName3"},
        {'id': 4, 'name': "CompanyName4"},
        {'id': 5, 'name': "CompanyName5"}
    ]
    return render_template('clients.html', data=clients)


if __name__ == '__main__':
    app.run(debug=True)
