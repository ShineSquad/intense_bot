import requests
import time
import json
import random

# https://core.telegram.org/bots/api#sendmessage

API_LINK = "https://api.telegram.org/bot"
TOKEN = ""
base = API_LINK + TOKEN

USER_KEYBOARD_1 = [
	["Получить"],
	["Предложить"]
]
USER_KEYBOARD_2 = [
	["Выполнил!"],
	["Не выполнил"]
]
MODERATOR_KB = [
	["Одобрить"],
	["Отменить"]
]

def getUpdates(offset):
	link = base + "/getUpdates"
	resp = requests.get(
		link,
		params={
			"offset": offset,
			"limit": 1
		}
	)

	return resp.json()

def sendMessage(chatID, text, rm=[[]]):
	link = base + "/sendMessage"
	resp = requests.get(
		link,
		params={
			"chat_id": chatID,
			"text": text,
			"reply_markup": json.dumps({
				"keyboard": rm,
				"one_time_keyboard": True
			})
		}
	)

def checkUser(chatID):
	for i in range(len(USER_DATA)):
		if USER_DATA[i]["chat_id"] == chatID:
			return i

	createNewUser(chatID)

	return len(USER_DATA)-1

def createNewUser(chatID):
	USER_DATA.append({
		"chat_id": chatID,
		"status": 0
	})

def userStatus(uID):
	return USER_DATA[uID]["status"]
def setStatus(uID, stat):
	USER_DATA[uID]["status"] = stat

USER_DATA = []
TASKS = [
	"Прыгни пять раз",
	"Достань языком до локтя",
	"Обними пять случайных людей"
]
MODERATE = []
ON_MODERATE = ""

offset = 0
moderatorID = 223074836

while True:
	data = getUpdates(offset)
	
	if len(data["result"]) > 0:
		answer = data["result"][0]
	else:
		continue

	message = answer["message"]
	chatID = message["chat"]["id"]
	userID = message["from"]["id"]
	text   = message["text"]
	
	if userID == moderatorID:
		if len(MODERATE) > 0:
			ON_MODERATE = MODERATE.pop()
			sendMessage(chatID, ON_MODERATE, MODERATOR_KB)

		if text == "Одобрить":
			TASKS.append(ON_MODERATE)
	else:
		uID = checkUser(chatID)
		if userStatus(uID) == 0:
			sendMessage(chatID, "Что будем делать?", USER_KEYBOARD_1)
			setStatus(uID, 1)
		elif userStatus(uID) == 1:
			if text == "Получить":
				taskID = random.randint(0, len(TASKS)-1)
				sendMessage(chatID, TASKS[taskID], USER_KEYBOARD_2)
				setStatus(uID, 3)
			elif text == "Предложить":
				sendMessage(chatID, "Введи задание, а я его отправлю модератору")
				setStatus(uID, 2)
			else:
				sendMessage(chatID, "Неверная команда")
		elif userStatus(uID) == 2:
			MODERATE.append(text)
			sendMessage(chatID, "Задание отправлено!", USER_KEYBOARD_1)
			setStatus(uID, 1)
		elif userStatus(uID) == 3:
			if text == "Выполнил!":
				sendMessage(chatID, "Молодец, поздравляем!", USER_KEYBOARD_1)
				setStatus(uID, 1)
			elif text == "Не выполнил":
				sendMessage(chatID, "Не расстраивайся, в следующий раз получится", USER_KEYBOARD_1)
				setStatus(uID, 1)
			else:
				sendMessage(chatID, "Неверная команда")

	offset = answer["update_id"]+1
	time.sleep(1)
