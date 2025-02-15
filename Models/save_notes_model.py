from mongoengine import Document, ReferenceField, StringField,DateTimeField
from datetime import datetime
from Models.user_model import User
from Models.lesson_note_model import Lesson_note

class Saved_notes(Document):
    user = ReferenceField(User,reverse_delete_rule=2)
    Lesson_note= ReferenceField(Lesson_note,required=True,reverse_delete_rule=2)
    type = StringField(choices=['Revise Later','Important','Reference'],required=True)
    path_name=StringField()
    path_url=StringField()

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id),
            "Lesson_note":str(self.Lesson_note.id),
            "type":self.type,
            "path_name":self.path_name,
            "path_url":self.path_url,
        }

    def with_key(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "Lesson_note":self.Lesson_note.to_json() if self.Lesson_note else None,
            "type":self.type,
            "path_name":self.path_name,
            "path_url":self.path_url,
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

