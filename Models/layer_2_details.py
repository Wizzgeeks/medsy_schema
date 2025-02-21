from mongoengine import Document,StringField,ReferenceField
from Models.course_model import Course


class Layer_2_details(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    layer_2_name = StringField(required=True)

    def to_json(self):
        return {
            'layer_2_name': self.layer_2_name
        }
            