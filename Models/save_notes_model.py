from datetime import datetime,timezone
from mongoengine import Document, ReferenceField, StringField,DateTimeField,ValidationError,IntField,CASCADE
from Models.user_model import User
from Models.lesson_note_model import Lesson_note
from Models.page_content_model import PageContent

class Saved_notes(Document):
    user = ReferenceField(User,reverse_delete_rule=CASCADE)
    page= ReferenceField(PageContent,reverse_delete_rule=CASCADE,required=True)
    type = StringField(choices=['RevisedLater','Important','Reference','Snapshot'],required=True)
    path_name=StringField()
    path_url=StringField()
    content=IntField()
    index = IntField(default=0)
    date = DateTimeField(required=True, default=datetime.now(timezone.utc))

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
            "notes":"",
            "index":self.index if self.index else 0

        }
    
    # def clean(self):
    #     if self.type == 'Snapshot':
    #         if not self.content:
    #             raise ValidationError("Content is required for  Snapshot")

    def with_key(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "Lesson_note":self.Lesson_note.to_json() if self.Lesson_note else None,
            "type":self.type,
            "path_name":self.path_name,
            "path_url":self.path_url,
            "date": self.date.strftime("%d %b %Y"),
            "content":self.content,
            "index":self.index if self.index else 0

        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

