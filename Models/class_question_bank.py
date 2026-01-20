from mongoengine import Document,StringField,DictField,ListField,BooleanField,IntField,ReferenceField,CASCADE,NULLIFY,EmbeddedDocumentField,EmbeddedDocument
from Models.admin_model import Admin

class QuestionBank(EmbeddedDocument):
    question = ReferenceField("ClassQuestionBank",required=True)
    sequence = IntField(default=0)
    
    def to_json(self):
        return {
            "question": self.question.to_json() if self.question else None,
            "sequence": self.sequence
        }


class ClassQuestionBank(Document):
    question = StringField(required=True)
    question_type = StringField(choices=["mcq", "descriptive"], required=True)
    is_main_question = BooleanField(default=True)
    main_question = ReferenceField("ClassQuestionBank",reverse_delete_rule=CASCADE)
    sub_questions = ListField(EmbeddedDocumentField(QuestionBank))
    options = DictField()
    explanation = StringField()
    # category = StringField(choices=["direct", "critical_thinking", "reasoning", "application"])
    category = StringField()
    image_url = StringField()
    cognitive_level = StringField()
    difficulty_level = StringField()
    skill_focus = ListField(StringField())
    function = ListField(StringField())
    thinking_level = StringField(choices=["HoT", "LoT"])
    organ_system = ListField(StringField())
    organ_sub_system = ListField(StringField())
    disease_tags = ListField(StringField())
    distractor_error_tags = DictField()
    key_concept = ListField(StringField())
    learning_objective = StringField()
    subject = ListField()
    layer1 = ListField()
    layer2 = ListField()
    layer3 = ListField()
    answer = StringField()
    meta_tags = DictField()
    active = BooleanField(default=True)
    mark = IntField(default=1)
    author = StringField()
    author_id = ReferenceField(Admin, reverse_delete_rule=NULLIFY, required=True)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "question": self.question,
            "question_type": self.question_type,
            "is_main_question": self.is_main_question,
            "main_question": str(self.main_question.id) if self.main_question else None,
            "sub_questions": [q.to_json() for q in self.sub_questions],
            "options": self.options if self.options else {},
            "explanation": self.explanation,
            "category": self.category,
            "cognitive_level": self.cognitive_level if self.cognitive_level else "",
            "image_url": self.image_url if self.image_url else "",
            "difficulty_level": self.difficulty_level,
            "skill_focus": self.skill_focus if self.skill_focus else [],
            "function": self.function if self.function else [],
            "thinking_level": self.thinking_level,
            "organ_system": self.organ_system if self.organ_system else [],
            "disease_tags": self.disease_tags if self.disease_tags else [],
            "distractor_error_tags": self.distractor_error_tags if self.distractor_error_tags else {},
            "subject": self.subject if self.subject else [],
            "layer1": self.layer1 if self.layer1 else [],
            "layer2": self.layer2 if self.layer2 else [],
            "layer3": self.layer3 if self.layer3 else [],
            "answer": self.answer,
            "meta_tags": self.meta_tags if self.meta_tags else {},
            "active": self.active,
            "mark": self.mark,
            "author": self.author if self.author else "",
            "key_concept": self.key_concept if self.key_concept else [],
            "organ_sub_system": self.organ_sub_system if self.organ_sub_system else [],
            "learning_objective": self.learning_objective if self.learning_objective else "",
            "author_id": {"id":str(self.author_id.id),"name":self.author_id.name,"faculty_id":self.author_id.admin_id} if self.author_id else {},
        }
