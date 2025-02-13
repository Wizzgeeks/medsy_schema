from mongoengine import Document, ReferenceField, StringField,DateTimeField
from datetime import datetime
from Models.user_model import User
from Models.lesson_note_model import Lesson_note

class Saved_notes(Document):
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    Lesson_note= ReferenceField(Lesson_note,required=True,reverse_delete_rule=2)
    type = StringField(choices=['Revise Later','Important','Reference'],required=True)

    
    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id),
            "lesson":str(self.lesson.id),
            "type":self.type
        }

    def with_key(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "lesson":self.lesson.to_json() if self.lesson else None,
            "type":self.type
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

