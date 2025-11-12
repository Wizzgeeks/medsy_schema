from mongoengine import Document,StringField,DictField,ListField,BooleanField


class ClassQuestionBank(Document):
    question = StringField(required=True)
    question_type = StringField(choices=["mcq", "qa"], required=True)
    options = DictField()
    explanation = StringField()
    category = StringField(choices=["direct", "critical_thinking", "reasoning", "application"])
    cognitive_level = StringField()
    difficulty_level = StringField()
    skill_focus = StringField()
    function = StringField()
    thinking_level = StringField()
    organ_system = StringField()
    disease_tags = ListField(StringField())
    distractor_error_tags = ListField(StringField())
    subject = StringField()
    topic = StringField()
    section = StringField()
    competency = StringField()
    answer = StringField()
    meta_tags = DictField()
    active = BooleanField(default=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "question": self.question,
            "question_type": self.question_type,
            "options": self.options,
            "explanation": self.explanation,
            "category": self.category,
            "cognitive_level": self.cognitive_level,
            "difficulty_level": self.difficulty_level,
            "skill_focus": self.skill_focus,
            "function": self.function,
            "thinking_level": self.thinking_level,
            "organ_system": self.organ_system,
            "disease_tags": self.disease_tags,
            "distractor_error_tags": self.distractor_error_tags,
            "subject": self.subject,
            "topic": self.topic,
            "section": self.section,
            "competency": self.competency,
            "answer": self.answer,
            "meta_tags": self.meta_tags,
            "active": self.active
        }
