from mongoengine import Document, ReferenceField, ListField, DictField,BooleanField,DateTimeField,CASCADE
from datetime import datetime,timezone
from Models.course_model import Course
from Models.year_model import Year
from Models.user_model import User
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.layer1_page_model import Layer1_page
from Models.layer2_page_model import Layer2_page
from Models.layer3_page_model import Layer3_page
from Models.subject_page_model import Subject_page
from Models.crossword_puzzle_model import CrosswordPuzzle



class CrosswordPuzzleResult(Document):
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
    user=ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    crossword_puzzle=ReferenceField(CrosswordPuzzle,reverse_delete_rule=CASCADE,required=True)
    attempted_data=ListField(DictField())
    completed = BooleanField(default=True)
    ignore = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(null=True)
    
    def to_json(self):
        return {
            "id":str(self.id),
            'course':str(self.course.id),
            'year': str(self.year.id) if self.year else None,
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id) if self.layer2 else None,
            'layer3':str(self.layer3.id) if self.layer3 else None,
            'user':str(self.user.id) if self.user.id else None,
            'crossword_puzzle':str(self.crossword_puzzle.id) if self.crossword_puzzle.id else None,
            'attempts_data':self.attempted_data,
            "layer1_page": str(self.layer1_page.id) if self.layer1_page else None,
            "layer2_page": str(self.layer2_page.id) if self.layer2_page else None,
            "layer3_page": str(self.layer3_page.id) if self.layer3_page else None,
            "subject_page": str(self.subject_page.id) if self.subject_page else None,
            "completed": self.completed,
            "ignore": self.ignore,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at) if self.updated_at else None,
        }
