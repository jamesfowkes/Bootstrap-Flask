from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SimpleForm(Form):

	name = StringField("Name", validators=[DataRequired()])

	action_url = ""

	@classmethod
	def set_action_url(cls, url):
		cls.action_url = url
