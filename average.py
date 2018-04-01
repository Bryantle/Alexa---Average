from flask import Flask, render_template
from flask_ask import Ask, question, session, statement
import logging

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@app.launch
def launcher():
  return question(render_template('start'))

@app.intent("yesIntent")
def yes():
  return question(render_template('yes'))

@app.intent("noIntent")
def no():
  return statement(render_template('no'))

@app.intent("averageIntent", convert = {'x': int, 'y': int})
def averager(x,y):
  z = (x + y)*.5
  message = "The average of {} and {} is {}.".format(x,y,z)
  return statement(message)

@app.session_ended
def end():
  return statement(render_template('end'))

if __name__ == '__main__':
  app.run(debug = True)
