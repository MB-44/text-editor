import PySimpleGUI as ps 
from pathlib import Path

menuLayout = [
                ['File',['Open','Save','option','---','quit']],
                ['Tools',['Word count']]
             ]

layout = [
            [ps.Menu(menuLayout)],
            [ps.Text('Untitled',key='-docName-')],
            [ps.Multiline(
                no_scrollbar=True,
                size=(80,30),
                key = "-textBox-"
                )]
         ]

window = ps.Window("NotePad by mena",layout)

while True:
    ps.theme("TanBlue") 
    event,values = window.read()
    
    if event == ps.WIN_CLOSED:
        break

    if event == "Open":
        filePath = ps.popup_get_file('open',no_window=False)
        if filePath:
            file = Path(filePath)
            window['-textBox-'].update(file.read_text())
            window['-docName-'].update(filePath.split('/')[-1])

    if event == "Save":
        filePath = ps.popup_get_file("Save as",no_window=False,save_as=True)
        file = Path(filePath)
        file.write_text(values['-textBox-'])
        window['-docName-'].update(filePath.split('/')[-1])

    if event == "Word count":
        fullText = values['-textBox-']
        wordLen = len(fullText.replace('\n',' ').split(' '))
        ps.popup(f"{wordLen} number of words!")

window.close()