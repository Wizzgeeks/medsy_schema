from mongoengine import Document, StringField, ValidationError,BooleanField

class Component(Document):
    name = StringField(required=True,unique=True)
    dependent = BooleanField(required=True,default=False)

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Component name cannot be empty")

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "dependent":self.dependent
        }

    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
