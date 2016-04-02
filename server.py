from flask import Flask, jsonify

app = Flask(__name__)
pdfs = [
	{
		'id' : 1,
		'name' : 'CSC 232 Autonomous Mobile Robots',
		'file' : 'sample-syllabus.pdf'
	}
]

@app.route("/")
def index():
	return "hi"

@app.route("/api/v1.0/pdfs", methods=['GET'])
def get_pdfs():
	return jsonify({'pdfs' : pdfs})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)


