from mongoengine import Document, StringField, DictField,BooleanField,DateTimeField
from datetime import datetime,timezone

class AdminPermission(Document):
    role = StringField(required=True,unique=True)
    module_permissions = DictField()
    active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now(timezone.utc))


    def to_json(self):
        return {
            'id': str(self.id),
            'role': self.role,
            'module_permissions': self.module_permissions,
            'active': self.active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

