from mongoengine  import Document,ReferenceField,ListField,DictField,EmbeddedDocument,EmbeddedDocumentField,StringField,CASCADE
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page
from Models.subject_page_model import Subject_page
from Models.year_model import Year
from Models.prompt_content_model import Prompt_content

class Exam(EmbeddedDocument):
    question=StringField(required=True)
    options = DictField()
    question_type = StringField(choices=["mcq","textbasedevaluation"])
    category = StringField()
    answer = StringField()
    explanation = StringField()
    meta_tags = DictField()
    
    def to_dict(self):
        return {
            "question": self.question,
            "options": self.options,
            "question_type": self.question_type,
            "category": self.category,
            "answer": self.answer,
            "explanation": self.explanation,
            "meta_tags": self.meta_tags
        }

class Exam_page(Document):
    course=ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year=ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE)
    layer1=ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2=ReferenceField(Layer_2,reverse_delete_rule=CASCADE)
    layer3=ReferenceField(Layer_3,reverse_delete_rule=CASCADE)
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=CASCADE, null=True)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=CASCADE, null=True)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=CASCADE, null=True)
    subject_page=ReferenceField(Subject_page,reverse_delete_rule=CASCADE, null=True)
    exam=ListField(EmbeddedDocumentField(Exam))
    prompt = ReferenceField(Prompt_content, reverse_delete_rule=CASCADE, required=True)


    def to_json(self):
        return {
            "id":str(self.id),
            'course':str(self.course.id),
            'year': str(self.year.id) if self.year else None,
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            'exam':[s.to_dict() for s in self.exam],
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page":str(self.subject_page.id) if self.subject_page else None,
            "prompt": self.prompt.to_json() if self.prompt else None
        }
    
    def to_user(self):
        return {
            "id": str(self.id),
            'course': str(self.course.id) if self.course else None,
            'year': str(self.year.id) if self.year else None,
            "subject": str(self.subject.id) if self.subject else None,
            "layer1": str(self.layer1.id) if self.layer1 else None,
            "layer2": str(self.layer2.id) if self.layer2 else None,
            "layer3": str(self.layer3.id) if self.layer3 else None,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page":str(self.subject_page.id) if self.subject_page else None,
            'exam':[s.to_dict() for s in self.exam],
        }