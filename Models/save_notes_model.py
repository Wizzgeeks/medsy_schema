from mongoengine import Document, ReferenceField, StringField,DateTimeField,ValidationError,ListField,DictField
from datetime import datetime
from Models.user_model import User
from Models.lesson_note_model import Lesson_note

class Saved_notes(Document):
    user = ReferenceField(User,reverse_delete_rule=2)
    Lesson_note= ReferenceField(Lesson_note,required=True,reverse_delete_rule=2)
    type = StringField(choices=['RevisedLater','Important','Reference','Snapshot'],required=True)
    path_name=StringField()
    path_url=StringField()
    content=StringField()
    date = DateTimeField(required=True, default=datetime.now)

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id),
            "Lesson_note":str(self.Lesson_note.id),
            "type":self.type,
            "path_name":self.path_name,
            "path_url":self.path_url,
            "date": self.date.strftime("%d %b %Y"),
            "content":self.content,
            "notes":""
        }
    
    def clean(self):
        if self.type == 'Snapshot':
            if not self.content:
                raise ValidationError("Content is required for  Snapshot")

    def with_key(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "Lesson_note":self.Lesson_note.to_json() if self.Lesson_note else None,
            "type":self.type,
            "path_name":self.path_name,
            "path_url":self.path_url,
            "date": self.date.strftime("%d %b %Y"),
            "content":self.content
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

