from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TemplateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    numpds = StringField('Number of Periods', validators=[DataRequired()])
    p1title  = StringField('Period 1 Title', validators=[DataRequired()])
    p1time = StringField('Period 1 Time', validators=[DataRequired()])
    p2title = StringField('Period 2 Title', validators=[DataRequired()])
    p2time = StringField('Period 2 Time', validators=[DataRequired()])
    p3title = StringField('Period 3 Title', validators=[DataRequired()])
    p3time = StringField('Period 3 Time', validators=[DataRequired()])
    submit = SubmitField('Create Template')