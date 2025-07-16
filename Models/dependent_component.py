from mongoengine import Document,BooleanField,StringField
from Models.prompt_model import Prompt

class Dependent_components(Document):
    name=StringField()
    types=StringField(required=True,unique=True)
    active=BooleanField(default=False)

    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    
    def to_json(self):
        return {
            'id': str(self.id),
            "name":self.name,
            "types":self.types,
            "active":self.active
        }
    