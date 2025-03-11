from mongoengine import Document, StringField,EmailField
import datetime


class Admin(Document):
    email=EmailField(required=True,unique=True)
    password=StringField(required=True)
    auth_token=StringField()

    def to_json(self):
        return{
            'email':self.email
        }
    def remove_expired_tokens(self):
        current_time = datetime.datetime.utcnow()
        valid_tokens = [token for token in self.authToken if 'exp' in token and token['exp'] > current_time]
        self.update(set__authToken=valid_tokens if valid_tokens else "")
        