from mongoengine import Document,StringField,ReferenceField
from Models.coupon_model import Coupon
from Models.subscription_model import Subscription
from Models.user_model import User

class User_subscription(Document):
    user = ReferenceField(User,required=True,reverse_delete_rule=2)
    subscription = ReferenceField(Subscription,required=True,reverse_delete_rule=2)
    coupon = ReferenceField(Coupon,reverse_delete_rule=2)
    coins_redeemed=StringField()
    expiry = StringField(required=True)

    def to_json(self):
        return {
            "id":str(self.id),
            "user":str(self.user.id) if self.user else None,
            "subscription":self.subscription.to_json() if self.subscription else None,
            "coupon":str(self.coupon.id) if self.coupon else None,
            "coins_redeemed":self.coins_redeemed if self.coins_redeemed else None,
            "expiry":self.expiry
        }
    
    def with_key(self):
        return {
            "id":str(self.id),
            "user":self.user.to_json() if self.user else None,
            "subscription":self.subscription.to_json() if self.subscription else None,
            "coupon":self.coupon.to_json() if self.coupon else None,
            "coins_redeemed":self.coins_redeemed if self.coins_redeemed else None,
            "expiry":self.expiry
        }