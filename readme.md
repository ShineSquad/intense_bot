# Интенсивный бот

Документация по Telegram API тут: https://core.telegram.org/bots/api

Ссылка на трансляцию: https://youtu.be/NnRT2UYkRx8

## Для создания нового бота: 
1) в приложении Telegram, найти бота: @BotFather  
2) написать ему команду (или выбрать из меню): /newbot
3) задать название и username для бота
4) скопировать токен доступа

## Для создания базовой ссылки
1) возьмите ссылку: https://api.telegram.org/bot  
2) возьмите токен авторизации, скопированный у @BotFather  
3) и получите сслылку, вида:  
	https://api.telegram.org/bot*Zdes'VashTokenAvtorizacii

## Проверяем работу
1) обратимся к боту с методом /getMe
2) добавим метод к базовой ссылке:  
	https://api.telegram.org/bot*Zdes'VashTokenAvtorizacii/getMe
3) можно вставить ссылку в строку браузера и в ответ прилетит объект:
```json
	{
		"ok":true,
		"result":{
			"id":1234567890,
			"is_bot":true,
			"first_name":"bot_title",
			"username":"username_bot",
			"can_join_groups":true,
			"can_read_all_group_messages":false,
			"supports_inline_queries":false
		}
	}
```

## python requests
Документация проекта: https://requests.readthedocs.io/en/master/

Для установки можно воспользоваться пакетным менеджером python:
```sh
pip install requests
# или
pip3 install requests
```

Для корректной работы, необходимо добавить python в переменные среды, как это сделать
можно посмотреть, например [тут](https://www.istocks.club/%D0%BA%D0%B0%D0%BA-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C-python-%D0%B2-%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%83%D1%8E-path-windows/2020-10-14/)