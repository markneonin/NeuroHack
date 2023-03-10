import json

with open('./constants/signals_mapping.json', 'r') as f:
    signals_mapping = json.load(f)

prediction_keys = [
'SM_Exgauster\[2:21]',
'SM_Exgauster\[2:218]',
'SM_Exgauster\[2:22]',
'SM_Exgauster\[2:219]',
'SM_Exgauster\[2:6]',
'SM_Exgauster\[2:167]',
'SM_Exgauster\[2:7]',
'SM_Exgauster\[2:168]',
'SM_Exgauster\[2:18]',
'SM_Exgauster\[2:215]',
'SM_Exgauster\[2:19]',
'SM_Exgauster\[2:216]',
'SM_Exgauster\[0:18]',
'SM_Exgauster\[0:213]',
'SM_Exgauster\[0:19]',
'SM_Exgauster\[0:214]',
'SM_Exgauster\[3:6]',
'SM_Exgauster\[3:165]',
'SM_Exgauster\[3:7]',
'SM_Exgauster\[3:166]',
'SM_Exgauster\[3:18]',
'SM_Exgauster\[3:213]',
'SM_Exgauster\[3:19]',
'SM_Exgauster\[3:214]',
'SM_Exgauster\[2:9]',
'SM_Exgauster\[2:170]',
'SM_Exgauster\[2:10]',
'SM_Exgauster\[2:171]',
'SM_Exgauster\[0:9]',
'SM_Exgauster\[0:168]',
'SM_Exgauster\[0:10]',
'SM_Exgauster\[0:169]',
'SM_Exgauster\[0:21]',
'SM_Exgauster\[0:216]',
'SM_Exgauster\[0:22]',
'SM_Exgauster\[0:217]',
'SM_Exgauster\[3:9]',
'SM_Exgauster\[3:168]',
'SM_Exgauster\[3:10]',
'SM_Exgauster\[3:169]',
'SM_Exgauster\[3:21]',
'SM_Exgauster\[3:216]',
'SM_Exgauster\[3:22]',
'SM_Exgauster\[3:217]',
'SM_Exgauster\[0:6]',
'SM_Exgauster\[0:165]',
'SM_Exgauster\[0:7]',
'SM_Exgauster\[0:166]',
]

