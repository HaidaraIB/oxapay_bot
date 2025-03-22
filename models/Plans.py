from models.BaseEnum import BaseEnum


class Plans(BaseEnum):
    Daily = {
        "text": "Daily: $15",
        "link": "https://oxapay.com/pay/30247996",
    }
    Weekly = {
        "text": "Weekly: $50",
        "link": "https://oxapay.com/pay/35978796",
    }
    Monthly = {
        "text": "Monthly: $100",
        "link": "https://oxapay.com/pay/48466270",
    }
    Lifetime = {
        "text": "Lifetime: $300",
        "link": "https://oxapay.com/pay/97253525",
    }

    @classmethod
    def get_plan_from_text(cls, text):
        for plan_name, plan_data in cls.__members__.items():
            if plan_data.value["text"] == text:
                return plan_data
        return None  # Return None if no match is found

