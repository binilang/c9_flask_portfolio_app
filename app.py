from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')
#the three line above means @app.route --> "for whom ever" come to the '/' --> "main page"
# use get method to ['GET'] --> means load the pages. home_page functions, will return the index.html template. 
@app.route('/<name>')
def profile(name):
	name = "\n\n dear " + name + " welcome to this Class !!"
	return render_template('index.html', name=name)
#line 17 above means if we type main page: https://ronaldportfolio.herokuapp.com/python_apps/ronald --> take the name --> ronald 
# and the python will pass that to HTML --> index.html and instead of page 404 error say Hellow to that name --> in our case we pass "coder" 
# & we salute them halo "clever coder ronald" 

@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 1
  	      try:
	
		interval_input = request.form['text'].split() #retreived the string input and split them in to'interval_input list 
		min_number = int(interval_input[0])
	      	max_number = int(interval_input[1])
	      	n_series = int(interval_input[-1])
  	      	#for str_num in request.form['text'].split():
		for n_num in range (n_series) 
			min_number, max_number = max_number, min_number+max_number
		total = min_number
		total1 = max_number/min_number
  	      		#total *= int(str_num)
  	      	return render_template('add_numbers.html', result=str(total)) render_template('add_numbers.html', result1=str(total1))
  	      except ValueError:
		return " Easy now !, please ensure your input in format of: 'start no'[ ]stop no[ ]n_sequence[ ]"
  	      	#return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)

         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')


if __name__ == '__main__':
	app.run(debug=True)
