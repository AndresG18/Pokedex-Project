from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired, Length,URL
class ItemForm(FlaskForm):

    happiness = IntegerField('happiness',validators=[Length(min=0,max=100 ,message='Must be betweenn 0-100')])
    imageUlr = StringField('Url', validators=[DataRequired("Must add a url"),Length(min=0,max=255,message="Url must be 0-255 characters"),URL("Please use a valid URL")])
    name = StringField('name' ,validators=[DataRequired("Must add a name"),Length(min=0,max=255,message="Name must be 0-255 characters")])
    price = IntegerField('price', validators=[DataRequired()])
    pokemonId = IntegerField('pokemonId', validators=[DataRequired()])
    submit = SubmitField('submit')
