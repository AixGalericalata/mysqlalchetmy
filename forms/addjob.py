from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job_title = StringField('Job Title', validators=[DataRequired()])
    team_leader_id = IntegerField("Team_leader_id")
    work_size = IntegerField("Work size")
    collaborators = StringField('Collaborators')
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField('Submit')
