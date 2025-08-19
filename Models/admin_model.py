from mongoengine import Document, StringField,EmailField,DateTimeField
from datetime import datetime,timezone

class Admin(Document):
    email=EmailField(required=True,unique=True)
    name = StringField(required=True)
    password=StringField(required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    auth_token=StringField()

    def to_json(self):
        return {
            'id': str(self.id),
            'email': self.email,
            'name': self.name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'auth_token': self.auth_token,
            
        }
    def remove_expired_tokens(self):
        current_time = datetime.now(timezone.utc)
        valid_tokens = [token for token in self.auth_token if 'exp' in token and token['exp'] > current_time]
        self.update(set__auth_token=valid_tokens if valid_tokens else "")


        