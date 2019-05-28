from app import create_app, db
from flask_script import Manager, Server
from app.models import User,Pitch,Comment,Category

from flask_migrate import Migrate, MigrateCommand

# Creating app instance
#development mode
# app = create_app('development')
app = create_app('production')#We pass in the production option from our config_options dictionary. This will change our app's configurations to the ProdConfig class.


manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    '''
    Run unit tests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitch = Pitch, Comment=Comment,Category=Category)
    


if __name__ == '__main__':
    manager.run()