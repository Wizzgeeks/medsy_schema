from datetime import datetime,timezone
from mongoengine import Document, ReferenceField, StringField,DateTimeField,ValidationError,IntField
from Models.user_model import User
from Models.lesson_note_model import Lesson_note
from Models.page_content_model import PageContent

class Saved_notes(Document):
    user = ReferenceField(User,reverse_delete_rule=2)
    page= ReferenceField(PageContent,required=True,reverse_delete_rule=2)
    type = StringField(choices=['RevisedLater','Important','Reference','Snapshot'],required=True)
    path_name=StringField()
    path_url=StringField()
    content=IntField()
    date = DateTimeField(required=True, default=datetime.now())

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id),
            "page":str(self.page.id),
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

