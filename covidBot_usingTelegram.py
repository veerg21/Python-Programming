from telegram.ext import Updater, CommandHandler
import requests
Api_Key="5275091047:AAGFKOSZUEbHhvnIUHFZOPHPadF-5L1qZfQ"
updater=Updater(token=Api_Key)
dispatcher=updater.dispatcher
updater.start_polling()
greeting_ls=["hi", "hello", "wussup"]
def greeting(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, how are you doing?")

greeting_handler=CommandHandler(greeting_ls, greeting)
dispatcher.add_handler(greeting_handler)
# https://api.covid19api.com/summary
def summary(update, context):
    response=requests.get("https://api.covid19api.com/summary")
    if response.status_code==200:
        data=response.json()
        # print(data)
        date=data["Date"][:10]
        print(date)
        ans=f"Covid-19 summary as of {date} is: \n"
        for i, j in data["Global"].items():
            if i not in ["NewConfirmed", "NewDeaths", "NewRecovered", "Date"]:
                # print(i, ":", j)
                ans+=i+ ": "+ str(j)+"\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)

    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="There was an error")
summaryHandler=CommandHandler("summary", summary)
dispatcher.add_handler(summaryHandler)