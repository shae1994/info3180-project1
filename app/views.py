"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db
from fileinput import filename
from sqlalchemy import create_engine
from app.models import Properties
from flask import send_from_directory, render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from app.form import CreateProperty



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
@app.route('/properties/')
def properties():
    return render_template('properties.html')

@app.route('/properties/create',methods=['GET', 'POST'])
def create():
    housing= ['Single-Family', 'Multi-Family', 'Apartment', 'Townhouse', 'Mansion', 'Condo', 'Co-operative']    
    form = CreateProperty()
    if request.method == 'POST':

        if form.validate_on_submit():

            properties_db = Properties()

            properties_db.title= form.title.data
            properties_db.description=form.description.data
            properties_db.no_of_bedrooms= form.no_of_bedrooms.data
            properties_db.no_of_bathrooms = form.no_of_bathrooms.data
            properties_db.price=form.price.data
            properties_db.type= form.select.data
            properties_db.location = form.location.data

            img = form.photo.data
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            properties_db.image_name = filename

            db.session.add(properties_db)
            db.session.commit()

            flash('File Saved', 'success')

            flash_errors(form)

        return redirect(url_for('properties'))

    return render_template('form.html', housing = housing, form = form)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
