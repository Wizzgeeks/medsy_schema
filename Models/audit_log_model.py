from mongoengine import Document,StringField,IntField,ReferenceField,DateTimeField,ListField,DictField,CASCADE
from Models.admin_model import Admin
from datetime import datetime,timezone
class Audit_log(Document):
    user_id = ReferenceField(Admin,reverse_delete_rule=CASCADE,required=True)
    method=StringField()
    table_name=StringField()
    id_or_key=StringField()
    updated_data=DictField(default={})
    existing_data=DictField(default={})
    created_at = DateTimeField(default=datetime.now(timezone.utc))

    def to_json(self):
        return {
            'user_id': str(self.user_id.id) if self.user_id else None,
            'method':self.method,
            'table_name':self.table_name,
            'id_or_key':self.id_or_key,
            'updated_data':self.updated_data,
            'existing_data':self.existing_data,
            'created_at':self.created_at.isoformat()
        }

