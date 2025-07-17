from mongoengine import Document,BooleanField,ReferenceField,DictField,ListField,StringField
from Models.page_content_model import PageContent

class Images(Document):
    page = ReferenceField(PageContent,reverse_delete_rule=2)
    images = ListField(DictField())
    query= StringField()
    active=BooleanField(default=True)

    
    def to_json(self):
        return {
            'id': str(self.id),
            "page":self.page if self.page else None,
            "query":self.query if self.query else "",
            "images":self.images if self.images else [],
            "active":self.active
        }
    