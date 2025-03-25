from mongoengine import Document,ReferenceField,StringField,IntField,ListField
from Models.course_model import Course

from Models.prompt_content_model import Prompt_content
# from Models.layer2_page_model import Layer2_page



class Layer2_page(Document):
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    name = StringField(required=True)
    types = StringField(choices=['content','mcq','test_series'],required=True)
    sequence = IntField(required=True)
    hierarcy_level = IntField(default=0)
    child_pages = ListField(ReferenceField("Layer2_page", reverse_delete_rule=2, required=True))
    prompts = ListField(ReferenceField(Prompt_content,reverse_delete_rule=2,required=True))    
    
  
    def to_json(self):
        return {
            "id": str(self.id),
            'course':str(self.course.id),
            'name':str(self.name),
            'types':str(self.types),
            'sequence':str(self.sequence),
            'hierarcy_level':str(self.hierarcy_level),
            "child_pages": [child.to_json() for child in self.child_pages] if self.child_pages else [],
            "prompts": [prompt.to_json() for prompt in self.prompts] if self.prompts else None
        }
    
    def to_user(self):
        return {
            "id": str(self.id),
            'course':str(self.course.id),
            'name':str(self.name),
            'types':str(self.types),
            'sequence':str(self.sequence),
            'hierarcy_level':str(self.hierarcy_level),
            "child_pages": [child.to_user() for child in self.child_pages] if self.child_pages else [],
        }