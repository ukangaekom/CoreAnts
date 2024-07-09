# AI related library
import openai
import os

# Bot related library
from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, CallbackContext

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def getCompletion(prompt, model='gpt-3.5-turbo'):
    messages = [{"role":"user", "content":prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message['content']



Finance = """
    Overview
    -Why you should learn how to use core chain
    -The future of core chain
    -Activities that happens in core chain
    
"""


prompt = 'Your task is to give a generative response for an imaginary blockchain called core. You are to anser, the user based on the provided info {Finance}'

response = getCompletion(prompt)

print(response)