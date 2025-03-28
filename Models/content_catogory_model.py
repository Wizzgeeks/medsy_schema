from mongoengine import Document, StringField, ValidationError

class ContentCategory(Document):
    name = StringField(required=True,unique=True)
    key = StringField(required=True,unique=True)

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Component name cannot be empty")

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "key":self.key
        }

    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
