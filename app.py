from flask import Flask
from database import db, ma
from routes.member_routes import member_bp
from routes.session_routes import session_bp

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Tekking58!@127.0.0.1/fitness_center_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow
db.init_app(app)
ma.init_app(app)

# Register the blueprints for members and workout sessions
app.register_blueprint(member_bp, url_prefix='/members')
app.register_blueprint(session_bp, url_prefix='/workout_sessions')

# Welcome route for the root URL
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the Fitness Center Database", 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
