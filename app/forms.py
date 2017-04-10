import flask_wtf
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(flask_wtf.Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
