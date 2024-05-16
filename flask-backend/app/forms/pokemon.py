from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,URLField
from wtforms.validators import DataRequired, Length,URL,NumberRange,ValidationError

def is_array(form, field):
    if not isinstance(field.data, list):
        raise ValidationError('Moves must be an array.')

class PokemonForm(FlaskForm):
    
    number = IntegerField('happiness',validators=[DataRequired,Length(min=0 ,message='Must be betweenn 0-100')])
    attack = IntegerField('attack',validators=[DataRequired(),NumberRange(min=0,max=100)])
    imageUlr = StringField('Url', validators=[DataRequired("Must add a url"),Length(min=0,max=255,message="Url must be 0-255 characters"),URL("Please use a valid URL")])
    name = StringField('name' ,validators=[DataRequired("cannot be empty"),Length(min=0,max=255,message="Name must be 0-255 characters")])
    type = IntegerField('price', validators=[DataRequired('cannot be empty')])
    moves = StringField('moves',validators=[is_array()])
    submit = SubmitField('submit')