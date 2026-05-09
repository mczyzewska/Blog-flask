import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask_blog.sqlite'),
    )

    from . import db
    db.init_app(app)

    from . import auth, blog, admin
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(admin.bp)

    os.makedirs(app.instance_path, exist_ok=True)

    return app
