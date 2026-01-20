from mongoengine import Document,StringField,BooleanField,ValidationError,ReferenceField,IntField,CASCADE,DateTimeField
from Models.course_model import Course

class Year(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    year = StringField(required=True)
    meta_title = StringField()
    meta_image_url = StringField()
    meta_image_name = StringField()
    meta_description = StringField()
    meta_content = StringField()
    has_prompt = BooleanField(required=True,default=False)
    key = StringField(required=True,unique=True)
    sequence=IntField()
    onboarded = BooleanField(default=False)
    phase = StringField(choices=['Demo/Trial','Pilot','Paid Plan',''],default='',returned=True)
    start_date = DateTimeField()
    end_date = DateTimeField()
    status = StringField(choices=['Activated','Deactivated'],default='Deactivated',returned=True)

    def clean(self):
        if not self.year.strip():
            raise ValidationError("year cannot be empty")
        if not self.key.strip():
            raise ValidationError("key cannot be empty")
       
    #response data year field changed as name for ui rendering purpose
    def to_json(self):
        return {
            "id":str(self.id),
            "course":str(self.course.id) if self.course else None,
            "name":self.year,
            "meta_title":self.meta_title,
            "meta_image_name":self.meta_image_name,
            "meta_image_url":self.meta_image_url,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key,
            "sequence":self.sequence if self.sequence else 0,
            "onboarded":self.onboarded if self.onboarded else False,
            "phase":self.phase if self.phase else None,
            "start_date":self.start_date.strftime('%d/%m/%Y') if self.start_date else None,
            "end_date":self.end_date.strftime('%d/%m/%Y') if self.end_date else None,
            "status":self.status if self.status else None
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            "course":self.course.to_json() if self.course else None,
            "name":self.year,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_image_name":self.meta_image_name,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key,
            "sequence":self.sequence if self.sequence else 0,
            "onboarded":self.onboarded if self.onboarded else False,
            "phase":self.phase if self.phase else None,
            "start_date":self.start_date.strftime('%d/%m/%Y') if self.start_date else None,
            "end_date":self.end_date.strftime('%d/%m/%Y') if self.end_date else None,
            "status":self.status if self.status else None
        }
    def admin_json(self):
        return {
            # "id":str(self.id),
            "course":self.course.name if self.course else None,
            "name":self.year,
            "meta_title":self.meta_title,
            "meta_image_url":self.meta_image_url,
            "meta_image_name":self.meta_image_name,
            "meta_description":self.meta_description,
            "meta_content":self.meta_content,
            "has_prompt":self.has_prompt,
            "key":self.key,
            "sequence":self.sequence if self.sequence else 0,
            "onboarded":self.onboarded if self.onboarded else False,
            "phase":self.phase if self.phase else None,
            "start_date":self.start_date.strftime('%d/%m/%Y') if self.start_date else None,
            "end_date":self.end_date.strftime('%d/%m/%Y') if self.end_date else None,
            "status":self.status if self.status else None
        }
    def accordian_json(self):
        return {
            "name":self.year,
            "key":self.key,
            "squence":self.sequence
        }
    
    def nav_json(self):
        return {
            "id":str(self.id),
            "name":self.year,
            "key":self.key,
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)

