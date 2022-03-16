from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired


class CreateProperty(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    no_of_bedrooms = StringField('No. of Rooms', validators=[DataRequired()])
    no_of_bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    type = StringField('Property Type', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo=FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg','PNG', 'JPEG', 'JPG'])])