
# import statement for CSRF
import os
from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .routes import items, pokemon
from .config import Configuration
from .models import db


app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)
app.register_blueprint(items.bp)
app.register_blueprint(pokemon.bp)

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
