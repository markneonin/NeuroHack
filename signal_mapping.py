import pymongo



client = pymongo.MongoClient('mongodb://user:password@0.0.0.0:27017')
db = client["statistic"]
collection = db["signal"]

class Bear():
    def __init__(self, keys):
        order_by = 'moment'
        self.vibration_horizontal = collection.find(
            {'key': keys[6]},
            {'value': 1, '_id':0}).sort(order_by).limit(500)
        self.vibration_horizontal = list(self.vibration_horizontal)
        self.vibration_horizontal = [i.get('value') for i in
                                     self.vibration_horizontal]
        self.vibration_horizontal_warning_max = collection.find_one({'exgauster': 1, 'key': keys[9]}, {'value': 1, '_id':0})
        self.vibration_vertical = collection.find(
            {'key': keys[11]},
            {'value': 1, '_id': 0}).sort(order_by).limit(500)
        self.vibration_vertical = list(self.vibration_vertical)
        self.vibration_vertical = [i.get('value') for i in
                                     self.vibration_vertical]
        self.vibration_vertical_warning_max = collection.find_one({'exgauster': 1, 'key': keys[14]}, {'value': 1, '_id':0})
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
        expected_step = (start_diapazone - data[-1]) / coef_step
        # step = 1 minute
        hours = expected_step / 60
        return hours if hours > 0 else 99999


pods_7_1_ex = [
'SM_Exgauster\[2:33]',
'SM_Exgauster\[2:8]',
'SM_Exgauster\[2:145]',
'SM_Exgauster\[2:157]',
'SM_Exgauster\[2:169]',
'SM_Exgauster\[2:181]',
'SM_Exgauster\[2:6]',
'SM_Exgauster\[2:143]',
'SM_Exgauster\[2:155]',
'SM_Exgauster\[2:167]',
'SM_Exgauster\[2:179]',
'SM_Exgauster\[2:7]',
'SM_Exgauster\[2:144]',
'SM_Exgauster\[2:156]',
'SM_Exgauster\[2:168]',
'SM_Exgauster\[2:180]',
]
pods_8_1_ex = [
'SM_Exgauster\[2:34]',
'SM_Exgauster\[2:11]',
'SM_Exgauster\[2:148]',
'SM_Exgauster\[2:160]',
'SM_Exgauster\[2:172]',
'SM_Exgauster\[2:184]',
'SM_Exgauster\[2:9]',
'SM_Exgauster\[2:146]',
'SM_Exgauster\[2:158]',
'SM_Exgauster\[2:170]',
'SM_Exgauster\[2:182]',
'SM_Exgauster\[2:10]',
'SM_Exgauster\[2:147]',
'SM_Exgauster\[2:159]',
'SM_Exgauster\[2:171]',
'SM_Exgauster\[2:183]',

]
a = Bear(pods_7_1_ex)
b = Bear(pods_8_1_ex)
print(a | b)



# use the find_one method to select one document from the collection
# temp = collection.find({'exgauster': 1, 'key': "SM_Exgauster\\[2:33]"}, {'value': 1, '_id':0})
# print(DataFrame(list(temp)))
# print the document
#
# list_json =[]
# final_dict = {}
# for sheet in range(1, 7):
#     WS = pd.read_excel('Маппинг сигналов.xlsx', sheet_name=str(sheet))
#     WS = WS.fillna(0)
#     WS_np = np.array(WS)
#     print(WS_np)
#     print('----------', sheet)
#     current_device = None
#     current_metrics = None
#     current_metrics_for_bears = None
#     current_exgauster = 1
#     for i in WS_np:
#         if i[0]:
#             current_device = i[0]
#         if i[1]:
#             current_metrics = i[1]
#         if i[2]:
#             current_metrics_for_bears = i[2]
#         else:
#             current_metrics_for_bears = None
#         final_dict[i[4]] = {'exgauster': sheet,
#                             'description':{'Device':current_device,
#                                 'Current metrics':current_metrics,
#                                 'Additional metrics for bears':current_metrics_for_bears,
#                                 'Full_name': i[5]
#                                            }
#                             }
#
# print(final_dict)
# with open('mapping.json', 'w') as file:
#     json.dump(final_dict, file)