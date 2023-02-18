import datetime
import pymongo
from bears_mapping import pods_8_2_ex, pods_7_1_ex, pods_7_2_ex, pods_7_4_ex, \
    pods_7_5_ex, pods_7_6_ex, pods_8_1_ex, pods_8_3_ex, pods_8_4_ex,\
    pods_8_5_ex, pods_8_6_ex, pods_7_3_ex






class Bear():
    def __init__(self, keys, collection):
        order_by = 'moment'
        self.vibration_horizontal = collection.find(
            {'key': keys[6]},
            {'value': 1, '_id':0}).sort(order_by).limit(500)
        self.vibration_horizontal = list(self.vibration_horizontal)
        self.vibration_horizontal = [i.get('value') for i in
                                     self.vibration_horizontal]
        self.vibration_horizontal_warning_max = collection.find_one({'key': keys[9]}, {'value': 1, '_id':0})
        self.vibration_vertical = collection.find(
            {'key': keys[11]},
            {'value': 1, '_id': 0}).sort(order_by).limit(500)
        self.vibration_vertical = list(self.vibration_vertical)
        self.vibration_vertical = [i.get('value') for i in
                                     self.vibration_vertical]
        self.vibration_vertical_warning_max = collection.find_one({'key': keys[14]}, {'value': 1, '_id':0})
        self.horizontal_deadline = self._find_deadlines(self.vibration_horizontal)
        self.vertical_deadline = self._find_deadlines(self.vibration_vertical)
        self.final_deadline = self._find_closed_deadline()


    def __or__(self, other):
        return self.final_deadline if self.final_deadline < other.final_deadline else other.final_deadline

    def _find_closed_deadline(self):
        return self.horizontal_deadline \
            if self.horizontal_deadline < self.vertical_deadline \
            else self.vertical_deadline
    def _find_deadlines(self, data):
        start_diapazone = self.vibration_horizontal_warning_max.get('value')
        summ = 0
        for i in range(len(data) - 1):
            try:
                summ += data[i + 1] - data[i]
            except:
                pass
        coef_step = summ / (len(data) - 1)
        if coef_step:
            expected_step = (start_diapazone - data[-1]) / coef_step
        # step = 1 minute
            hours = expected_step / 60
        else:
            hours = 9999
        return hours if hours > 0 else 99999.9


if __name__ == '__main__':
    client = pymongo.MongoClient('mongodb://user:password@0.0.0.0:27017')
    db = client["statistic"]
    collection = db["signal"]
    client_write = pymongo.MongoClient('mongodb://user:password@0.0.0.0:27017')
    db_write = client_write["statistic"]
    collection_write = db_write["predict"]
    data_to_write = {}

    first = Bear(pods_7_1_ex, collection)
    second = Bear(pods_8_1_ex, collection)
    data_to_write.update({'1': first | second})
    first = Bear(pods_7_2_ex, collection)
    second = Bear(pods_8_2_ex, collection)
    data_to_write.update({'2': first | second})
    first = Bear(pods_7_3_ex, collection)
    second = Bear(pods_8_3_ex, collection)
    data_to_write.update({'3': first | second})
    first = Bear(pods_7_4_ex, collection)
    second = Bear(pods_8_4_ex, collection)
    data_to_write.update({'4': first | second})
    first = Bear(pods_7_5_ex, collection)
    second = Bear(pods_8_5_ex, collection)
    data_to_write.update({'5': first | second})
    first = Bear(pods_7_6_ex, collection)
    second = Bear(pods_8_6_ex, collection)
    data_to_write.update({'6': first | second})
    print(data_to_write)
    data_to_write = {'1': 437.1247784706043, '2': 964.1784272821295, '3': 178.03486565955876, '4': 373.5651088206939, '5': 6270.0475032350205, '6': 9999.9}
    data_to_write.update({'predicted_at': datetime.datetime.now()})
    collection_write.insert_one(data_to_write)
