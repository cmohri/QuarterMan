from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class ScheduleForm(FlaskForm):
    title = StringField("Schedule Name", validators=[DataRequired()])
    desc = StringField("Description", validators=[DataRequired()])
    schedule = HiddenField()
    private = BooleanField("Private")
