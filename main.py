import PySimpleGUI as sg
import logging

from transformer.bot import ChatBot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sg.theme("GreenTan")
sg.set_options(font=("Courier New", 16))

layout = [[sg.Text('WELCOME!')],
          [sg.Multiline(size=(50, 20), disabled=True, key='-OUTPUT-')],
          [sg.InputText(key='-INPUT-')],
          [sg.Button('Send', bind_return_key=True), sg.Button('Exit')]]

window = sg.Window('Chat App', layout, finalize=True)
bot = ChatBot()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    input = values['-INPUT-']
    window['-OUTPUT-'].print("Me: " + input)
    
    if input:
        res = bot.run(input)
        window['-OUTPUT-'].print("Sushi(bot): " + res["answer"].lstrip(), text_color='blue')

    window['-INPUT-'].update('')

window.close()