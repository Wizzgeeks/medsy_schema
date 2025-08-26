from mongoengine import Document,StringField,BooleanField,ValidationError,ReferenceField,CASCADE
from Models.institution_model import Institution
from Models.university_model import University

class Course(Document):
    # university = ReferenceField(University,required=True, reverse_delete_rule=CASCADE)
    # institution = ReferenceField(Institution,required=True, reverse_delete_rule=CASCADE)
    name = StringField(required=True,unique=True)
    duration = StringField(required=True)
    country = StringField(required=True)
    coin_value = StringField(required=True)
    meta_title = StringField()
    meta_image_url = StringField()
    meta_description = StringField()
    meta_content = StringField()
    has_prompt = BooleanField(required=True,default=False)
    key = StringField(required=True,unique=True)
    

    def clean(self):
        if not self.duration.strip():
            raise ValidationError("duration cannot be empty")
        if not self.coin_value.strip():
            raise ValidationError("coin_value cannot be empty")
        if not self.name.strip():
            raise ValidationError("course name cannot be empty")
        if not self.country.strip():
            raise ValidationError("country cannot be empty")
        if not self.key.strip():
            raise ValidationError("key cannot be empty")
        
    
    def to_json(self):
        return {
            "id": str(self.id),
            # "university":str(self.university.id) if self.university else None,
            # "institution":str(self.institution.id) if self.institution else None,
            "name":self.name,
            "duration":self.duration,
            "country":self.country,
            "coin_value":int(self.coin_value),
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key,
            }
    def admin_json(self):
        return {
            # "university":str(self.university.id) if self.university else None,
            # "institution":str(self.institution.id) if self.institution else None,
            "name":self.name,
            "duration":self.duration,
            "country":self.country,
            "coin_value":int(self.coin_value),
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key
        }
    def simple_data(self):
        return {
            # "id": str(self.id),
            "name":self.name,
            "country":self.country,
            "key":self.key
        }
    
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

