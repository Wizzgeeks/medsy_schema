from mongoengine import Document,StringField,ReferenceField,BooleanField,ValidationError,IntField,CASCADE
from Models.course_model import Course
from Models.year_model import Year

class Subject(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    year = ReferenceField(Year,required=True,reverse_delete_rule=CASCADE)
    name = StringField(required=True)
    meta_title = StringField()
    meta_image_url = StringField()
    meta_description = StringField()
    meta_content = StringField()
    has_prompt = BooleanField(required=True,default=False)
    key = StringField(required=True,unique=True)
    has_3_layers = BooleanField()
    sequence=IntField()

    def clean(self):
        if not self.name.strip():
            raise ValidationError("subject name cannot be empty")
        if not self.key.strip():
            raise ValidationError("key cannot be empty")

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "year":str(self.year.id) if self.year else None,
            "name":self.name,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "has_3_layers":self.has_3_layers,
            "key":self.key,
            "sequence":self.sequence if self.sequence else 0
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "year":self.year.to_json() if self.year else None,
            "name":self.name,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "has_3_layers":self.has_3_layers,
            "key":self.key,
            "sequence":self.sequence if self.sequence else 0
        }
    def admin_json(self):
        return {
            # "id": str(self.id),
            "course":self.course.name if self.course else None,
            "year":self.year.year if self.year else None,
            "name":self.name,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "has_3_layers":self.has_3_layers,
            "key":self.key,
            "sequence":self.sequence if self.sequence else 0
        }
    
    def accordian_json(self):
        return {
            "name":self.name,
            "key":self.key,
            "sequence":self.sequence if self.sequence else 0
        }
    
    def nav_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "key":self.key,
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    
    
   