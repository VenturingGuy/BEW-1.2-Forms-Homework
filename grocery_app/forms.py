from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import ItemCategory, GroceryStore

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField('Store Title', validators=[DataRequired(), Length(min=5, max=80)])
    address = StringField('Store Address', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Grocery Item', validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField('Item Price', validators=[DataRequired()])
    category = SelectField('Item Category', choices=ItemCategory.choices())
    photo_url = StringField('Item Photo', validators=[URL(require_tld=True)])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')
