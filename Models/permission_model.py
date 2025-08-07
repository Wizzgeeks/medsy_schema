from mongoengine import Document, ReferenceField, StringField, DictField, CASCADE
from Models.admin_model import Admin

class AdminPermission(Document):
    admin = ReferenceField(Admin, required=True, unique=True, reverse_delete_rule=CASCADE)
    role = StringField(choices=["superadmin", "admin", "staff"], required=True)
    module_permissions = DictField()
