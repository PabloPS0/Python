import PySimpleGUI as sg

sg.theme('DarkAmber') # Cor do tema
 
# Criar Todo o Conteúdo que Terá Dentro da Janela
layout = [  [sg.Text('Nome')], 
            [sg.Text('Idade')],
            [sg.Text('Empregado'), sg.Button('Sim'), sg.Button('Não')]
            [sg.Button('Enviar'), sg.Button('Cancelar')]
]

# Criar uma Janela
window = sg.Window('Cadastro', layout)

# Evento de Loop para processar "eventos" e obter os "valores" da entrada de dados
