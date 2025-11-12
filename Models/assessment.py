from mongoengine import ( Document, StringField, ReferenceField, ListField, DateTimeField, IntField, BooleanField ,CASCADE)
from datetime import datetime,timezone
from Models.course_model import Course
from Models.year_model import Year
from Models.admin_model import Admin
from Models.class_question_bank import ClassQuestionBank
from Models.assessment_prompt import AssessmentPrompt


class Assessment(Document):
    name = StringField(required=True)
    description = StringField()
    test_type = StringField(choices=["mcq", "qa", "hybrid"], required=True)
    category = StringField(choices=["internal", "midterm", "final", "viva"], required=True)
    duration = IntField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)
    total_marks = IntField()
    instructions = StringField()
    course = ReferenceField(Course, required=True)
    year = ReferenceField(Year, required=True)
    section = StringField(required=True)
    created_by = ReferenceField(Admin, required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    mcq_questions = ListField(ReferenceField(ClassQuestionBank,reversedelete_rule=CASCADE))
    qa_questions = ListField(ReferenceField(ClassQuestionBank,reversedelete_rule=CASCADE))
    active = BooleanField(default=True)
    published = BooleanField(default=False)
    prompts = ListField(ReferenceField(AssessmentPrompt,reversedelete_rule=CASCADE))
    

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
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
            "mcq_questions": [str(q.id) for q in self.mcq_questions],
            "qa_questions": [str(q.id) for q in self.qa_questions],
            "published": self.published,
            "section": self.section,
            "active": self.active,
            "prompts": [str(p.id) for p in self.prompts],
        }
