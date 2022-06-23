from flask import Flask         # Import the Flask class and create an application object

app = Flask(__name__)

@app.route('/')                 # Define routes for handling requests sent from various URLs
@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'


@app.route('/reporter/<int:reporter_id>')       # Create variable rules to handle dynamic URLs
def reporter(reporter_id):
    return f'''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''

@app.route('/article/<string:article_name>')
def article(article_name):
  return f'''
          <h2>{article_name.replace('-', ' ').title()}</h2>
          <a href="/
