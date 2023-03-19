from random import sample
import sqlite3
import os

connector = sqlite3.connect("Database.db")

cursor = connector.cursor()

try:
    cursor.execute("CREATE TABLE messages_and_replies(message, replied);")
    cursor.execute("INSERT INTO messages_and_replies(message, replied) VALUES('Hello', 'Hello, How are you?'), ('Hello', 'Hello'), ('Hello', 'Hello'), ('Hello', 'Hi'), ('Hello', 'Hi');")
    connector.commit()
except sqlite3.OperationalError:
    pass

data = cursor.execute("SELECT * FROM messages_and_replies;")

if not data.fetchall():
    print("Data is empty.")
    os.system("pause")
    exit(1)

SENSITIVITY = 40

LIMITATION = 5

messages_and_replies = {}

for item in data.fetchall():
    if item[0] in messages_and_replies:
        messages_and_replies[item[0]].append(item[1])
    else:
        messages_and_replies[item[0]] = [item[1]]


def random_reply(message: str, messages_and_replies) -> str:
    result = []
    if message in messages_and_replies:
        if len(messages_and_replies[message]) >= LIMITATION:
            for reply in set(messages_and_replies[message]):
                if (round((messages_and_replies[message].count(reply)/len(messages_and_replies[message]))*100)) >= SENSITIVITY:
                    result.append(reply)
            return sample(result, 1)[0]


if __name__ == "__main__":
    try:
        while True:
            message = input(">> ")
            if message in messages_and_replies:
                reply = random_reply("Hello", messages_and_replies)
                print(reply)
    except KeyboardInterrupt:
        print("Process Stopped.")

