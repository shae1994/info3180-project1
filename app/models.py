from email.mime import image
from . import db


class Properties(db.Model):
    __tablename__ = "Properties"
    propertyid      = db.Column(db.Integer, primary_key=True, autoincrement= True)
    title           = db.Column(db.String(75), unique = True)
    description     = db.Column(db.String(350))
    no_of_bedrooms  = db.Column(db.Integer)
    no_of_bathrooms = db.Column(db.String(10))
    types            = db.Column(db.String(25))
    prices           = db.Column(db.String(35))
    location        = db.Column(db.String(50))
    image_name      = db.Column(db.String(50))

    def __init__(self, title,description,no_of_bedrooms,no_of_bathrooms,types,prices, location, image_name ):
        self.title = title
        self.description=description
        self.no_of_bedrooms=no_of_bedrooms
        self.no_of_bathrooms= no_of_bathrooms
        self.types = types
        self.prices = prices
        self.location= location
        self.image_name= image_name



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