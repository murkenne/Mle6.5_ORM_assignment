from flask import Blueprint, request, jsonify
from models import Member
from database import db
from schemas import member_schema, members_schema

member_bp = Blueprint('member_bp', __name__)

# Get a specific member (GET)
@member_bp.route('/<int:id>', methods=['GET'])
def get_member(id):
    member = Member.query.get_or_404(id)
    return member_schema.jsonify(member)

# Update a specific member (PUT)
@member_bp.route('/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    member = Member.query.get_or_404(id)
    try:
        member.name = data.get('name', member.name)
        member.age = data.get('age', member.age)
        member.email = data.get('email', member.email)
        member.membership_date = data.get('membership_date', member.membership_date)
        db.session.commit()
        return member_schema.jsonify(member)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Delete a specific member (DELETE)
@member_bp.route('/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    try:
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Member deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 400
