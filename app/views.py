"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
from operator import truediv
import os
from sre_constants import SUCCESS
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
    query = Properties.query.all()
    res = [{"propertyid":i.propertyid, "title":i.title, "description":i.description,  "no_of_bedrooms":i.no_of_bedrooms,
            "no_of_bathrooms":i.no_of_bathrooms, "price":i.price,"types":i.types, "location":i.location, "image_name":i.image_name } for i in query]

    return render_template('properties.html',res=res)

@app.route('/property/<propertyid>')
def propertyDetails(propertyid):
    query = Properties.query.all()
    lst=[]
    res = [{"propertyid":i.propertyid, "title":i.title, "description":i.description,  "no_of_bedrooms":i.no_of_bedrooms,
            "no_of_bathrooms":i.no_of_bathrooms, "price":i.price,
            "types":i.types, "location":i.location, "image_name":i.image_name } for i in query]
    lst.append(propertyid)
    lst.append(query)
    return render_template('property.html', res=lst)



@app.route('/properties/create',methods=['GET', 'POST'])
def create():
    
    form = CreateProperty()
    housing= [{'types':'Single-Family'}, {'types':'Multi-Family'}, {'types':'Apartment'}, {'types':'Townhouse'}, {'types':'Mansion'}, {'types':'Condo'}, {'types':'Co-operative'}]

    if request.method == 'POST':
        if form.validate_on_submit():
            img = form.photo.data
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            
            """properties_db = Properties()
            properties_db.title= form.title.data
            properties_db.description=form.description.data
            properties_db.no_of_bedrooms= form.no_of_bedrooms.data
            properties_db.no_of_bathrooms = form.no_of_bathrooms.data
            properties_db.price=form.price.data
            properties_db.type= request.form['types']
            properties_db.location = form.location.data"""

            t= request.form['title']
            d=request.form['description']
            be=request.form['no_of_bedrooms']
            ba = request.form['no_of_bedrooms']
            p= request.form['price']
            ty= request.form['types']
            l= request.form['location']
            
            properties_db = Properties(t,d,be,ba,ty,p,l, filename)

             

            db.session.add(properties_db)
            db.session.commit()
            flash('Property Added', SUCCESS)
            flash_errors(form)
        return redirect(url_for('properties'))
    return render_template('form.html', form = form, housing = housing, types='types')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


def get_uploaded_images():
    uploads='/uploads'
    typelist=[]
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir + uploads):
        for file in files:
            if file.endswith(('.jpg', '.png', '.jpeg','.JPEG', '.PNG', '.JPG')):
                typelist.append(file)
    return typelist

@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)


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
