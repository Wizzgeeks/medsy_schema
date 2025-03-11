from mongoengine import Document,StringField,ReferenceField,DateTimeField
from Models.admin_model import Admin
from datetime import datetime
class Blog(Document):
    admin = ReferenceField(Admin,required=True,reverse_delete_rule=2)
    blog_image_url=StringField()
    blog_title=StringField()
    blog_description=StringField()
    created_at = DateTimeField(default=datetime.utcnow)

    def to_json(self):
        return {
            "blog_title":self.blog_title,
            "created_at": self.created_at.strftime("%d %b %Y"),
            "blog_description":self.blog_description,
            "blog_image_url":self.blog_image_url
        }
