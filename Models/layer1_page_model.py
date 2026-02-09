from mongoengine import Document,ReferenceField,StringField,IntField,ListField,BooleanField,CASCADE
from Models.course_model import Course

from Models.prompt_content_model import Prompt_content
# from Models.layer1_page_model import Layer1_page


class Layer1_page(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    name = StringField(required=True)
    types = StringField(choices=['content','mcq','test_series','exam','adaptive_learning','adaptive_learning_mcq','adaptive_learning_content',"related_videos","active_recall","active_recall_mcq","active_recall_content","crossword_puzzle"],required=True)
    sequence = IntField(required=True)
    hierarcy_level = IntField(default=0)
    enable_days = IntField(default=0)
    child_pages = ListField(ReferenceField("Layer1_page", reverse_delete_rule=CASCADE, required=True))
    prompts = ListField(ReferenceField(Prompt_content,reverse_delete_rule=CASCADE,required=True))  
    optional=BooleanField(default=False)
    ignore=BooleanField(default=False)
    min_page=IntField(default=0)
    parent = BooleanField(default=False)
 

   
  
    def to_json(self):
        return {
            "id": str(self.id),
            'course': str(self.course.id),
            'name': self.name,
            'types': self.types,
            'sequence': self.sequence,
            'hierarcy_level': self.hierarcy_level,
            'enable_days': self.enable_days if self.enable_days else 0,
            "child_pages": [child.to_json() for child in self.child_pages] if self.child_pages else [],
            "prompts": [prompt.to_json() for prompt in self.prompts] if self.prompts else None,
            "optional": self.optional,
            "ignore": self.ignore,
            "min_page": self.min_page if self.min_page else 0,
            "parent": self.parent
        }
    
    def to_user(self):
        return {
            "id": str(self.id),
            'course': str(self.course.id),
            'name': self.name,
            'types': self.types,
            'sequence': self.sequence,
            'enable_days': self.enable_days if self.enable_days else 0,
            'hierarcy_level': self.hierarcy_level,
            "child_pages": [child.to_user() for child in self.child_pages] if self.child_pages else [],
            "optional": self.optional,
            "ignore": self.ignore,
            "min_page": self.min_page if self.min_page else 0,
            "parent": self.parent            
        }
    
    def to_admin(self):
        return {
            "id": str(self.id),
            'course': str(self.course.id),
            'name': self.name,
            'types': self.types,
            'sequence': self.sequence,
            'hierarcy_level': self.hierarcy_level,
            'enable_days': self.enable_days if self.enable_days else 0,
            "child_pages": [child.to_admin() for child in self.child_pages] if self.child_pages else [],
            "prompts": [str(prompt.id) for prompt in self.prompts] if self.prompts else None,
            "optional": self.optional,
            "ignore": self.ignore,
            "min_page": self.min_page if self.min_page else 0,
            "parent": self.parent
        }

