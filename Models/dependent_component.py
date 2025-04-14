from mongoengine import Document,ReferenceField,StringField
from Models.prompt_model import Prompt

class Dependent_components(Document):
    name=StringField()
    prompt=ReferenceField(Prompt,required=True,reverse_delete_rule=2)
    types=StringField(required=True)

    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    
    def to_json(self):
        return {
            "name":self.name,
            "prompt":str(self.prompt.id),
            "types":self.types
        }
    