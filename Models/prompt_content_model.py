from mongoengine import Document,ReferenceField,DictField,ListField,StringField,BooleanField,CASCADE
from Models.course_model import Course
from Models.model_model import Model

class Prompt_content(Document):
    name = StringField(required=True)
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    system_content = StringField(required=True)
    framework = ListField(DictField())
    model = ReferenceField(Model,reverse_delete_rule=CASCADE,required=True)
    deep_dive = StringField()
    summarize = StringField()
    json_schema=StringField()
    json_mode = BooleanField(default=False)
    thinking_mode = BooleanField(default=False)

  
    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            'course':str(self.course.id),
            'system_content':self.system_content,
            'framework':self.framework,
            'model':str(self.model.id),
            'deep_dive':self.deep_dive if self.deep_dive else None,
            'summarize':self.summarize if self.summarize else None,
            'json_schema':self.json_schema,
            'json_mode':self.json_mode if self.json_mode else False,
            'thinking_mode':self.thinking_mode if self.thinking_mode else False,
        }
