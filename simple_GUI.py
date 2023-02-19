import PySimpleGUI as sg
sg.theme('DarkAmber')

layout = [  [sg.Text('Nome')], 
            [sg.Text('Idade')],
            [sg.Button('Enviar'), sg.Button('Cancelar')]
]

# Criar uma Janela