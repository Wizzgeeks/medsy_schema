from mongoengine import Document,ReferenceField,DictField,StringField,BooleanField,CASCADE
from Models.course_model import Course
from Models.model_model import Model
from Models.year_model import Year


class Prompt(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE)
    model = ReferenceField(Model,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE)
    types=StringField(required=True)
    prompt_framework = DictField(required=True)
    name=StringField(default='CTC Prompt')
    default=BooleanField(default=False)
    json_schema=StringField()
    json_mode = BooleanField(default=False)
    thinking_mode = BooleanField(default=False)


    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "model":str(self.model.id) if self.model else None,
            "year":str(self.year.id) if self.year else None,
            "types":self.types,
            "prompt_framework":self.prompt_framework,
            "name":self.name,
            "default":self.default,
            'json_schema':self.json_schema if self.json_schema else None,
            'json_mode':self.json_mode if self.json_mode else False,
            'thinking_mode':self.thinking_mode if self.thinking_mode else False,
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
            "default":self.default,
            'json_schema':self.json_schema if self.json_schema else None,
            'json_mode':self.json_mode if self.json_mode else False,
            'thinking_mode':self.thinking_mode if self.thinking_mode else False,
        }
        