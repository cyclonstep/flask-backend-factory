from .. import db, flask_bcrypt

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))


class roles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(512), unique=True, nullable=False)
    # password = db.Column(db.String(512))
    password_hash = db.Column(db.String(100))
    auth_id = db.Column(db.String(512), default='', nullable=True)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('roles', secondary=roles_users, 
                            backref=db.backref('users', lazy='dynamic'))
    apps = db.relationship('apps', backref='users',
                           cascade='all, delete-orphan', lazy=True)
    
    @property
    def password(self):
        raise AttributeError('password: write-only field')
    
    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)
    