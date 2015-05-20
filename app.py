from flask import Flask, render_template, url_for, redirect
from view_simple_form import SimpleForm

app = Flask(__name__)
app.config.from_object("config.DevConfig")

@app.route('/', methods=('GET', 'POST'))
def view_simple_form():

	form = SimpleForm()
	form.set_action_url(url_for('view_simple_form'))

	if form.validate_on_submit():
		return render_template('template.simple-view.html', name = form.name.data)
	else:
		return render_template('template.simple-form.html', form=form)

if __name__ == "__main__":
	app.run(debug=True)
