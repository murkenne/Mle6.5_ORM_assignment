from database import ma
from models import Member, WorkoutSession

# Schema for serializing Member data
class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member
        load_instance = True

# Schema for serializing WorkoutSession data
class WorkoutSessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutSession
        load_instance = True

# Single and multiple object schema instances
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
session_schema = WorkoutSessionSchema()
sessions_schema = WorkoutSessionSchema(many=True)
