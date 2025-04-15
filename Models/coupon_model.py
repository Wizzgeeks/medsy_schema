from mongoengine import Document,StringField,ReferenceField,ValidationError,DateTimeField,IntField
from Models.course_model import Course
from datetime import datetime,timezone

class Coupon(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=2)
    name = StringField(required=True)
    discount_in_percentage = StringField()
    discount_in_flat = IntField()
    max_discount_in_price = IntField(required=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    expires = DateTimeField(required=True)
    code = StringField(required=True)
    max_usage=IntField(required=True)
    current_usage=IntField()

    

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Coupon name cannot be empty")
        

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "name":self.name,
            "discount_in_percentage":self.discount_in_percentage,
            "discount_in_flat":self.discount_in_flat,
            "max_discount_in_price":self.max_discount_in_price,
            "expires":self.expires,
            "count":self.code,
            "created_at": self.created_at.strftime("%d %B %Y"),
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "name":self.name,
            "discount_in_percentage":self.discount_in_percentage,
            "discount_in_flat":self.discount_in_flat,
            "max_discount_in_price":self.max_discount_in_price,
            "expires":self.expires,
            "count":self.code,
            "created_at": self.created_at.strftime("%d %B %Y")
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    
    
   