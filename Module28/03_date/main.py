class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

    @classmethod
    def is_date_valid(cls, date):
        dm_list = date.split('-')
        day, month, year = int(dm_list[0]), int(dm_list[1]), int(dm_list[2])
        return 0 < day <= 31 and 0 < month <= 12 and year <= 9999

    @classmethod
    def from_string(cls, date):
        dm_list = date.split('-')
        day, month, year = int(dm_list[0]), int(dm_list[1]), int(dm_list[2])
        date_obj = cls(day, month, year)
        return date_obj


my_date = Date.from_string('03-06-2024')
print(my_date)
print(Date.is_date_valid('03-06-2024'))
print(Date.is_date_valid('31-06-2025'))
