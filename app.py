from flask import Flask, render_template

app = Flask(__name__)

job_list = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Vilnius, Lithuania',
        'salary': '$2500'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Vilnius, Lithuania',
        'salary': '$3500'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Vilnius, Lithuania',
        'salary': '$2500'
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'Vilnius, Lithuania',
        'salary': '$4500'
    }
    
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=job_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
