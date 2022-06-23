# Imagine you are looking to add a new furry friend to your family! On the pet adoption website,
# you browse through the categories of animals and select the one you’re interested in, which brings
# you to another page that contains a list of available pets. Then, you continue your search by
# further clicking on an individual pet to view its profile page.
#
# Every time you navigate to a different webpage, your browser is making a request to the web server.
# Thanks to routing, the server knows exactly which endpoint should handle the request and can
# return the correct HTML page to display.
#
# In this project, you’ll use Python’s Flask framework to create a simple pet adoption site
# that contains multiple routes.
#
# project from: https://www.codecademy.com/courses/learn-flask/projects/adopt-a-pet

from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
        <h1>Adopt a Pet!</h1>
        <p>Browse through the links below to find your new furry friend:</p>
        <ul>
        <li><a href='/animals/dogs'>Dogs</a></li>
        <li><a href='/animals/cats'>Cats</a></li>
        <li><a href='/animals/rabbits'>Rabbits</a></li>
        </ul>
        '''

@app.route('/animals/<string:pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'
  for i, pet in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{i}">' + pet['name'] + '</a></li>'
  html += '</ul>'
  return html

@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return f'''
          <h1> {pet["name"]} </h1>
          <img src="{pet["url"]}"/>
          <p>{pet['description']}</p>
          <ul>
            <li>Breed: {pet['breed']}</li>
            <li>Age: {pet['age']}</li>
          </ul>
          '''
