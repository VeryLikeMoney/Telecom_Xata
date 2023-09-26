import PySimpleGUI as sg
import applying_code
sg.theme('LightBlue')
n,m=35,1 # Размер Text
layout = [
    [sg.Column(layout='',size=(200,1)),sg.Text('Приветсвие',size=(n,m))],
    [sg.Text('Ввод частоты (1÷3000 в МГц)',size=(n,m)),sg.InputText(k='f',size=(n,m))],
    [sg.Text('Ввод растояния (1÷30 в километрах)',size=(n,m)),sg.InputText(k='d',size=(n,m))],
    [sg.Text('Высота антенны приемника (30÷300 в метрах)',size=(n,m)),sg.InputText(k='h_b',size=(n,m))],
    [sg.Text('Высота антенны передатчика (1,5÷3 в метрах)',size=(n,m)),sg.InputText(k='h_m',size=(n,m))],
    [sg.Button('Расчет'),sg.VSeparator(),sg.Text('________',k='-Result-')]   
]
window = sg.Window('Программа для расчета потерь на трассе', layout)
while True:                             # The Event Loop
    event, values = window.read() 
    if event=='Расчет':
        l=applying_code.out_L(values)
        print(l)
        window['-Result-'].update(l)
    if event in (None, 'Exit', 'Cancel'):
        break