from mongoengine import Document, ReferenceField, StringField, DateTimeField,CASCADE
from datetime import datetime,timezone
from Models.user_model import User

class Self_note(Document):
    user = ReferenceField(User, reverse_delete_rule=CASCADE,required=True)
    title = StringField(required=True)
    notes_content = StringField(required=True)
    date = DateTimeField(required=True, default=datetime.utcnow )
    path=StringField()



    
    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id),
            "title": self.title,
            "notes_content": self.notes_content,
            "date": self.date.strftime("%d %b %Y"),
            "path":self.path
        }

    def with_key(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "title": self.title,
            "notes_content": self.notes_content,
            "date": self.date.strftime("%d %b %Y"),
            "path":self.path
        }

    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
