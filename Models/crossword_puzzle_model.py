from mongoengine import Document, ReferenceField,BooleanField,ListField,CASCADE,DictField,StringField
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


class CrosswordPuzzle(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    year = ReferenceField(Year, reverse_delete_rule=CASCADE, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE, required=True)
    layer1 = ReferenceField(Layer_1, reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2, reverse_delete_rule=CASCADE)
    layer3 = ReferenceField(Layer_3, reverse_delete_rule=CASCADE)
    layer1_page = ReferenceField(Layer1_page, reverse_delete_rule=CASCADE, null=True)
    layer2_page = ReferenceField(Layer2_page, reverse_delete_rule=CASCADE, null=True)
    layer3_page = ReferenceField(Layer3_page, reverse_delete_rule=CASCADE, null=True)
    subject_page= ReferenceField(Subject_page, reverse_delete_rule=CASCADE, null=True)
    content = ListField()
    prompt = ReferenceField(Prompt_content, reverse_delete_rule=CASCADE, null=True)
    published = BooleanField(default=True)
    isintegrated = BooleanField(default=False)
    related_contents = ListField(DictField())
    instruction = StringField()
    ignore=BooleanField(default=False)
    extra_meta = DictField()

    def to_json(self):
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
            "subject_page": str(self.subject_page.id) if self.subject_page else None,
            "content": self.content,
            "prompt": self.prompt.to_json() if self.prompt else None,
            "instruction": self.instruction,
            "related_contents": self.related_contents,
            "published": self.published if self.published else False,
            "ignore":self.ignore if self.ignore else False,
            "isintegrated": self.isintegrated if self.isintegrated else False,
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
            "layer1_page": {"id":str(self.layer1_page.id),"name":self.layer1_page.name} if self.layer1_page else None,
            "layer2_page": {"id":str(self.layer2_page.id),"name":self.layer2_page.name} if self.layer2_page else None,
            "layer3_page": {"id":str(self.layer3_page.id),"name":self.layer3_page.name} if self.layer3_page else None,
            "subject_page": {"id":str(self.subject_page.id),"name":self.subject_page.name} if self.subject_page else None,
            "content": self.content,
            "ignore":self.ignore if self.ignore else False,
            "published": self.published if self.published else False,
            "isintegrated": self.isintegrated if self.isintegrated else False,
            "related_contents": self.related_contents,
            "instruction": self.instruction,
            
        }
