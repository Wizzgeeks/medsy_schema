from mongoengine import Document,StringField,DictField,ListField,BooleanField,IntField,ReferenceField,CASCADE


class ClassQuestionBank(Document):
    question = StringField(required=True)
    question_type = StringField(choices=["mcq", "descriptive"], required=True)
    is_main_question = BooleanField(default=True)
    main_question = ReferenceField("ClassQuestionBank",reverse_delete_rule=CASCADE)
    sub_questions = ListField(ReferenceField("ClassQuestionBank",reverse_delete_rule=CASCADE))
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
    subject = ListField(DictField())
    topic = ListField(DictField())
    section = ListField(DictField())
    competency = ListField(DictField())
    answer = StringField()
    meta_tags = DictField()
    active = BooleanField(default=True)
    mark = IntField(default=1)

    def to_json(self):
        return {
            "id": str(self.id),
            "question": self.question,
            "question_type": self.question_type,
            "is_main_question": self.is_main_question,
            "main_question": str(self.main_question.id) if self.main_question else None,
            "sub_questions": [ q.to_json() for q in self.sub_questions],
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
            "topic": self.topic if self.topic else [],
            "section": self.section if self.section else [],
            "competency": self.competency if self.competency else [],
            "answer": self.answer,
            "meta_tags": self.meta_tags if self.meta_tags else {},
            "active": self.active,
            "mark": self.mark,
        }
