import PySimpleGUI as sg
import webbrowser

sg.theme('DarkBlue1')
url = "https://en.wikipedia.org/wiki/Special:Random/"


layout = [
    [sg.Text('Random wikipedia page :)'), sg.Text(size= (20,1), key = '-TEXT-')],
    [sg.Button('Click here to open'), sg.Text(size=(15,1), key = "-OPEN-")]
    
    
]

window = sg.Window('Random wikipedia page', layout,)




while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Click here to open':
        webbrowser.open_new_tab(url)

    

window.close()