from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField,CASCADE
from Models.job_detail import Job_detail
from Models.course_model import Course
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3
from Models.year_model import Year
from datetime import datetime,timezone

class Layer3_page_creation_job(Document):
    job_id=ReferenceField(Job_detail,reverse_delete_rule=CASCADE,required=True)
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = ReferenceField(Year,reverse_delete_rule=CASCADE,required=True)
    subject = ReferenceField(Subject,reverse_delete_rule=CASCADE,required=True)
    layer1 = ReferenceField(Layer_1,reverse_delete_rule=CASCADE)
    layer2 = ReferenceField(Layer_2,reverse_delete_rule=CASCADE,required=True)
    layer3 = ReferenceField(Layer_3,reverse_delete_rule=CASCADE,required=True)
    logs=ListField(DictField())
    conversation = ListField(default=[])
    created_at=DateTimeField(default=datetime.now(timezone.utc),required=True)
    updated_at = DateTimeField(null=True)
    status=StringField()
    neo4j_book = ListField(StringField())
    book_s3_url = ListField(StringField())
    

    def to_json(self):
        return {
            "id":str(self.id),
            'job_id':self.job_id.to_json(),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id),
            'layer3':self.layer3.to_json(),
            'status':self.status,
            'logs':self.logs,
            'conversation':self.conversation if self.conversation else [],
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at),
            'neo4j_book':self.neo4j_book if self.neo4j_book else [],
            'book_s3_url':self.book_s3_url if self.book_s3_url else [],
            }
    
    def to_admin(self):
        return {
            "id":str(self.id),
            'job_id':str(self.job_id.id),
            'course':str(self.course.id),
            'year':str(self.year.id),
            'subject':str(self.subject.id),
            'layer1':str(self.layer1.id) if self.layer1 else None,
            'layer2':str(self.layer2.id),
            'layer3':self.layer3.to_json(),
            'status':self.status,
            'logs':self.logs,
            'conversation':self.conversation if self.conversation else [],
            'updated_at':str(self.updated_at) if self.updated_at else None,
            'created_at':str(self.created_at),
            'neo4j_book':self.neo4j_book if self.neo4j_book else [],
            'book_s3_url':self.book_s3_url if self.book_s3_url else [],
            }