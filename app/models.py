class User(UserMixin,db.Model):
    '''
    user class that creates instances of user object
    '''

    __tablename__='users'

    #create the db columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    comment = db.relationship("Comments", backref="user", lazy = "dynamic")
    vote = db.relationship("Votes", backref="user", lazy = "dynamic")

class Pitch(db.Model):
    '''
    pitch class that creates instances of the pitch object
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="pitches", lazy = "dynamic")
    vote = db.relationship("Votes", backref="pitches", lazy = "dynamic")

class Category(db.Model):
    '''
    category class that separates pitches in different ctegories
    '''
    
    __tablename__ = 'categories'

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))