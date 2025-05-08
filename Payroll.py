from PaySchedule import PaySchedule


class Payroll:
    def __init__(self):
        self.staff_category_pay_schedules = {"Manager": PaySchedule("1st")}

    def get_staff_category_pay_schedule(self, staff_category):
        return self.staff_category_pay_schedules[staff_category]

    def get_staff_category_pay_day(self, staff_category):
        return self.staff_category_pay_schedules[staff_category].get_pay_date()