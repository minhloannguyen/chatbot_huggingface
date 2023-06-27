import PySimpleGUI as sg

sg.theme("DarkBlue3")
sg.set_options(font=("Courier New", 16))

layout = [[sg.Text('WELCOME!')],
          [sg.Multiline(size=(50, 20), disabled=True, key='-OUTPUT-')],
          [sg.InputText(key='-INPUT-')],
          [sg.Button('Send'), sg.Button('Exit')]]

window = sg.Window('Chat App', layout, finalize=True)
window['-INPUT-'].bind("<Return>", "_Enter")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    window['-OUTPUT-'].print(values['-INPUT-'])
    window['-INPUT-'].update('')
