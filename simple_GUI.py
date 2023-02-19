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

# Evento de Loop para Processar "Eventos" e Obter os "Valores" da Entrada de Dados
while True:
    event, values = window.read()
    if events == sg.WIN_CLOSED or event == 'Cancel': # Se o Usuário Fechar a Janela ou clicar em CANCELAR
        break # A Janela Vai Quebrar ou Fechar
    print('Você se cadastrou com sucesso!', values[0])
window.close()