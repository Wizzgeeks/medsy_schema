from mongoengine import Document,ReferenceField,DateTimeField,DictField,ListField,CASCADE
from Models.course_model import Course
from datetime import datetime,timezone
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.subject_model import Subject
from Models.year_model import Year
from Models.page_content_model import PageContent

class Mastery_components(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    page = ReferenceField(PageContent,reverse_delete_rule=CASCADE,required=True)
    layer1 = ReferenceField(Layer_1, reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2, reverse_delete_rule=CASCADE)
    layer3 = ReferenceField(Layer_3, reverse_delete_rule=CASCADE)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE, null=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    ctc_count=DictField(default={"image":0,"video":0,"conversation":0,
                                 "fillups":0,"justify":0,"mcq":0,"trueorfalse":0,
                                 "assertion_reasoning":0,"match":0,
                                 "relatedQuestions":0,"predictandprevent":0,
                                 "amazing_fact":0})
    ctc_index = ListField(DictField())
    updated_at = DateTimeField(null=True)
    

    def to_json(self):
        return {
            'id': str(self.id),
            'course': self.course.key if self.course else None,
            'year': self.year.key if self.year else None,
            'page': str(self.page.id) if self.page else None,
            'layer1': self.layer1.key if self.layer1 else None,
            'layer2': self.layer2.key if self.layer2 else None,
            'layer3': self.layer3.key if self.layer3 else None,
            'subject': self.subject.key if self.subject else None,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at) if self.updated_at else None,
            'ctc_count': self.ctc_count,
            'ctc_index': self.ctc_index if self.ctc_index else None,
        }
