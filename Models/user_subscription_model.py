from mongoengine import Document,IntField,ReferenceField,DateTimeField,CASCADE
from Models.coupon_model import Coupon
from Models.subscription_model import Subscription
from Models.user_model import User

class User_subscription(Document):
    user = ReferenceField(User,reverse_delete_rule=CASCADE,required=True)
    subscription = ReferenceField(Subscription,reverse_delete_rule=CASCADE,required=True)
    coupon = ReferenceField(Coupon,reverse_delete_rule=CASCADE)
    coins_redeemed=IntField()
    expiry = DateTimeField(required=True)

    def to_json(self):
        return {
            "id":str(self.id),
            "user":str(self.user.id) if self.user else None,
            "subscription":self.subscription.to_json() if self.subscription else None,
            "coupon":str(self.coupon.id) if self.coupon else None,
            "coins_redeemed":self.coins_redeemed if self.coins_redeemed else None,
            "expiry":self.expiry.strftime('%d/%m/%Y')
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            "user":self.user.to_json() if self.user else None,
            "subscription":self.subscription.to_json() if self.subscription else None,
            "coupon":self.coupon.to_json() if self.coupon else None,
            "coins_redeemed":self.coins_redeemed if self.coins_redeemed else None,
            "expiry":self.expiry.strftime('%d/%m/%Y')
        }