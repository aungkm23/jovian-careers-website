from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Yangon, Myanmar',
    'salary': 'Ks. 1,500,000'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Yangon, Myanmar',
    'salary': 'Ks. 1,000,000'
  },
  {
    'id': 3,
    'title': 'Front End Engineer',
    'location': 'Remote',
    'salary': 'Ks. 1,200,000'
  },
  {
    'id': 4,
    'title': 'Back End Engineer',
    'location': 'San Francisco, USA',
    'salary': '$ 100,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
