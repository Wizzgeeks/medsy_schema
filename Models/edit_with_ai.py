from mongoengine import Document,BooleanField,ReferenceField,DateTimeField,ListField,DictField,CASCADE
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page
from Models.subject_page_model import Subject_page
from Models.page_content_model import PageContent
from Models.model_model import Model
from Models.admin_model import Admin
from Models.year_model import Year
from datetime import datetime,timezone


class Edit_with_ai(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=CASCADE)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=CASCADE)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=CASCADE)
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=CASCADE)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=CASCADE)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=CASCADE)
    subject_page = ReferenceField(Subject_page, reverse_delete_rule=CASCADE)
    page = ReferenceField(PageContent, reverse_delete_rule=CASCADE)
    edited_by = ReferenceField(Admin,reverse_delete_rule=CASCADE,required=True)
    model = ReferenceField(Model,reverse_delete_rule=CASCADE,required=True)
    section = ListField(DictField())
    original_content = ListField(DictField())
    content_preview = ListField(DictField())
    suggestion = ListField(DictField())
    edit_instruction = ListField(DictField())
    active = BooleanField(default=True)
    created_at=DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)

    def to_json(self):
        return {
            'id': str(self.id),
            'course': str(self.course.id),
            'year': str(self.year.id),
            'subject': str(self.subject.id) if self.subject else None,
            'layer1': str(self.layer1.id) if self.layer1 else None,
            'layer2': str(self.layer2.id) if self.layer2 else None,
            'layer3': str(self.layer3.id) if self.layer3 else None,
            'layer1_page': str(self.layer1_page.id) if self.layer1_page else None,
            'layer2_page': str(self.layer2_page.id) if self.layer2_page else None,
            'layer3_page': str(self.layer3_page.id) if self.layer3_page else None,
            'subject_page': str(self.subject_page.id) if self.subject_page else None,
            'page': str(self.page.id) if self.page else None,
            'edited_by': str(self.edited_by.id),
            'model': str(self.model.id),
            'section': self.section,
            'original_content': self.original_content,
            'content_preview': self.content_preview,
            'suggestion': self.suggestion,
            'edit_instruction': self.edit_instruction,
            'active': self.active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }

