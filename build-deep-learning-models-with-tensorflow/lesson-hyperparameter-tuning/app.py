import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
  #this code below is to test the plotting functionality
  #not actually needed later
  #x = [1,2,3,4,5]
  #y = [20,30,-40,10,-50]
  #plt.plot(x,y)
  #plt.savefig('static/images/new_plot.png')
  return render_template('plt_tmpl.html', name = "Hyperparameter tuning: learning rate", url ='static/images/my_plot.png')
