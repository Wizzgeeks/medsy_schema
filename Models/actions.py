from mongoengine import Document,StringField

class Action(Document):
    name = StringField(required=True,unique=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
        }
    