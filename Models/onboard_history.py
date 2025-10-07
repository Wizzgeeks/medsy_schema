from mongoengine import Document,StringField,ReferenceField,CASCADE,DateTimeField
from Models.course_model import Course
from Models.institution_model import Institution
from Models.year_model import Year
from datetime import datetime,timezone

class OnboardHistory(Document):
    institution = ReferenceField(Institution,required=True, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    year = ReferenceField(Year,required=True,reverse_delete_rule=CASCADE)
    phase = StringField(choices=['Demo/Trial','Pilot','Paid Plan',''],default='',returned=True)
    start_date = DateTimeField()
    end_date = DateTimeField()
    remarks = StringField()
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    status = StringField(choices=['Activated','Deactivated'],default='Deactivated',returned=True)

   
    def to_json(self):
        return {
            "id":str(self.id),
            "institution":str(self.institution.id) if self.institution else None,
            "course":str(self.course.id) if self.course else None,
            "year":str(self.year.id) if self.year else None,
            "remarks":self.remarks if self.remarks else None,
            "phase":self.phase if self.phase else None,
            "start_date":self.start_date.isoformat('%d/%m/%Y') if self.start_date else None,
            "end_date":self.end_date.isoformat('%d/%m/%Y') if self.end_date else None,
            "status":self.status if self.status else None,
            "created_at":self.created_at.isoformat('%d/%m/%Y') if self.created_at else None
        }
    


