# NeuroHack Team

Проект хакатона ЕВРАЗА 2.0

![image](https://iv.kommersant.ru/gboxtexts/sp_com/logos/019.jpg)

## Архитектура системы
https://miro.com/welcomeonboard/MmdidW1SVHBSQWVKRnF2d2Vqc3RndG5ueUtUTFFhb05IdXRjYUhxanJzNmhJcTJRcXRmelhSWmRRUVVnTzc5MHwzMDc0NDU3MzQ4MzAyNzYyNDExfDI=?share_link_id=283531829997

## Запуск
```
docker-compose up
```

Фронт не в докере, чтобы проверить:
```
cd ui
npm run serve
```

## ТЗ
https://pgenesis.notion.site/d6ef73e9d00143fdbfa8a9b6143d2905

backendUrl: "http://localhost:88/api",

webSocketUrl: "wss://localhost:8001"


PS. Если не грузятся данные просьба ребутнуть контейнер

### ENTRYPOINTS:

- <b>/exgausters</b> - отдает все данные о всех машинах (текущие)
- <b>/exgausters/{pk: int}</b> - отдает все данные по конкретной машине (текущие + переключалка)


### Используемые технологии 

![image](https://img.shields.io/badge/Python-004088?logo=Python)
![image](https://img.shields.io/badge/FastApi-2ac8d4?logo=fastapi)
![image](https://img.shields.io/badge/Postgresql-yellow?logo=Postgresql)
![image](https://img.shields.io/badge/sqlalchemy-2aa1d4)
![image](https://img.shields.io/badge/pydantic-2ad482)
![image](https://img.shields.io/badge/MongoDB-DF0067?logo=Mongodb)
![image](https://img.shields.io/badge/Kafka-2aa1d4?logo=kafka)

![image](https://camo.githubusercontent.com/a1309b252e82434062012a8073fa9fc1416a96289b7ca11555577b9fbe1cf03e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d4a6176615363726970742d2532334637444631433f7374796c653d666c61742d737175617265266c6f676f3d6a617661736372697074266c6f676f436f6c6f723d303030303030266c6162656c436f6c6f723d25323346374446314326636f6c6f723d253233464643453541)
![image](https://img.shields.io/badge/Vue.js-114a13?logo=Vue.js)
![image](https://camo.githubusercontent.com/9a7c8c4ee62739436a191706be9f786a813dc377ce778522da198cb94874dc22/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d48544d4c352d2532334534344432373f7374796c653d666c61742d737175617265266c6f676f3d68746d6c35266c6f676f436f6c6f723d666666666666)
![image](https://camo.githubusercontent.com/19d98ab99fe0a1a5c00ef27920be3ada8548f2476877db0598960ac2a5f8788d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d435353332d2532333135373242363f7374796c653d666c61742d737175617265266c6f676f3d63737333)
