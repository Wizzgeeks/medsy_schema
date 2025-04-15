from Models.prompt_model import Prompt
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.year_model import Year
from Models.dependent_component import Dependent_components
from mongoengine import Document,ReferenceField

class Layer1_ctc_prompt(Document):
    prompt=ReferenceField(Prompt,reverse_delete_rule=2,required=True)
    ctc = ReferenceField(Dependent_components,reverse_delete_rule=2,required=True)
    course = ReferenceField(Course,reverse_delete_rule=2,required=True)
    year = ReferenceField(Year,reverse_delete_rule=2,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=2,required=True)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=2,required=True)

    def to_json(self):
        return {
            "id":str(self.id),
            'prompt':self.prompt.to_json(),
            'ctc':self.ctc.to_json(),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'layer1':self.layer1.to_json(),
            }
    
    def to_admin(self):
        return {
            "id":str(self.id),
            'prompt':str(self.prompt.id),
            'ctc':self.ctc.to_json(),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'layer1':self.layer1.to_json(),
            }