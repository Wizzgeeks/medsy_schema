from mongoengine import ReferenceField,Document,StringField,DateTimeField,IntField,CASCADE
from Models.user_model import User
from Models.user_subscription_model import User_subscription
from datetime import datetime,timezone

class Transaction_detail(Document):
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    user_subscription = ReferenceField(User_subscription,reverse_delete_rule=CASCADE,required=True)
    transaction_time = DateTimeField(required=True,default=datetime.now(timezone.utc))
    order_id = StringField(required=True)
    payment_id = StringField(required=True)
    signature = StringField(required=True)
    mode = StringField(required=True)
    amount_paid = IntField(required=True)
    status = StringField(required=True)

    def to_json(self):
        return {
        "id":str(self.id),
        "user":str(self.user.id) if self.user else None,
        "user_subscription":self.user_subscription.to_json() if self.user_subscription else None,
        "transaction_time":self.transaction_time,
        "order_id":self.order_id,
        "payment_id":self.payment_id,
        "signature":self.signature,
        "mode":self.mode,
        "amount_paid":self.amount_paid,
        "status":self.status
        }
    
    def with_key(self):
        return {
        "id":str(self.id),
        "user":self.user.to_json() if self.user else None,
        "user_subscription":self.user_subscription.to_json() if self.user_subscription else None,
        "transaction_time":self.transaction_time,
        "order_id":self.order_id,
        "payment_id":self.payment_id,
        "signature":self.signature,
        "mode":self.mode,
        "amount_paid":self.amount_paid,
        "status":self.status
        }

