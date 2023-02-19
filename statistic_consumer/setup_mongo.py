import asyncio

import motor.motor_asyncio
from bson import ObjectId
from pymongo import ASCENDING

STATISTIC_DB = "mongodb://user:password@mongo"

client = motor.motor_asyncio.AsyncIOMotorClient(STATISTIC_DB)
db = client.statistic
signal = db['signal']

collections = [
    'bearing_big',
    'bearing_small',
    'cooler',
    'exgauster_work',
    'gas_manifold',
    'main_drive',
    'oil_system',
    'valve_position',
]


async def create_indexes():
    await signal.create_index([("moment", ASCENDING)], expireAfterSeconds=36000)
    index = [('component_id', 1), ('moment', -1)]
    for collection in collections:
        await db[collection].create_index(index)


async def write_to_mongo(objects):
    if not await db.exgauster.find_one():
        await db.exgauster.insert_many(objects)
    await create_indexes()


objs = [
    {
        'number': 1,
        'name': 'У-171',
        'bearings_big': [
            {
                '_id': ObjectId(),
                'number': 1,
                'name': 'Подшипник 1',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:27]',
                    'temperature_alarm_max': 'SM_Exgauster\\[2:65]',
                    'temperature_alarm_min': 'SM_Exgauster\\[2:74]',
                    'temperature_warning_max': 'SM_Exgauster\\[2:83]',
                    'temperature_warning_min': 'SM_Exgauster\\[2:92]',
                    'vibration_axial': 'SM_Exgauster\\[2:2]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[2:139]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[2:151]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[2:163]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[2:175]',
                    'vibration_horizontal': 'SM_Exgauster\\[2:0]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[2:137]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[2:149]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[2:161]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[2:173]',
                    'vibration_vertical': 'SM_Exgauster\\[2:1]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[2:138]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[2:150]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[2:162]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[2:174]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 2,
                'name': 'Подшипник 2',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:28]',
                    'temperature_alarm_max': 'SM_Exgauster\\[2:66]',
                    'temperature_alarm_min': 'SM_Exgauster\\[2:75]',
                    'temperature_warning_max': 'SM_Exgauster\\[2:84]',
                    'temperature_warning_min': 'SM_Exgauster\\[2:93]',
                    'vibration_axial': 'SM_Exgauster\\[2:5]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[2:142]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[2:154]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[2:166]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[2:178]',
                    'vibration_horizontal': 'SM_Exgauster\\[2:3]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[2:140]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[2:152]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[2:164]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[2:176]',
                    'vibration_vertical': 'SM_Exgauster\\[2:4]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[2:141]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[2:153]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[2:165]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[2:177]',
                }
            },
            {
                '_id': ObjectId(),
                'name': 'Подшипник 7',
                'number': 7,
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:33]',
                    'temperature_alarm_max': 'SM_Exgauster\\[2:71]',
                    'temperature_alarm_min': 'SM_Exgauster\\[2:80]',
                    'temperature_warning_max': 'SM_Exgauster\\[2:89]',
                    'temperature_warning_min': 'SM_Exgauster\\[2:98]',
                    'vibration_axial': 'SM_Exgauster\\[2:8]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[2:145]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[2:157]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[2:169]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[2:181]',
                    'vibration_horizontal': 'SM_Exgauster\\[2:6]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[2:143]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[2:155]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[2:167]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[2:179]',
                    'vibration_vertical': 'SM_Exgauster\\[2:7]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[2:144]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[2:156]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[2:168]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[2:180]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 8,
                'name': 'Подшипник 8',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:34]',
                    'temperature_alarm_max': 'SM_Exgauster\\[2:72]',
                    'temperature_alarm_min': 'SM_Exgauster\\[2:81]',
                    'temperature_warning_max': 'SM_Exgauster\\[2:90]',
                    'temperature_warning_min': 'SM_Exgauster\\[2:99]',
                    'vibration_axial': 'SM_Exgauster\\[2:11]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[2:148]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[2:160]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[2:172]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[2:184]',
                    'vibration_horizontal': 'SM_Exgauster\\[2:9]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[2:146]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[2:158]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[2:170]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[2:182]',
                    'vibration_vertical': 'SM_Exgauster\\[2:10]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[2:147]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[2:159]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[2:171]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[2:183]',
                }
            },
        ],
        'bearings_small': [
            {
                '_id': ObjectId(),
                'number': 3,
                'name': 'Подшипник 3',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:29]',
                    'alarm_max': 'SM_Exgauster\\[2:67]',
                    'alarm_min': 'SM_Exgauster\\[2:76]',
                    'warning_max': 'SM_Exgauster\\[2:85]',
                    'warning_min': 'SM_Exgauster\\[2:94]',
                }

            },
            {
                '_id': ObjectId(),
                'number': 4,
                'name': 'Подшипник 4',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:30]',
                    'alarm_max': 'SM_Exgauster\\[2:68]',
                    'alarm_min': 'SM_Exgauster\\[2:77]',
                    'warning_max': 'SM_Exgauster\\[2:86]',
                    'warning_min': 'SM_Exgauster\\[2:95]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 5,
                'name': 'Подшипник 5',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:31]',
                    'alarm_max': 'SM_Exgauster\\[2:69]',
                    'alarm_min': 'SM_Exgauster\\[2:78]',
                    'warning_max': 'SM_Exgauster\\[2:87]',
                    'warning_min': 'SM_Exgauster\\[2:96]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 6,
                'name': 'Подшипник 6',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:32]',
                    'alarm_max': 'SM_Exgauster\\[2:70]',
                    'alarm_min': 'SM_Exgauster\\[2:79]',
                    'warning_max': 'SM_Exgauster\\[2:88]',
                    'warning_min': 'SM_Exgauster\\[2:97]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 9,
                'name': 'Подшипник 9',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:35]',
                    'alarm_max': 'SM_Exgauster\\[2:73]',
                    'alarm_min': 'SM_Exgauster\\[2:82]',
                    'warning_max': 'SM_Exgauster\\[2:91]',
                    'warning_min': 'SM_Exgauster\\[2:100]',
                }
            },
        ],
        'cooler': {
            '_id': ObjectId(),
            'name': 'Охладитель',
            'fields_map': {
                'oil_temperature_after': 'SM_Exgauster\\[2:42]',
                'oil_temperature_before': 'SM_Exgauster\\[2:41]',
                'water_temperature_after': 'SM_Exgauster\\[2:37]',
                'water_temperature_before': 'SM_Exgauster\\[2:36]',
            }
        },
        'gas_manifold': {
            '_id': ObjectId(),
            'name': 'Газовый коллектор',
            'fields_map': {
                'temperature_before': 'SM_Exgauster\\[2:24]',
                'underpressure_before': 'SM_Exgauster\\[2:61]',
            }
        },
        'valve_position': {
            '_id': ObjectId(),
            'name': 'Положение задвижки',
            'fields_map': {
                'gas_valve_closed': 'SM_Exgauster\\[4.1]',
                'gas_valve_open': 'SM_Exgauster\\[4.2]',
                'gas_valve_position': 'SM_Exgauster\\[4:6]',
            }
        },
        'main_drive': {
            '_id': ObjectId(),
            'name': 'Главный привод',
            'fields_map': {
                'rotor_current': 'SM_Exgauster\\[4:2]',
                'rotor_voltage': 'SM_Exgauster\\[4:4]',
                'stator_current': 'SM_Exgauster\\[4:3]',
                'stator_voltage': 'SM_Exgauster\\[4:5]',
            }
        },
        'oil_system': {
            '_id': ObjectId(),
            'name': 'Маслосистема',
            'fields_map': {
                'oil_level': 'SM_Exgauster\\[4:0]',
                'oil_pressure': 'SM_Exgauster\\[4:1]',
            }
        },
        'exgauster_work': {
            '_id': ObjectId(),
            'name': 'Работа эксгаустера',
            'fields_map': {
                'work': 'SM_Exgauster\\[2.0]',
            }
        },

    },
    {
        'number': 2,
        'name': 'У-172',
        'bearings_big': [
            {
                '_id': ObjectId(),
                'number': 1,
                'name': 'Подшипник 1',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:43]',
                    'temperature_alarm_max': 'SM_Exgauster\\[2:101]',
                    'temperature_alarm_min': 'SM_Exgauster\\[2:110]',
                    'temperature_warning_max': 'SM_Exgauster\\[2:119]',
                    'temperature_warning_min': 'SM_Exgauster\\[2:128]',
                    'vibration_axial': 'SM_Exgauster\\[2:14]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[2:187]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[2:199]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[2:211]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[2:223]',
                    'vibration_horizontal': 'SM_Exgauster\\[2:12]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[2:185]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[2:197]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[2:209]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[2:221]',
                    'vibration_vertical': 'SM_Exgauster\\[2:13]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[2:186]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[2:198]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[2:210]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[2:222]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 2,
                'name': 'Подшипник 2',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:44]',
                    'temperature_alarm_max': 'SM_Exgauster\\[2:102]',
                    'temperature_alarm_min': 'SM_Exgauster\\[2:111]',
                    'temperature_warning_max': 'SM_Exgauster\\[2:120]',
                    'temperature_warning_min': 'SM_Exgauster\\[2:129]',
                    'vibration_axial': 'SM_Exgauster\\[2:17]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[2:190]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[2:202]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[2:214]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[2:226]',
                    'vibration_horizontal': 'SM_Exgauster\\[2:15]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[2:188]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[2:200]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[2:212]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[2:224]',
                    'vibration_vertical': 'SM_Exgauster\\[2:16]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[2:189]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[2:201]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[2:213]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[2:225]',

                }
            },
            {
                '_id': ObjectId(),
                'number': 7,
                'name': 'Подшипник 7',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:50]',
                    'temperature_alarm_max': 'SM_Exgauster\\[2:107]',
                    'temperature_alarm_min': 'SM_Exgauster\\[2:116]',
                    'temperature_warning_max': 'SM_Exgauster\\[2:125]',
                    'temperature_warning_min': 'SM_Exgauster\\[2:134]',
                    'vibration_axial': 'SM_Exgauster\\[2:20]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[2:193]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[2:205]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[2:217]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[2:229]',
                    'vibration_horizontal': 'SM_Exgauster\\[2:18]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[2:191]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[2:203]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[2:215]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[2:227]',
                    'vibration_vertical': 'SM_Exgauster\\[2:19]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[2:192]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[2:204]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[2:216]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[2:228]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 8,
                'name': 'Подшипник 8',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:51]',
                    'temperature_alarm_max': 'SM_Exgauster\\[2:108]',
                    'temperature_alarm_min': 'SM_Exgauster\\[2:117]',
                    'temperature_warning_max': 'SM_Exgauster\\[2:126]',
                    'temperature_warning_min': 'SM_Exgauster\\[2:135]',
                    'vibration_axial': 'SM_Exgauster\\[2:23]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[2:196]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[2:208]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[2:220]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[2:232]',
                    'vibration_horizontal': 'SM_Exgauster\\[2:21]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[2:194]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[2:206]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[2:218]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[2:230]',
                    'vibration_vertical': 'SM_Exgauster\\[2:22]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[2:195]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[2:207]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[2:219]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[2:231]',

                }
            },
        ],
        'bearings_small': [
            {
                '_id': ObjectId(),
                'number': 3,
                'name': 'Подшипник 3',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:45]',
                    'alarm_max': 'SM_Exgauster\\[2:103]',
                    'alarm_min': 'SM_Exgauster\\[2:112]',
                    'warning_max': 'SM_Exgauster\\[2:121]',
                    'warning_min': 'SM_Exgauster\\[2:130]',
                }

            },
            {
                '_id': ObjectId(),
                'number': 4,
                'name': 'Подшипник 4',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:47]',
                    'alarm_max': 'SM_Exgauster\\[2:104]',
                    'alarm_min': 'SM_Exgauster\\[2:113]',
                    'warning_max': 'SM_Exgauster\\[2:122]',
                    'warning_min': 'SM_Exgauster\\[2:131]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 5,
                'name': 'Подшипник 5',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:48]',
                    'alarm_max': 'SM_Exgauster\\[2:105]',
                    'alarm_min': 'SM_Exgauster\\[2:114]',
                    'warning_max': 'SM_Exgauster\\[2:123]',
                    'warning_min': 'SM_Exgauster\\[2:132]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 6,
                'name': 'Подшипник 6',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:49]',
                    'alarm_max': 'SM_Exgauster\\[2:106]',
                    'alarm_min': 'SM_Exgauster\\[2:115]',
                    'warning_max': 'SM_Exgauster\\[2:124]',
                    'warning_min': 'SM_Exgauster\\[2:133]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 9,
                'name': 'Подшипник 9',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[2:52]',
                    'alarm_max': 'SM_Exgauster\\[2:109]',
                    'alarm_min': 'SM_Exgauster\\[2:118]',
                    'warning_max': 'SM_Exgauster\\[2:127]',
                    'warning_min': 'SM_Exgauster\\[2:136]',
                }
            },
        ],
        'cooler': {
            '_id': ObjectId(),
            'name': 'Охладитель',
            'fields_map': {
                'oil_temperature_after': 'SM_Exgauster\\[2:60]',
                'oil_temperature_before': 'SM_Exgauster\\[2:59]',
                'water_temperature_after': 'SM_Exgauster\\[2:54]',
                'water_temperature_before': 'SM_Exgauster\\[2:53]',
            }
        },
        'gas_manifold': {
            '_id': ObjectId(),
            'name': 'Газовый коллектор',
            'fields_map': {
                'temperature_before': 'SM_Exgauster\\[2:25]',
                'underpressure_before': 'SM_Exgauster\\[2:62]',
            }
        },
        'valve_position': {
            '_id': ObjectId(),
            'name': 'Положение задвижки',
            'fields_map': {
                'gas_valve_closed': 'SM_Exgauster\\[4.6]',
                'gas_valve_open': 'SM_Exgauster\\[4.7]',
                'gas_valve_position': 'SM_Exgauster\\[4:13]',
            }
        },
        'main_drive': {
            '_id': ObjectId(),
            'name': 'Главный привод',
            'fields_map': {
                'rotor_current': 'SM_Exgauster\\[4:9]',
                'rotor_voltage': 'SM_Exgauster\\[4:11]',
                'stator_current': 'SM_Exgauster\\[4:10]',
                'stator_voltage': 'SM_Exgauster\\[4:12]',

            }
        },
        'oil_system': {
            '_id': ObjectId(),
            'name': 'Маслосистема',
            'fields_map': {
                'oil_level': 'SM_Exgauster\\[4:7]',
                'oil_pressure': 'SM_Exgauster\\[4:8]',

            }
        },
        'exgauster_work': {
            '_id': ObjectId(),
            'name': 'Работа эксгаустера',
            'fields_map': {
                'work': 'SM_Exgauster\\[2.1]',
            }
        },

    },
    {
        'number': 3,
        'name': 'Ф-171',
        'bearings_big': [
            {
                '_id': ObjectId(),
                'number': 1,
                'name': 'Подшипник 1',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:27]',
                    'temperature_alarm_max': 'SM_Exgauster\\[0:63]',
                    'temperature_alarm_min': 'SM_Exgauster\\[0:72]',
                    'temperature_warning_max': 'SM_Exgauster\\[0:81]',
                    'temperature_warning_min': 'SM_Exgauster\\[0:90]',
                    'vibration_axial': 'SM_Exgauster\\[0:2]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[0:137]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[0:149]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[0:161]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[0:173]',
                    'vibration_horizontal': 'SM_Exgauster\\[0:0]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[0:135]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[0:147]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[0:159]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[0:171]',
                    'vibration_vertical': 'SM_Exgauster\\[0:1]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[0:136]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[0:148]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[0:160]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[0:172]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 2,
                'name': 'Подшипник 2',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:28]',
                    'temperature_alarm_max': 'SM_Exgauster\\[0:64]',
                    'temperature_alarm_min': 'SM_Exgauster\\[0:73]',
                    'temperature_warning_max': 'SM_Exgauster\\[0:82]',
                    'temperature_warning_min': 'SM_Exgauster\\[0:91]',
                    'vibration_axial': 'SM_Exgauster\\[0:5]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[0:140]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[0:152]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[0:164]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[0:176]',
                    'vibration_horizontal': 'SM_Exgauster\\[0:3]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[0:138]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[0:150]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[0:162]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[0:174]',
                    'vibration_vertical': 'SM_Exgauster\\[0:4]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[0:139]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[0:151]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[0:163]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[0:175]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 7,
                'name': 'Подшипник 7',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:33]',
                    'temperature_alarm_max': 'SM_Exgauster\\[0:69]',
                    'temperature_alarm_min': 'SM_Exgauster\\[0:78]',
                    'temperature_warning_max': 'SM_Exgauster\\[0:87]',
                    'temperature_warning_min': 'SM_Exgauster\\[0:96]',
                    'vibration_axial': 'SM_Exgauster\\[0:8]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[0:143]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[0:155]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[0:167]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[0:179]',
                    'vibration_horizontal': 'SM_Exgauster\\[0:6]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[0:141]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[0:153]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[0:165]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[0:177]',
                    'vibration_vertical': 'SM_Exgauster\\[0:7]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[0:142]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[0:154]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[0:166]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[0:178]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 8,
                'name': 'Подшипник 8',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:34]',
                    'temperature_alarm_max': 'SM_Exgauster\\[0:70]',
                    'temperature_alarm_min': 'SM_Exgauster\\[0:79]',
                    'temperature_warning_max': 'SM_Exgauster\\[0:88]',
                    'temperature_warning_min': 'SM_Exgauster\\[0:97]',
                    'vibration_axial': 'SM_Exgauster\\[0:11]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[0:146]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[0:158]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[0:170]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[0:182]',
                    'vibration_horizontal': 'SM_Exgauster\\[0:9]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[0:144]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[0:156]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[0:168]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[0:180]',
                    'vibration_vertical': 'SM_Exgauster\\[0:10]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[0:145]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[0:157]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[0:169]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[0:181]',
                }
            },
        ],
        'bearings_small': [
            {
                '_id': ObjectId(),
                'number': 3,
                'name': 'Подшипник 3',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:29]',
                    'alarm_max': 'SM_Exgauster\\[0:65]',
                    'alarm_min': 'SM_Exgauster\\[0:74]',
                    'warning_max': 'SM_Exgauster\\[0:83]',
                    'warning_min': 'SM_Exgauster\\[0:92]',
                }

            },
            {
                '_id': ObjectId(),
                'number': 4,
                'name': 'Подшипник 4',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:30]',
                    'alarm_max': 'SM_Exgauster\\[0:66]',
                    'alarm_min': 'SM_Exgauster\\[0:75]',
                    'warning_max': 'SM_Exgauster\\[0:84]',
                    'warning_min': 'SM_Exgauster\\[0:93]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 5,
                'name': 'Подшипник 5',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:31]',
                    'alarm_max': 'SM_Exgauster\\[0:67]',
                    'alarm_min': 'SM_Exgauster\\[0:76]',
                    'warning_max': 'SM_Exgauster\\[0:85]',
                    'warning_min': 'SM_Exgauster\\[0:94]',

                }
            },
            {
                '_id': ObjectId(),
                'number': 6,
                'name': 'Подшипник 6',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:32]',
                    'alarm_max': 'SM_Exgauster\\[0:68]',
                    'alarm_min': 'SM_Exgauster\\[0:77]',
                    'warning_max': 'SM_Exgauster\\[0:86]',
                    'warning_min': 'SM_Exgauster\\[0:95]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 9,
                'name': 'Подшипник 9',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:35]',
                    'alarm_max': 'SM_Exgauster\\[0:71]',
                    'alarm_min': 'SM_Exgauster\\[0:80]',
                    'warning_max': 'SM_Exgauster\\[0:89]',
                    'warning_min': 'SM_Exgauster\\[0:98]',
                }
            },
        ],
        'cooler': {
            '_id': ObjectId(),
            'name': 'Охладитель',
            'fields_map': {
                'oil_temperature_after': 'SM_Exgauster\\[0:42]',
                'oil_temperature_before': 'SM_Exgauster\\[0:41]',
                'water_temperature_after': 'SM_Exgauster\\[0:37]',
                'water_temperature_before': 'SM_Exgauster\\[0:36]',
            }
        },
        'gas_manifold': {
            '_id': ObjectId(),
            'name': 'Газовый коллектор',
            'fields_map': {
                'temperature_before': 'SM_Exgauster\\[0:24]',
                'underpressure_before': 'SM_Exgauster\\[0:61]',
            }
        },
        'valve_position': {
            '_id': ObjectId(),
            'name': 'Положение задвижки',
            'fields_map': {
                'gas_valve_closed': 'SM_Exgauster\\[1.1]',
                'gas_valve_open': 'SM_Exgauster\\[1.2]',
                'gas_valve_position': 'SM_Exgauster\\[1:6]',
            }
        },
        'main_drive': {
            '_id': ObjectId(),
            'name': 'Главный привод',
            'fields_map': {
                'rotor_current': 'SM_Exgauster\\[1:2]',
                'rotor_voltage': 'SM_Exgauster\\[1:4]',
                'stator_current': 'SM_Exgauster\\[1:3]',
                'stator_voltage': 'SM_Exgauster\\[1:5]',
            }
        },
        'oil_system': {
            '_id': ObjectId(),
            'name': 'Маслосистема',
            'fields_map': {
                'oil_level': 'SM_Exgauster\\[1:0]',
                'oil_pressure': 'SM_Exgauster\\[1:1]',
            }
        },
        'exgauster_work': {
            '_id': ObjectId(),
            'name': 'Работа эксгаустера',
            'fields_map': {
                'work': 'SM_Exgauster\\[0.0]',
            }
        },

    },
    {
        'number': 4,
        'name': 'Ф-172',
        'bearings_big': [
            {
                '_id': ObjectId(),
                'number': 1,
                'name': 'Подшипник 1',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:43]',
                    'temperature_alarm_max': 'SM_Exgauster\\[0:99]',
                    'temperature_alarm_min': 'SM_Exgauster\\[0:108]',
                    'temperature_warning_max': 'SM_Exgauster\\[0:117]',
                    'temperature_warning_min': 'SM_Exgauster\\[0:126]',
                    'vibration_axial': 'SM_Exgauster\\[0:14]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[0:185]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[0:197]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[0:209]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[0:221]',
                    'vibration_horizontal': 'SM_Exgauster\\[0:12]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[0:183]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[0:195]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[0:207]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[0:219]',
                    'vibration_vertical': 'SM_Exgauster\\[0:13]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[0:184]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[0:196]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[0:208]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[0:220]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 2,
                'name': 'Подшипник 2',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:44]',
                    'temperature_alarm_max': 'SM_Exgauster\\[0:100]',
                    'temperature_alarm_min': 'SM_Exgauster\\[0:109]',
                    'temperature_warning_max': 'SM_Exgauster\\[0:118]',
                    'temperature_warning_min': 'SM_Exgauster\\[0:127]',
                    'vibration_axial': 'SM_Exgauster\\[0:17]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[0:188]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[0:200]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[0:212]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[0:224]',
                    'vibration_horizontal': 'SM_Exgauster\\[0:15]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[0:186]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[0:198]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[0:210]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[0:222]',
                    'vibration_vertical': 'SM_Exgauster\\[0:16]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[0:187]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[0:199]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[0:211]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[0:223]',
                }
            },
            {
                '_id': ObjectId(),
                'name': 'Подшипник 7',
                'number': 7,
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:50]',
                    'temperature_alarm_max': 'SM_Exgauster\\[0:105]',
                    'temperature_alarm_min': 'SM_Exgauster\\[0:114]',
                    'temperature_warning_max': 'SM_Exgauster\\[0:123]',
                    'temperature_warning_min': 'SM_Exgauster\\[0:132]',
                    'vibration_axial': 'SM_Exgauster\\[0:20]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[0:191]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[0:203]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[0:215]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[0:227]',
                    'vibration_horizontal': 'SM_Exgauster\\[0:18]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[0:189]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[0:201]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[0:213]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[0:225]',
                    'vibration_vertical': 'SM_Exgauster\\[0:19]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[0:190]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[0:202]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[0:214]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[0:226]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 8,
                'name': 'Подшипник 8',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:51]',
                    'temperature_alarm_max': 'SM_Exgauster\\[0:106]',
                    'temperature_alarm_min': 'SM_Exgauster\\[0:115]',
                    'temperature_warning_max': 'SM_Exgauster\\[0:124]',
                    'temperature_warning_min': 'SM_Exgauster\\[0:133]',
                    'vibration_axial': 'SM_Exgauster\\[0:23]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[0:194]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[0:206]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[0:218]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[0:230]',
                    'vibration_horizontal': 'SM_Exgauster\\[0:21]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[0:192]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[0:204]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[0:216]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[0:228]',
                    'vibration_vertical': 'SM_Exgauster\\[0:22]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[0:193]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[0:205]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[0:217]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[0:229]',
                }
            },
        ],
        'bearings_small': [
            {
                '_id': ObjectId(),
                'number': 3,
                'name': 'Подшипник 3',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:45]',
                    'alarm_max': 'SM_Exgauster\\[0:101]',
                    'alarm_min': 'SM_Exgauster\\[0:110]',
                    'warning_max': 'SM_Exgauster\\[0:119]',
                    'warning_min': 'SM_Exgauster\\[0:128]',
                }

            },
            {
                '_id': ObjectId(),
                'number': 4,
                'name': 'Подшипник 4',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:47]',
                    'alarm_max': 'SM_Exgauster\\[0:102]',
                    'alarm_min': 'SM_Exgauster\\[0:111]',
                    'warning_max': 'SM_Exgauster\\[0:120]',
                    'warning_min': 'SM_Exgauster\\[0:129]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 5,
                'name': 'Подшипник 5',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:48]',
                    'alarm_max': 'SM_Exgauster\\[0:103]',
                    'alarm_min': 'SM_Exgauster\\[0:112]',
                    'warning_max': 'SM_Exgauster\\[0:121]',
                    'warning_min': 'SM_Exgauster\\[0:130]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 6,
                'name': 'Подшипник 6',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:49]',
                    'alarm_max': 'SM_Exgauster\\[0:104]',
                    'alarm_min': 'SM_Exgauster\\[0:113]',
                    'warning_max': 'SM_Exgauster\\[0:122]',
                    'warning_min': 'SM_Exgauster\\[0:131]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 9,
                'name': 'Подшипник 9',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[0:52]',
                    'alarm_max': 'SM_Exgauster\\[0:107]',
                    'alarm_min': 'SM_Exgauster\\[0:116]',
                    'warning_max': 'SM_Exgauster\\[0:125]',
                    'warning_min': 'SM_Exgauster\\[0:134]',
                }
            },
        ],
        'cooler': {
            '_id': ObjectId(),
            'name': 'Охладитель',
            'fields_map': {
                'oil_temperature_after': 'SM_Exgauster\\[0:60]',
                'oil_temperature_before': 'SM_Exgauster\\[0:59]',
                'water_temperature_after': 'SM_Exgauster\\[0:54]',
                'water_temperature_before': 'SM_Exgauster\\[0:53]',
            }
        },
        'gas_manifold': {
            '_id': ObjectId(),
            'name': 'Газовый коллектор',
            'fields_map': {
                'temperature_before': 'SM_Exgauster\\[0:25]',
                'underpressure_before': 'SM_Exgauster\\[0:62]',
            }
        },
        'valve_position': {
            '_id': ObjectId(),
            'name': 'Положение задвижки',
            'fields_map': {
                'gas_valve_closed': 'SM_Exgauster\\[1.6]',
                'gas_valve_open': 'SM_Exgauster\\[1.7]',
                'gas_valve_position': 'SM_Exgauster\\[1:13]',
            }
        },
        'main_drive': {
            '_id': ObjectId(),
            'name': 'Главный привод',
            'fields_map': {
                'rotor_current': 'SM_Exgauster\\[1:9]',
                'rotor_voltage': 'SM_Exgauster\\[1:11]',
                'stator_current': 'SM_Exgauster\\[1:10]',
                'stator_voltage': 'SM_Exgauster\\[1:12]',
            }
        },
        'oil_system': {
            '_id': ObjectId(),
            'name': 'Маслосистема',
            'fields_map': {
                'oil_level': 'SM_Exgauster\\[1:7]',
                'oil_pressure': 'SM_Exgauster\\[1:8]',
            }
        },
        'exgauster_work': {
            '_id': ObjectId(),
            'name': 'Работа эксгаустера',
            'fields_map': {
                'work': 'SM_Exgauster\\[0.1]',
            }
        },

    },
    {
        'number': 5,
        'name': 'X-171',
        'bearings_big': [
            {
                '_id': ObjectId(),
                'number': 1,
                'name': 'Подшипник 1',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:27]',
                    'temperature_alarm_max': 'SM_Exgauster\\[3:63]',
                    'temperature_alarm_min': 'SM_Exgauster\\[3:72]',
                    'temperature_warning_max': 'SM_Exgauster\\[3:81]',
                    'temperature_warning_min': 'SM_Exgauster\\[3:90]',
                    'vibration_axial': 'SM_Exgauster\\[3:2]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[3:137]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[3:149]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[3:161]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[3:173]',
                    'vibration_horizontal': 'SM_Exgauster\\[3:0]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[3:135]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[3:147]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[3:159]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[3:171]',
                    'vibration_vertical': 'SM_Exgauster\\[3:1]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[3:136]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[3:148]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[3:160]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[3:172]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 2,
                'name': 'Подшипник 2',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:28]',
                    'temperature_alarm_max': 'SM_Exgauster\\[3:64]',
                    'temperature_alarm_min': 'SM_Exgauster\\[3:73]',
                    'temperature_warning_max': 'SM_Exgauster\\[3:82]',
                    'temperature_warning_min': 'SM_Exgauster\\[3:91]',
                    'vibration_axial': 'SM_Exgauster\\[3:5]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[3:140]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[3:152]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[3:164]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[3:176]',
                    'vibration_horizontal': 'SM_Exgauster\\[3:3]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[3:138]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[3:150]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[3:162]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[3:174]',
                    'vibration_vertical': 'SM_Exgauster\\[3:4]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[3:139]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[3:151]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[3:163]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[3:175]',
                }
            },
            {
                '_id': ObjectId(),
                'name': 'Подшипник 7',
                'number': 7,
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:33]',
                    'temperature_alarm_max': 'SM_Exgauster\\[3:69]',
                    'temperature_alarm_min': 'SM_Exgauster\\[3:78]',
                    'temperature_warning_max': 'SM_Exgauster\\[3:87]',
                    'temperature_warning_min': 'SM_Exgauster\\[3:96]',
                    'vibration_axial': 'SM_Exgauster\\[3:8]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[3:143]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[3:155]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[3:167]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[3:179]',
                    'vibration_horizontal': 'SM_Exgauster\\[3:6]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[3:141]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[3:153]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[3:165]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[3:177]',
                    'vibration_vertical': 'SM_Exgauster\\[3:7]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[3:142]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[3:154]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[3:166]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[3:178]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 8,
                'name': 'Подшипник 8',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:34]',
                    'temperature_alarm_max': 'SM_Exgauster\\[3:70]',
                    'temperature_alarm_min': 'SM_Exgauster\\[3:79]',
                    'temperature_warning_max': 'SM_Exgauster\\[3:88]',
                    'temperature_warning_min': 'SM_Exgauster\\[3:97]',
                    'vibration_axial': 'SM_Exgauster\\[3:11]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[3:146]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[3:158]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[3:170]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[3:182]',
                    'vibration_horizontal': 'SM_Exgauster\\[3:9]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[3:144]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[3:156]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[3:168]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[3:180]',
                    'vibration_vertical': 'SM_Exgauster\\[3:10]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[3:145]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[3:157]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[3:169]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[3:181]',
                }
            },
        ],
        'bearings_small': [
            {
                '_id': ObjectId(),
                'number': 3,
                'name': 'Подшипник 3',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:29]',
                    'alarm_max': 'SM_Exgauster\\[3:65]',
                    'alarm_min': 'SM_Exgauster\\[3:74]',
                    'warning_max': 'SM_Exgauster\\[3:83]',
                    'warning_min': 'SM_Exgauster\\[3:92]',
                }

            },
            {
                '_id': ObjectId(),
                'number': 4,
                'name': 'Подшипник 4',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:30]',
                    'alarm_max': 'SM_Exgauster\\[3:66]',
                    'alarm_min': 'SM_Exgauster\\[3:75]',
                    'warning_max': 'SM_Exgauster\\[3:84]',
                    'warning_min': 'SM_Exgauster\\[3:93]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 5,
                'name': 'Подшипник 5',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:31]',
                    'alarm_max': 'SM_Exgauster\\[3:67]',
                    'alarm_min': 'SM_Exgauster\\[3:76]',
                    'warning_max': 'SM_Exgauster\\[3:85]',
                    'warning_min': 'SM_Exgauster\\[3:94]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 6,
                'name': 'Подшипник 6',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:32]',
                    'alarm_max': 'SM_Exgauster\\[3:68]',
                    'alarm_min': 'SM_Exgauster\\[3:77]',
                    'warning_max': 'SM_Exgauster\\[3:86]',
                    'warning_min': 'SM_Exgauster\\[3:95]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 9,
                'name': 'Подшипник 9',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:35]',
                    'alarm_max': 'SM_Exgauster\\[3:71]',
                    'alarm_min': 'SM_Exgauster\\[3:80]',
                    'warning_max': 'SM_Exgauster\\[3:89]',
                    'warning_min': 'SM_Exgauster\\[3:98]',
                }
            },
        ],
        'cooler': {
            '_id': ObjectId(),
            'name': 'Охладитель',
            'fields_map': {
                'oil_temperature_after': 'SM_Exgauster\\[3:42]',
                'oil_temperature_before': 'SM_Exgauster\\[3:41]',
                'water_temperature_after': 'SM_Exgauster\\[3:37]',
                'water_temperature_before': 'SM_Exgauster\\[3:36]',
            }
        },
        'gas_manifold': {
            '_id': ObjectId(),
            'name': 'Газовый коллектор',
            'fields_map': {
                'temperature_before': 'SM_Exgauster\\[3:24]',
                'underpressure_before': 'SM_Exgauster\\[3:61]',
            }
        },
        'valve_position': {
            '_id': ObjectId(),
            'name': 'Положение задвижки',
            'fields_map': {
                'gas_valve_closed': 'SM_Exgauster\\[5.1]',
                'gas_valve_open': 'SM_Exgauster\\[5.2]',
                'gas_valve_position': 'SM_Exgauster\\[5:6]',
            }
        },
        'main_drive': {
            '_id': ObjectId(),
            'name': 'Главный привод',
            'fields_map': {
                'rotor_current': 'SM_Exgauster\\[5:2]',
                'rotor_voltage': 'SM_Exgauster\\[5:4]',
                'stator_current': 'SM_Exgauster\\[5:3]',
                'stator_voltage': 'SM_Exgauster\\[5:5]',
            }
        },
        'oil_system': {
            '_id': ObjectId(),
            'name': 'Маслосистема',
            'fields_map': {
                'oil_level': 'SM_Exgauster\\[5:0]',
                'oil_pressure': 'SM_Exgauster\\[5:1]',
            }
        },
        'exgauster_work': {
            '_id': ObjectId(),
            'name': 'Работа эксгаустера',
            'fields_map': {
                'work': 'SM_Exgauster\\[3.0]',
            }
        },

    },
    {
        'number': 6,
        'name': 'X-172',
        'bearings_big': [
            {
                '_id': ObjectId(),
                'number': 1,
                'name': 'Подшипник 1',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:43]',
                    'temperature_alarm_max': 'SM_Exgauster\\[3:99]',
                    'temperature_alarm_min': 'SM_Exgauster\\[3:108]',
                    'temperature_warning_max': 'SM_Exgauster\\[3:117]',
                    'temperature_warning_min': 'SM_Exgauster\\[3:126]',
                    'vibration_axial': 'SM_Exgauster\\[3:14]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[3:185]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[3:197]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[3:209]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[3:221]',
                    'vibration_horizontal': 'SM_Exgauster\\[3:12]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[3:183]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[3:195]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[3:207]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[3:219]',
                    'vibration_vertical': 'SM_Exgauster\\[3:13]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[3:184]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[3:196]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[3:208]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[3:220]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 2,
                'name': 'Подшипник 2',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:44]',
                    'temperature_alarm_max': 'SM_Exgauster\\[3:100]',
                    'temperature_alarm_min': 'SM_Exgauster\\[3:109]',
                    'temperature_warning_max': 'SM_Exgauster\\[3:118]',
                    'temperature_warning_min': 'SM_Exgauster\\[3:127]',
                    'vibration_axial': 'SM_Exgauster\\[3:17]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[3:188]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[3:200]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[3:212]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[3:224]',
                    'vibration_horizontal': 'SM_Exgauster\\[3:15]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[3:186]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[3:198]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[3:210]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[3:222]',
                    'vibration_vertical': 'SM_Exgauster\\[3:16]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[3:187]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[3:199]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[3:211]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[3:223]',
                }
            },
            {
                '_id': ObjectId(),
                'name': 'Подшипник 7',
                'number': 7,
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:50]',
                    'temperature_alarm_max': 'SM_Exgauster\\[3:105]',
                    'temperature_alarm_min': 'SM_Exgauster\\[3:114]',
                    'temperature_warning_max': 'SM_Exgauster\\[3:123]',
                    'temperature_warning_min': 'SM_Exgauster\\[3:132]',
                    'vibration_axial': 'SM_Exgauster\\[3:20]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[3:191]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[3:203]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[3:215]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[3:227]',
                    'vibration_horizontal': 'SM_Exgauster\\[3:18]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[3:189]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[3:201]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[3:213]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[3:225]',
                    'vibration_vertical': 'SM_Exgauster\\[3:19]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[3:190]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[3:202]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[3:214]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[3:226]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 8,
                'name': 'Подшипник 8',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:51]',
                    'temperature_alarm_max': 'SM_Exgauster\\[3:106]',
                    'temperature_alarm_min': 'SM_Exgauster\\[3:115]',
                    'temperature_warning_max': 'SM_Exgauster\\[3:124]',
                    'temperature_warning_min': 'SM_Exgauster\\[3:133]',
                    'vibration_axial': 'SM_Exgauster\\[3:23]',
                    'vibration_axial_alarm_max': 'SM_Exgauster\\[3:194]',
                    'vibration_axial_alarm_min': 'SM_Exgauster\\[3:206]',
                    'vibration_axial_warning_max': 'SM_Exgauster\\[3:218]',
                    'vibration_axial_warning_min': 'SM_Exgauster\\[3:230]',
                    'vibration_horizontal': 'SM_Exgauster\\[3:21]',
                    'vibration_horizontal_alarm_max': 'SM_Exgauster\\[3:192]',
                    'vibration_horizontal_alarm_min': 'SM_Exgauster\\[3:204]',
                    'vibration_horizontal_warning_max': 'SM_Exgauster\\[3:216]',
                    'vibration_horizontal_warning_min': 'SM_Exgauster\\[3:228]',
                    'vibration_vertical': 'SM_Exgauster\\[3:22]',
                    'vibration_vertical_alarm_max': 'SM_Exgauster\\[3:193]',
                    'vibration_vertical_alarm_min': 'SM_Exgauster\\[3:205]',
                    'vibration_vertical_warning_max': 'SM_Exgauster\\[3:217]',
                    'vibration_vertical_warning_min': 'SM_Exgauster\\[3:229]',
                }
            },
        ],
        'bearings_small': [
            {
                '_id': ObjectId(),
                'number': 3,
                'name': 'Подшипник 3',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:45]',
                    'alarm_max': 'SM_Exgauster\\[3:101]',
                    'alarm_min': 'SM_Exgauster\\[3:110]',
                    'warning_max': 'SM_Exgauster\\[3:119]',
                    'warning_min': 'SM_Exgauster\\[3:128]',
                }

            },
            {
                '_id': ObjectId(),
                'number': 4,
                'name': 'Подшипник 4',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:47]',
                    'alarm_max': 'SM_Exgauster\\[3:102]',
                    'alarm_min': 'SM_Exgauster\\[3:111]',
                    'warning_max': 'SM_Exgauster\\[3:120]',
                    'warning_min': 'SM_Exgauster\\[3:129]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 5,
                'name': 'Подшипник 5',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:48]',
                    'alarm_max': 'SM_Exgauster\\[3:103]',
                    'alarm_min': 'SM_Exgauster\\[3:112]',
                    'warning_max': 'SM_Exgauster\\[3:121]',
                    'warning_min': 'SM_Exgauster\\[3:130]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 6,
                'name': 'Подшипник 6',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:49]',
                    'alarm_max': 'SM_Exgauster\\[3:104]',
                    'alarm_min': 'SM_Exgauster\\[3:113]',
                    'warning_max': 'SM_Exgauster\\[3:122]',
                    'warning_min': 'SM_Exgauster\\[3:131]',
                }
            },
            {
                '_id': ObjectId(),
                'number': 9,
                'name': 'Подшипник 9',
                'fields_map': {
                    'temperature': 'SM_Exgauster\\[3:52]',
                    'alarm_max': 'SM_Exgauster\\[3:107]',
                    'alarm_min': 'SM_Exgauster\\[3:116]',
                    'warning_max': 'SM_Exgauster\\[3:125]',
                    'warning_min': 'SM_Exgauster\\[3:134]',
                }
            },
        ],
        'cooler': {
            '_id': ObjectId(),
            'name': 'Охладитель',
            'fields_map': {
                'oil_temperature_after': 'SM_Exgauster\\[3:60]',
                'oil_temperature_before': 'SM_Exgauster\\[3:59]',
                'water_temperature_after': 'SM_Exgauster\\[3:54]',
                'water_temperature_before': 'SM_Exgauster\\[3:53]',
            }
        },
        'gas_manifold': {
            '_id': ObjectId(),
            'name': 'Газовый коллектор',
            'fields_map': {
                'temperature_before': 'SM_Exgauster\\[3:25]',
                'underpressure_before': 'SM_Exgauster\\[3:62]',
            }
        },
        'valve_position': {
            '_id': ObjectId(),
            'name': 'Положение задвижки',
            'fields_map': {
                'gas_valve_closed': 'SM_Exgauster\\[5.6]',
                'gas_valve_open': 'SM_Exgauster\\[5.7]',
                'gas_valve_position': 'SM_Exgauster\\[5:13]',
            }
        },
        'main_drive': {
            '_id': ObjectId(),
            'name': 'Главный привод',
            'fields_map': {
                'rotor_current': 'SM_Exgauster\\[5:9]',
                'rotor_voltage': 'SM_Exgauster\\[5:11]',
                'stator_current': 'SM_Exgauster\\[5:10]',
                'stator_voltage': 'SM_Exgauster\\[5:12]',
            }
        },
        'oil_system': {
            '_id': ObjectId(),
            'name': 'Маслосистема',
            'fields_map': {
                'oil_level': 'SM_Exgauster\\[5:7]',
                'oil_pressure': 'SM_Exgauster\\[5:8]',
            }
        },
        'exgauster_work': {
            '_id': ObjectId(),
            'name': 'Работа эксгаустера',
            'fields_map': {
                'work': 'SM_Exgauster\\[3.1]',
            }
        },
    }

]

asyncio.run(write_to_mongo(objs))
