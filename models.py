from database import db

# Member model matching the existing Members table
class Member(db.Model):
    __tablename__ = 'Members'  # Match the manual table name
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    membership_type = db.Column(db.String(100))

    # Relationship with WorkoutSession (one-to-many)
    workout_sessions = db.relationship('WorkoutSession', backref='member', lazy=True)

# WorkoutSession model matching the existing WorkoutSessions table
class WorkoutSession(db.Model):
    __tablename__ = 'WorkoutSessions'  # Match the manual table name
    session_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('Members.id'), nullable=False)
    session_date = db.Column(db.Date, nullable=False)
    session_time = db.Column(db.String(255))
    activity = db.Column(db.String(255))

