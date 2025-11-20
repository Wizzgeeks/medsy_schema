from mongoengine import ( Document, StringField, ReferenceField, ListField, DateTimeField, IntField, BooleanField ,CASCADE, EmbeddedDocument, EmbeddedDocumentField)
from datetime import datetime,timezone
from Models.course_model import Course
from Models.year_model import Year
from Models.admin_model import Admin
from Models.class_question_bank import ClassQuestionBank


class AssessmentSubQuestion(EmbeddedDocument):
    sub_question_id = ReferenceField(ClassQuestionBank,required=True,reversedelete_rule=CASCADE)
    marks = IntField(default=0)

    def to_json(self):
        return {
            "sub_question_id": self.sub_question_id.to_json() if self.sub_question_id else None,
            "marks": self.marks,
        }


class AssessmentQuestion(EmbeddedDocument):
    question_id = ReferenceField(ClassQuestionBank,required=True,reversedelete_rule=CASCADE)
    marks = IntField(default=0)
    sub_questions = ListField(EmbeddedDocumentField(AssessmentSubQuestion))

    def to_json(self):
        return {
            "question_id": self.question_id.to_json() if self.question_id else None,
            "marks": self.marks,
            "sub_questions": [
                sq.to_json()
                for sq in self.sub_questions
            ],
        }

class Assessment(Document):
    course = ReferenceField(Course, reversedelete_rule=CASCADE)
    year = ReferenceField(Year, reversedelete_rule=CASCADE)
    month_year = DateTimeField(required=True)
    created_by = ReferenceField(Admin, required=True, reversedelete_rule=CASCADE)
    questions = ListField(EmbeddedDocumentField(AssessmentQuestion))
    section = StringField()
    name = StringField(required=True)
    description = StringField()
    test_type = StringField(choices=["mcq", "qa", "hybrid"], required=True)
    category = StringField(choices=["internal", "midterm", "final", "viva",""], required=True)
    duration = IntField(required=True)
    start_time = DateTimeField(null=True)
    end_time = DateTimeField(null=True)
    total_marks = IntField()
    instructions = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    active = BooleanField(default=True)
    status = StringField()
    subject = ListField(StringField())
    topic = ListField(StringField())
    section = ListField(StringField())
    competency = ListField(StringField())
    published = BooleanField(default=False)
    

    def to_json(self):
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
            "total_marks": self.total_marks,
            "instructions": self.instructions,
            "course": str(self.course.id) if self.course else None,
            "year": str(self.year.id) if self.year else None,
            "created_by": str(self.created_by.id) if self.created_by else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "questions": [q.to_json() for q in self.questions],
            "published": self.published,
            "section": self.section,
            "active": self.active,
            "status": self.status,
            "subject": self.subject if self.subject else [],
            "topic": self.topic if self.topic else [],
            "section": self.section if self.section else [],
            "competency": self.competency if self.competency else [],
        }
