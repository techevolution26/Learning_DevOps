from app.db import db

class FamilyMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    tasks = db.relationship('Task', backref='family_member', lazy=True)
    
    def __repr__(self):
        return f'<FamilyMember {self.name}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date)
    family_member_id = db.Column(db.Integer, db.ForeignKey('family_member.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.description}>'

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family_member1_id = db.Column(db.Integer, db.ForeignKey('family_member.id'), nullable=False)
    family_member2_id = db.Column(db.Integer, db.ForeignKey('family_member.id'), nullable=False)
    relationship = db.Column(db.String(50))  # e.g., "parent", "sibling"

    def __repr__(self):
        return f'<Connection {self.family_member1_id} - {self.family_member2_id}>'
