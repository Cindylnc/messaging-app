from flask import Flask, render_template, request
import requests
import os
import json
import os.path

text_belt_apikey = os.environ['TEXT_BELT_API_KEY']

app = Flask (__name__)

@app.get("/")
def home_page():
    return render_template("index.html")


conversation = {}
@app.post("/")
def confirmation():

    message = request.form.get("messages")
    csv_data = request.form.get("csv_data")

    keys = []
    data = []
    results = []

    print(csv_data)
    csv_data = csv_data.replace("\r", "")
    rows = csv_data.split("\n")
    print("Rows:")
    print(rows)
    first_row = 0
    for row in rows:
        values = row.split(",")
        first_row = first_row + 1
        if first_row ==1:
            keys = values
        else:
            dictiona = {}
            key_index = 0
            for key in keys:
                dictiona[key] = values [key_index]
                key_index = key_index + 1
            data.append(dictiona)
    print(data)
 


    for each_message in data:
            print (each_message)
            resp = requests.post("https://textbelt.com/text", {
                "phone": each_message["phone"],
                "message": message.format(**each_message),
                "key": text_belt_apikey,
                "replyWebhookUrl": "https://0ee1-204-113-19-48.ngrok-free.app/reply"
            })
            confirmation = resp.json()
            print (confirmation)

            textId = confirmation.get("textId")
            conversation[textId] = []
            conversation [textId].append({"from": "sender","text": message.format(**each_message)})

            with open ("conversation.json", "w") as file:
                json.dump(conversation, file, indent=4)

    return render_template("confirmation.html", results = results)


@app.post("/reply")
def reply():
    reply = (request.json)
    textId = reply.get("textId")
    conversation.get(textId).append({"from": reply.get("fromNumber"), "text": reply.get("text")})
    # with open ("conversation.json", "w") as file:
    #     json.dump(conversation, file)

app.run (debug=True, port=9000)




