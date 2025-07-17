from mongoengine import Document,BooleanField,ReferenceField,DictField,ListField
from Models.page_content_model import PageContent

class Images(Document):
    page = ReferenceField(PageContent,reverse_delete_rule=2)
    images = ListField(DictField())
    active=BooleanField(default=True)

    
    def to_json(self):
        return {
            'id': str(self.id),
            "images":self.images,
            "active":self.active
        }
    