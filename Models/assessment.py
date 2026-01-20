from mongoengine import ( Document, StringField, ReferenceField, ListField, DateTimeField, IntField, BooleanField ,CASCADE, NULLIFY, EmbeddedDocument, EmbeddedDocumentField,DictField)
from datetime import datetime,timezone
from Models.course_model import Course
from Models.year_model import Year
from Models.admin_model import Admin
from Models.class_question_bank import ClassQuestionBank
from Models.university_model import University
from Models.institution_model import Institution


class AssessmentQuestion(EmbeddedDocument):
    question_id = ReferenceField(ClassQuestionBank,required=True)
    marks = IntField(default=0)
    sequence = IntField(default=0)

    def to_json(self):
        return {
            "question_id": self.question_id.to_json() if self.question_id else None,
            "marks": self.marks,
            "sequence": self.sequence
        }
        
class AssessmentSectionQuestion(EmbeddedDocument):
    section_name = StringField(required=True)
    questions = ListField(EmbeddedDocumentField(AssessmentQuestion))
    total_marks = IntField(default=0)

    def to_json(self):
        return {
            "section_name": self.section_name,
            "total_marks": self.total_marks,
            "questions": [
                q.to_json()
                for q in self.questions
            ],
        }

class Assessment(Document):
    university = ReferenceField(University, reverse_delete_rule=CASCADE)
    institution = ReferenceField(Institution, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    year = ReferenceField(Year, reverse_delete_rule=CASCADE)
    month_year = DateTimeField(required=True)
    created_by = ReferenceField(Admin,reverse_delete_rule=NULLIFY,required=True)
    sections = ListField(EmbeddedDocumentField(AssessmentSectionQuestion))
    section = StringField()
    name = StringField(required=True)
    description = StringField()
    test_type = StringField(choices=["mcq", "descriptive", "hybrid"], required=True)
    category = StringField(choices=["internal", "midterm", "final", "viva"], required=True)
    duration = IntField(required=True)
    start_time = DateTimeField(null=True)
    end_time = DateTimeField(null=True)
    offline_start_time = DateTimeField(null=True)
    offline_end_time = DateTimeField(null=True)
    log_details = ListField(DictField())
    mcq_publish_type_online = BooleanField(default=True)
    descriptive_publish_type_online = BooleanField(default=False)
    auto_result_mcq = BooleanField(default=False)
    total_marks = IntField()
    instructions = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    active = BooleanField(default=True)
    status = StringField()
    subject = ListField()
    layer1 = ListField()
    layer2 = ListField()
    layer3 = ListField()
    draft = BooleanField(default=True)
    published = BooleanField(default=False)
    evaluation = BooleanField(default=False)
    evaluation_status = StringField(default="Incomplete")
    analytics = BooleanField(default=False)
    analytics_data = DictField()
    

    

    def to_json(self):
        return {
            "id": str(self.id),
            "university": str(self.university.id) if self.university else None,
            "institution": str(self.institution.id) if self.institution else None,
            "name": self.name,
            "description": self.description,
            "month_year": self.month_year.isoformat() if self.month_year else None,
            "test_type": self.test_type,
            "category": self.category,
            "duration": self.duration,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "offline_start_time": self.offline_start_time.isoformat() if self.offline_start_time else None,
            "offline_end_time": self.offline_end_time.isoformat() if self.offline_end_time else None,
            "log_details": self.log_details if self.log_details else [],
            "mcq_publish_type_online": self.mcq_publish_type_online,
            "descriptive_publish_type_online": self.descriptive_publish_type_online,
            "auto_result_mcq": self.auto_result_mcq,
            "total_marks": self.total_marks,
            "instructions": self.instructions,
            "course": {"id": str(self.course.id), "name": self.course.name,"key":self.course.key} if self.course else {},
            "year": {"id": str(self.year.id), "name": self.year.year,"key":self.year.key} if self.year else {},
            "created_by": str(self.created_by.id) if self.created_by else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "sections": [s.to_json() for s in self.sections],
            "published": self.published,
            "section": self.section,
            "active": self.active,
            "status": self.status,
            "subject": self.subject if self.subject else [],
            "layer1": self.layer1 if self.layer1 else [],
            "layer2": self.layer2 if self.layer2 else [],
            "layer3": self.layer3 if self.layer3 else [],
            "draft": self.draft,
            "evaluation": self.evaluation,
            "analytics": self.analytics,
            "analytics_data": self.analytics_data,
            "evaluation_status": self.evaluation_status if self.evaluation_status else ""            
        }
        
    def get_all(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "month_year": self.month_year.isoformat() if self.month_year else None,
            "test_type": self.test_type,
            "category": self.category,
            "duration": self.duration,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "offline_start_time": self.offline_start_time.isoformat() if self.offline_start_time else None,
            "offline_end_time": self.offline_end_time.isoformat() if self.offline_end_time else None,
            "log_details": self.log_details if self.log_details else [],
            "mcq_publish_type_online": self.mcq_publish_type_online,
            "descriptive_publish_type_online": self.descriptive_publish_type_online,
            "auto_result_mcq": self.auto_result_mcq,
            "total_marks": self.total_marks,
            "course": {"id": str(self.course.id), "name": self.course.name,"key":self.course.key} if self.course else {},
            "year": {"id": str(self.year.id), "name": self.year.year,"key":self.year.key} if self.year else {},
            "created_by": str(self.created_by.id) if self.created_by else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "published": self.published,
            "section": self.section,
            "active": self.active,
            "status": self.status,
            "draft": self.draft,   
            "evaluation": self.evaluation,
            "analytics": self.analytics,
            "analytics_data": self.analytics_data,
            "evaluation_status": self.evaluation_status if self.evaluation_status else ""          
        }
        
        
    def to_dict(self):
        """Convert assessment to dictionary without ObjectId references"""
        data = self.to_mongo().to_dict()
        data['id'] = str(self.id)
        
        # Handle ReferenceFields
        if self.course:
            data['course'] = str(self.course.id)
        if self.year:
            data['year'] = str(self.year.id)
        if self.created_by:
            data['created_by'] = str(self.created_by.id)
        
        # Handle embedded documents
        if self.sections:
            data['sections'] = []
            for section in self.sections:
                section_dict = section.to_mongo().to_dict()
                section_dict['questions'] = [
                    {
                        'question_id': str(q.question_id.id) if q.question_id else None,
                        'marks': q.marks,
                        'sequence': q.sequence
                    }
                    for q in section.questions
                ]
                data['sections'].append(section_dict)
        
        return data
