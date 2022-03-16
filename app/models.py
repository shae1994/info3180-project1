from . import db
from werkzeug.security import generate_password_hash


class Properties(db.Model):
    __tablename__ = 'properties'

    propertyid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(180))
    no_of_bedrooms = db.Column(db.String(10), unique=True)
    no_of_bathrooms = db.Column(db.String(10))
    type = db.Column(db.String(25))
    price = db.Column(db.String(25))
    location = db.Column(db.String(50))

    def __init__(self, propertyid, title,description,no_of_bedrooms,no_of_bathrooms,type,price, location ):
        self.propertyid = propertyid
        self.title = title
        self.description=description
        self.no_of_bedrooms=no_of_bedrooms
        self.no_of_bathrooms= no_of_bathrooms
        self.type = type
        self.price = price
        self.location= location


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)