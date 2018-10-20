from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='',
    minutes='', minutes_error='')

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    firstName = request.form['firstName']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=firstName)



time_form = """
    <style>
        .error{{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method= 'POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}' />
        </label>
        <p class="error">(hours_error)</p>
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">(minutes_error)</p>
        <input type="submit" value="Validate" />
    </form>
"""


app.run()