from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self , name , expires):
        self.name = name
        self.expiry_date_time = expires
    
    @property
    def expired(self):
        if NOW < self.expiry_date_time:
            return False
        else:
            return True