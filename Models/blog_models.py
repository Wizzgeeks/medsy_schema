from mongoengine import Document,StringField,ReferenceField,DateTimeField,BooleanField,CASCADE
from Models.admin_model import Admin
from datetime import datetime,timezone
class Blog(Document):
    admin = ReferenceField(Admin,reverse_delete_rule=CASCADE,required=True)
    blog_image_url=StringField()
    blog_title=StringField()
    blog_description=StringField()
    description=StringField()
    blog_category=StringField(choices=['blog','announcements','article'],required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    file_name=StringField()
    publish=BooleanField(default=False)

    def to_json(self):
        return {
            "id":str(self.id),
            "blog_title":self.blog_title,
            "created_at": self.created_at.strftime("%d %B %Y"),
            "blog_description":self.blog_description,
            "blog_image_url":self.blog_image_url,
            "description":self.description,
            "blog_category":self.blog_category,
            "file_name":self.file_name,
            "publish":self.publish if self.publish else False,
        }
