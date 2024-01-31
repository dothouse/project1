from flask import Flask

### sql 부분
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    ### sql 부분
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # blueprint
    from .views import main_views, select1_views, select2_views, select3_views
    from .views import select_tour_views, select_pension_views, info_views, weather_views
    # filter
    from .filter import thousand_comma
    app.jinja_env.filters['t_comma'] = thousand_comma

    app.register_blueprint(main_views.bp)

    app.register_blueprint(select1_views.bp)
    app.register_blueprint(select2_views.bp)
    app.register_blueprint(select3_views.bp)

    app.register_blueprint(select_tour_views.bp)
    app.register_blueprint(select_pension_views.bp)
    app.register_blueprint(info_views.bp)
    app.register_blueprint(weather_views.bp)

    return app
