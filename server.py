
from flask import Flask, render_template, url_for, request, redirect
import csv 				# <--- DB
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


#  			*OR for more dynamic

@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)

#            *For SEND btn
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     return 'YOUR FORM SUBMITTED..!!!!'

#  *** You can also use below code- form submit (dynamic) ***

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
# 	if request.method == 'POST':
# 		data = request.form.to_dict()
# 		print(data)
# 		return redirect('/thankyou.html')		#call html page
# 	else:
# 		return 'something went wrong. try again.!!!'



# 	* DB submit form and save form data in .txt file

# def write_to_file(data):
# 	with open('database.txt', mode='a') as database:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		file = database.write(f'\n {email}, {subject}, {message}')

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
# 	if request.method == 'POST':
# 		data = request.form.to_dict()
# 		write_to_file(data)
# 		return redirect('/thankyou.html')		#call html page
# 	else:
# 		return 'something went wrong. try again.!!!'


#  send btn   ** DATABASE with CSV **

def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form2():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')		#call html page
		except:
			return 'Did not send'	
	else:
		return 'something went wrong. try again.!!!'









