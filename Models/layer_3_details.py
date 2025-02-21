from mongoengine import Document,StringField,ReferenceField
from Models.course_model import Course


class Layer_3_details(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    layer_3_name = StringField(required=True)

    def to_json(self):
        return {
            'course': self.course.key,
            'layer_1_name': self.layer_3_name
        }
            