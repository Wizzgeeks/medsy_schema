from mongoengine import Document,StringField,DictField,ListField,BooleanField,IntField,ReferenceField,CASCADE,EmbeddedDocumentField,EmbeddedDocument
from Models.subject_model import Subject
from Models.layer_1_model import Layer_1
from Models.layer_2_model import Layer_2
from Models.layer_3_model import Layer_3

class QuestionBank(EmbeddedDocument):
    question = ReferenceField("ClassQuestionBank", required=True)
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
    category = StringField(choices=["direct", "critical_thinking", "reasoning", "application"])
    image_url = StringField()
    cognitive_level = StringField()
    difficulty_level = StringField()
    skill_focus = ListField(StringField())
    function = ListField(StringField())
    thinking_level = StringField()
    organ_system = ListField(StringField())
    disease_tags = ListField(StringField())
    distractor_error_tags = DictField()
    key_concept = ListField(StringField())
    learning_objective = StringField()
    subject = ListField(ReferenceField(Subject,reverse_delete_rule=CASCADE, required=True))
    layer1 = ListField(ReferenceField(Layer_1,reverse_delete_rule=CASCADE, required=True))
    layer2 = ListField(ReferenceField(Layer_2,reverse_delete_rule=CASCADE, required=True))
    layer3 = ListField(ReferenceField(Layer_3,reverse_delete_rule=CASCADE, required=True))
    answer = StringField()
    meta_tags = DictField()
    active = BooleanField(default=True)
    mark = IntField(default=1)
    author=StringField()
    

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
            "subject": [{"id": str(subject.id), "name": subject.name, "key": subject.key} for subject in self.subject] if self.subject else [],
            "layer1": [{"id": str(layer1.id), "name": layer1.name, "key": layer1.key} for layer1 in self.layer1] if self.layer1 else [],
            "layer2": [{"id": str(layer2.id), "name": layer2.name, "key": layer2.key} for layer2 in self.layer2] if self.layer2 else [],
            "layer3": [{"id": str(layer3.id), "name": layer3.name, "key": layer3.key} for layer3 in self.layer3] if self.layer3 else [],
            "answer": self.answer,
            "meta_tags": self.meta_tags if self.meta_tags else {},
            "active": self.active,
            "mark": self.mark,
            "author": self.author if self.author else "",
            "key_concept": self.key_concept if self.key_concept else [],
            "learning_objective": self.learning_objective if self.learning_objective else ""
        }
