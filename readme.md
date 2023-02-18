## Архитектура системы
https://miro.com/welcomeonboard/MmdidW1SVHBSQWVKRnF2d2Vqc3RndG5ueUtUTFFhb05IdXRjYUhxanJzNmhJcTJRcXRmelhSWmRRUVVnTzc5MHwzMDc0NDU3MzQ4MzAyNzYyNDExfDI=?share_link_id=283531829997

## Запуск
```
docker-compose up
```

PS: Фронт еще не в докере, чтобы проверить:
```
cd ui
npm run serve
```

## ТЗ
https://pgenesis.notion.site/d6ef73e9d00143fdbfa8a9b6143d2905

backendUrl: "http://localhost:88/api",
webSocketUrl: "wss://localhost:8001"

### Ручки

- <b>/exgausters</b> - отдает все данные о всех машинах (текущие)
- <b>/exgausters/{pk: int}</b> - отдает все данные по конкретной машине (текущие)
- <b>(ws)/exgausters/{pk: int}/threads?date_start={date: DateTime}&date_start=</b> - отдает данные тредов по конкретной машине (история)

{
    ps: [id: int, description: {}, values: [{value: значение, date: момент}, {value: null, date: момент}]]
}
