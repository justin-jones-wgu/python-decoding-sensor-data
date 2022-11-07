from datetime import date, datetime

class HouseInfo:

    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []

        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record[field]):
                field_data.append(record[field])

        return field_data

    def get_data_by_date(self, field, rec_data=date.today()):
        field_data = []

        for record in self.data:
            if rec_data.strftime("%m/%d/%y") == record['date']:
                field_data.append(record[field])

        return field_data
