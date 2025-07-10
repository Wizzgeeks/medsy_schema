from mongoengine import Document, StringField

class Quick_suggestion(Document):
    suggestion = StringField(required=True)


    def to_json(self):
        return {
            "id": str(self.id),
            "suggestion": self.suggestion,
        }
