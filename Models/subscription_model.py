from mongoengine import Document,StringField,ReferenceField,ValidationError,ListField,FloatField,DictField,CASCADE
from Models.course_model import Course
from Models.year_model import Year
from Models.content_catogory_model import ContentCategory

class Subscription(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = ListField(ReferenceField(Year,reverse_delete_rule=CASCADE,required=True))
    term_in_months = StringField(required=True)
    price = FloatField(required=True)
    subscription_tier=StringField(required=True)
    coins_threshold = StringField(required=True)
    categories=ListField(ReferenceField(ContentCategory,reverse_delete_rule=CASCADE,required=True))
    package_name=StringField(required=True)
    max_token=StringField(required=True)

   

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "year":[years.to_json() for years in self.year] if self.year else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "coins_threshold":self.coins_threshold,
            "categories":[categories.to_json() for categories in self.categories] if self.categories else None,
            "subscription_tier":self.subscription_tier,
            "package_name":self.package_name,
            "max_token":self.max_token
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "year":[years.to_json() for years in self.year] if self.year else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "coins_threshold":self.coins_threshold,
            "categories":[categories.to_json() for categories in self.categories] if self.categories else None,
            "subscription_tier":self.subscription_tier,
            "package_name":self.package_name,
            "max_token":self.max_token
        }
    def admin_json(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "year":[years.to_json() for years in self.year] if self.year else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "coins_threshold":self.coins_threshold,
            "categories":[categories.to_json() for categories in self.categories] if self.categories else None,
            "subscription_tier":self.subscription_tier,
            "package_name":self.package_name,
            "max_token":self.max_token
        }   
    
    
    
   