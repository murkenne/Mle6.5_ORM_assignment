from flask import Blueprint, request, jsonify
from models import WorkoutSession
from database import db
from schemas import session_schema, sessions_schema

session_bp = Blueprint('session_bp', __name__)

# Add a new workout session (POST)
@session_bp.route('/', methods=['POST'])
def add_workout_session():
    data = request.json
    try:
        new_session = WorkoutSession(
            workout_type=data['workout_type'],
            date=data['date'],
            duration=data['duration'],
            member_id=data['member_id']
        )
        db.session.add(new_session)
        db.session.commit()
        return session_schema.jsonify(new_session), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Get all workout sessions for a specific member (GET)
@session_bp.route('/<int:member_id>', methods=['GET'])
def get_workout_sessions(member_id):
    sessions = WorkoutSession.query.filter_by(member_id=member_id).all()
    return sessions_schema.jsonify(sessions)

# Update a workout session (PUT)
@session_bp.route('/<int:id>', methods=['PUT'])
def update_workout_session(id):
    data = request.json
    session = WorkoutSession.query.get_or_404(id)
    try:
        session.workout_type = data.get('workout_type', session.workout_type)
        session.date = data.get('date', session.date)
        session.duration = data.get('duration', session.duration)
        db.session.commit()
        return session_schema.jsonify(session)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


