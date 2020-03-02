# initial imports
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify
from flask_cors import CORS

import pymongo
import random
import string
from bson.objectid import ObjectId

# instance and config
app = Flask(__name__)
#CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}}, headers='Content-Type')
app.config['TEMPLATES_AUTO_RELOAD'] = True


#------------------------------------------------------------------------------


# database connection
# connection = pymysql.connect(host='127.0.0.1', user='root', db='DJPlayList')
# cursor = connection.cursor()



# functions
# Function to generate a random string with the combination of lowercase and uppercase letters
def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Function to create x number of screenshot URLs
def generateURL(x):
	urls_slugs = []
	for i in range(x):
		d1 = random.randint(0, 9)
		d2 = random.randint(0, 9)
		d3 = random.randint(0, 9)
		d4 = random.randint(0, 9)
		s = randomString(2)
		slug = f'{s}{d1}{d2}{d3}{d4}'
		urls_slugs.append(slug)
	return urls_slugs


# routes
# Route for handling the login page logic
    
@app.route("/")
def main():
	slugs = generateURL(100)
	print(slugs)
	return render_template('index.html', slugs=slugs)


#------------------------------------------------------------------------------


if __name__ == "__main__":
	#app.run()
	app.run()