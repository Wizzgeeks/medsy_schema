from mongoengine import Document,StringField,ReferenceField,ValidationError,ListField,DecimalField,DictField
from Models.course_model import Course
from Models.year_model import Year

class Subscription(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    year = StringField()
    term_in_months = StringField(required=True)
    price = DecimalField(required=True)
    subscription_tier=StringField(required=True,)
    coins_threshold = StringField(required=True)
    component_association=ListField(DictField(),required=True)
   
    def clean(self):
        if not self.term_in_months.strip():
            raise ValidationError("Term in months cannot be empty")
        if not self.price.strip():
            raise ValidationError("Price  cannot be empty")
        if not self.coins_threshold.strip():
            raise ValidationError("Coins threshold cannot be empty")
        

    def to_json(self):
        return {
            "id": str(self.id),
            "course":(self.course.id) if self.course else None,
            "year":self.year if self.year else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "coins_threshold":self.coins_threshold,
            "component_association":self.component_association
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "year":self.year if self.year else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "coins_threshold":self.coins_threshold,
            "component_association":self.component_association
        }
    def admin_json(self):
        return {
            "id": str(self.id),
            "course":(self.course.name) if self.course else None,
            "year":self.year if self.year else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "coins_threshold":self.coins_threshold,
            "component_association":self.component_association
        }   
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    
    
   