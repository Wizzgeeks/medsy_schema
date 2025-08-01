from mongoengine import Document, ReferenceField, ListField, DictField, StringField, EmbeddedDocument, EmbeddedDocumentField,DateTimeField
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
from Models.user_model import User
from Models.prompt_content_model import Prompt_content
from datetime import datetime,timezone
from uuid import uuid4


class MCQ(EmbeddedDocument):
    id = StringField(default=lambda: str(uuid4()))
    question = StringField(required=True)
    options = DictField(required=True)
    question_type = StringField(choices=["mcq","textbasedevaluation"],required=True)
    category = StringField(choices=["direct", "critical_thinking", "reasoning", "application"],required=True)
    answer = StringField(required=True)
    explanation = StringField(required=True)
    meta_tags = DictField()

    def to_dict(self):
        return {
            "id":self.id if self.id else None,
            "question": self.question,
            "options": self.options,
            "question_type": self.question_type,
            "category": self.category,
            "answer": self.answer,
            "explanation": self.explanation,
            "meta_tags": self.meta_tags
        }


class Active_recall_mcq(Document):
    course=ReferenceField(Course,reverse_delete_rule=2,required=True)
    year=ReferenceField(Year,reverse_delete_rule=2,required=True)
    user = ReferenceField(User, reverse_delete_rule=2, required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=2)
    layer1=ReferenceField(Layer_1,reverse_delete_rule=2)
    layer2=ReferenceField(Layer_2,reverse_delete_rule=2)
    layer3=ReferenceField(Layer_3,reverse_delete_rule=2)
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=2, null=True)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=2, null=True)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=2, null=True)
    subject_page=ReferenceField(Subject_page,reverse_delete_rule=2, null=True)
    mcq=ListField(EmbeddedDocumentField(MCQ))
    created_at=DateTimeField(default=datetime.now(timezone.utc),required=True)
    updated_at=DateTimeField(null=True)
    prompt = ReferenceField(Prompt_content, reverse_delete_rule=2, required=True)


    def to_json(self):
        return {
            "id":str(self.id),
            'course':str(self.course.id),
            'user': str(self.user.id) if self.user else None,
            'year': str(self.year.id) if self.year else None,
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            "mcq": [q.to_dict() for q in self.mcq],
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page":str(self.subject_page.id) if self.subject_page else None,
            "prompt": self.prompt.to_json() if self.prompt else None,
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at)
        }
    
    def to_user(self):
        return {
            "id": str(self.id),
            'course': str(self.course.id) if self.course else None,
            'user': str(self.user.id) if self.user else None,
            'year': str(self.year.id) if self.year else None,
            "subject": str(self.subject.id) if self.subject else None,
            "layer1": str(self.layer1.id) if self.layer1 else None,
            "layer2": str(self.layer2.id) if self.layer2 else None,
            "layer3": str(self.layer3.id) if self.layer3 else None,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page":str(self.subject_page.id) if self.subject_page else None,
            "mcq": [q.to_dict() for q in self.mcq],
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at)
        }
        
    
    def to_active(self):
        return {
            "id": str(self.id),
            'course': {"name":str(self.course.name),"key":str(self.course.key)} if self.course else None,
            'user': str(self.user.username) if self.user else None,
            'year': {"name":str(self.year.year),"key":str(self.year.key)} if self.year else None,
            "subject": {"name":str(self.subject.name),"key":str(self.subject.key),"id":str(self.subject.id)} if self.subject else None,
            "layer1":{"name":str(self.layer1.name) ,"key":str(self.layer1.key),"id":str(self.layer1.id) } if self.layer1 else None,
            "layer2": {"name":str(self.layer2.name) ,"key":str(self.layer2.key),"id":str(self.layer2.id)} if self.layer2 else None,
            "layer3": {"name":str(self.layer3.name) ,"key":str(self.layer3.key),"id":str(self.layer3.id)} if self.layer3 else None,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page":str(self.subject_page.id) if self.subject_page else None,
            # "mcq": [q.to_dict() for q in self.mcq],
            'updated_at':self.updated_at.strftime("%d %b %Y") if self.updated_at else None,
            'created_at':self.created_at.strftime("%d %b %Y")
        }