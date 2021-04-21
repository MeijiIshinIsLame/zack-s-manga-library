from flask import Flask, render_template, request
import os
app = Flask(__name__)

EXT = ['.jpg', '.jpeg', '.gif', '.png']
BASE_DIR = os.path.join(os.getcwd(), 'static')

@app.route('/')
def initial_browse():
	item_list = os.listdir(BASE_DIR)
	item_list.remove("css")
	return render_template('browse.html', url_file_path=None, item_list=item_list)

@app.route('/<path:url_file_path>')
def browse_nested(url_file_path):
	nested_file_path = os.path.join(BASE_DIR, url_file_path)
	if os.path.isdir(nested_file_path):
		item_list = os.listdir(nested_file_path)
		
		#if there is an image file, we know theres manga
		item_list.sort()
		for item in item_list:
			for extension in EXT:
				if extension in item:
					return render_template('read.html', url_file_path=url_file_path, item_list=item_list)
					
		#else keep browsing
		return render_template('browse.html', url_file_path=url_file_path, item_list=item_list)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
