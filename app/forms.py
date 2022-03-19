from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField,  SelectField 
from wtforms import TextAreaField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired


class CreateProperty(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    no_of_bedrooms = StringField('No. of Rooms', validators=[DataRequired()])
    no_of_bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    prices = StringField('Price', validators=[DataRequired()])
    types = SelectField('Property Types', choices=[('Single-Family', 'Single-Family'), ('Multi-Family', 'Multi-Family'), ('Apartment', 'Apartment'), ('Town-House', 'Town-House'), ('Mansion', 'Mansion'), ('Villa', 'Villa'), ('Condo', 'Condo'), ('Co-operative', 'Co-operative')],validators=[InputRequired()])
    option = SelectField('Tenure Type', choices=[('Rent', 'Rent'), ('Sale', 'Sale')],validators=[InputRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo=FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg','PNG', 'JPEG', 'JPG', 'jng', 'JNG', 'gif', 'GIF'])])