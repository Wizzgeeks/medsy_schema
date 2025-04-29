from mongoengine import Document,ReferenceField,DictField,StringField,BooleanField
from Models.course_model import Course
from Models.model_model import Model
from Models.year_model import Year


class Prompt(Document):
    course = ReferenceField(Course,reverse_delete_rule=2)
    model = ReferenceField(Model,required=True,reverse_delete_rule=2)
    year = ReferenceField(Year,reverse_delete_rule=2)
    types=StringField(required=True)
    prompt_framework = DictField(required=True)
    name=StringField(default='CTC Prompt')
    default=BooleanField(default=False)


    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "model":str(self.model.id) if self.model else None,
            "year":str(self.year.id) if self.year else None,
            "types":self.types,
            "prompt_framework":self.prompt_framework,
            "name":self.name,
            "default":self.default
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "model":self.model.to_json() if self.model else None,
            "year":self.year.to_json() if self.year else None,
            "types":self.types,
            "prompt_framework":self.prompt_framework,
            "name":self.name,
            "default":self.default
        }
        