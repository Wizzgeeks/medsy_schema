from mongoengine import Document,ReferenceField,DictField,ListField,StringField
from Models.course_model import Course
from Models.model_model import Model

class Prompt_content(Document):
    name = StringField(required=True)
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    system_content = StringField(required=True)
    framework = ListField(DictField())
    model = ReferenceField(Model,reverse_delete_rule=2,required=True)

  
    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            'course':str(self.course.id),
            'system_content':self.system_content,
            'framework':self.framework,
            'model':str(self.model.id)
        }
