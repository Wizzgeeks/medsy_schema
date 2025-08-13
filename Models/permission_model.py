from mongoengine import Document, StringField, DictField

class AdminPermission(Document):
    role = StringField(required=True)
    module_permissions = DictField()
