from flask import Flask, render_template, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.validators import ValidationError

class Companyform(FlaskForm):

    companyname = StringField('Company Name', validators=[DataRequired()])
    country = SelectField('pick country:', choices=['United States', 'India', 'Singapore', 'Europe', 'Thailand', 'Padova'])
    category = SelectField('Category', choices=[ 'Automotiv', 'Arts&crafts', 'Apparel&Fashion', 'Airlines', 'Accounting'])
    submit = SubmitField('Enter')

class employeeform(FlaskForm):

    empname = StringField('username', validators=[DataRequired()])
    empdesign = StringField('username', validators=[DataRequired()])    
    submit = SubmitField('Enter')

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route("/") 
def home():
    return render_template("home.html")


@app.route("/companyinfo", methods=['GET', 'POST'])
def companyinfo():
    form = Companyform()
    if form.validate_on_submit():
        session['companyname'] = form.companyname.data
        session['country'] = form.country.data
        session['category'] = form.category.data

    return render_template('companyinfo.html', form = form)

@app.route("/employeeinfo", methods=['GET', 'POST'])   
def employeeinfo():
    form = employeeform()
    if form.validate_on_submit():
        empname = form.empname.data
        empdesign = form.empdesign.data

    return render_template('empinfo.html', form = form)

if __name__ == "__main__":
    app.run(debug=True)
