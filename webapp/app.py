'''
    Authors:
    Valentina Guerrero
    Aishwarya Varma 
'''
import sys
import argparse
import flask
import api


app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

# This route delivers the user your site's home page.
@app.route('/')
def home():
    return flask.render_template('home.html')


@app.route('/home')
def test():
    return flask.render_template('home.html')


@app.route('/results')
def results():
    return flask.render_template('results.html')


@app.route('/movie')
def movie():
    return flask.render_template('movie.html')

@app.route('/advanced')
def advanced_search():
    return flask.render_template('advanced_search.html')

@app.errorhandler(404)  
def not_found(e): 
  return flask.render_template("error.html") 

# This route supports relative links among your web pages, assuming those pages
# are stored in the templates/ directory or one of its descendant directories,
# without requiring you to have specific routes for each page.
@app.route('/<path:path>')
def shared_header_catchall(path):
    return flask.render_template(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A tiny Flask application, including API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
