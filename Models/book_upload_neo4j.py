from mongoengine import Document,StringField,ReferenceField,DateTimeField,BooleanField,CASCADE
from Models.admin_model import Admin
from Models.course_model import Course
from datetime import datetime,timezone
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year

class Book_upload(Document):
    course=ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year=ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE)
    layer1=ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2=ReferenceField(Layer_2,reverse_delete_rule=CASCADE)
    layer3=ReferenceField(Layer_3,reverse_delete_rule=CASCADE)
    uploaded_by=ReferenceField(Admin,reverse_delete_rule=CASCADE,required=True)
    uploaded_at = DateTimeField(default=datetime.now(timezone.utc))
    layer=StringField(choices=['subject','layer1','layer2','layer3'],required=True)
    book_name =StringField(required=True)
    book_url_s3 =StringField(required=True)
    neo4j_id = StringField(required=True)
    active=BooleanField(default=True)
    
    
    

    def to_json(self):
        return {
            'id': str(self.id),
            'course': str(self.course.id) if self.course else None,
            'year': str(self.year.id) if self.year else None,
            'subject': str(self.subject.id) if self.subject else None,
            'layer1': str(self.layer1.id) if self.layer1 else None,
            'layer2': str(self.layer2.id) if self.layer2 else None,
            'layer3': str(self.layer3.id) if self.layer3 else None,
            'uploaded_by': str(self.uploaded_by.id) if self.uploaded_by else None,
            'uploaded_at': self.uploaded_at.isoformat() if self.uploaded_at else None,
            'layer': self.layer,
            'book_name': self.book_name,
            'book_url_s3': self.book_url_s3,
            'neo4j_id': self.neo4j_id,
            'active': self.active,
        }

    def to_json_expand(self):
        return {
            'id': str(self.id),
            'course': self.course.to_json() if self.course else None,
            'year': self.year.to_json() if self.year else None,
            'subject': self.subject.to_json() if self.subject else None,
            'layer1': self.layer1.to_json() if self.layer1 else None,
            'layer2': self.layer2.to_json() if self.layer2 else None,
            'layer3': self.layer3.to_json() if self.layer3 else None,
            'uploaded_by': self.uploaded_by.to_json() if self.uploaded_by else None,
            'uploaded_at': self.uploaded_at.isoformat() if self.uploaded_at else None,
            'layer': self.layer,
            'book_name': self.book_name,
            'book_url_s3': self.book_url_s3,
            'neo4j_id': self.neo4j_id,
            'active': self.active,
        }
