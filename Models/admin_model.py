from mongoengine import Document, StringField,EmailField
from datetime import datetime,timezone


class Admin(Document):
    email=EmailField(required=True,unique=True)
    name = StringField(required=True)
    password=StringField(required=True)
    auth_token=StringField()

    def to_json(self):
        return{
            'id':str(self.id),
            'email':self.email,
            'name':self.name
        }
    def remove_expired_tokens(self):
        current_time = datetime.now()
        valid_tokens = [token for token in self.authToken if 'exp' in token and token['exp'] > current_time]
        self.update(set__authToken=valid_tokens if valid_tokens else "")
        