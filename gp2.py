import PySimpleGUI as sg

sg.theme("Dark Amber")


# PROGRESSO DE CADASTRO
def ProgressoC():
    layoutProgresso = [[sg.Text('Criando sua conta...')],
                       [sg.ProgressBar(250, orientation='h', size=(20, 20), key='progresso')],
                       [sg.Cancel()]]
    windowProgresso = sg.Window('JPK™', layoutProgresso)
    for i in range(250):
        event, values = windowProgresso.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            menu()
        windowProgresso['progresso'].update_bar(i + 1)
    windowProgresso.close()


# PROGRESSO DE LOGIN
def ProgressoL():
    layoutProgresso = [[sg.Text('Entrando na sua conta...')],
                       [sg.ProgressBar(250, orientation='h', size=(20, 20), key='progresso')],
                       [sg.Cancel()]]
    windowProgresso = sg.Window('JPK™', layoutProgresso)
    for i in range(250):
        event, values = windowProgresso.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            menu()
        windowProgresso['progresso'].update_bar(i + 1)
    windowProgresso.close()


# PROGRESSO DE CRIANDO O PRODUTO
def ProgressoP():
    layoutProgresso = [[sg.Text('Criando produto')],
                       [sg.ProgressBar(250, orientation='h', size=(20, 20), key='progresso')],
                       [sg.Cancel()]]
    windowProgresso = sg.Window('JPK™', layoutProgresso)
    for i in range(250):
        event, values = windowProgresso.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            menu()
        windowProgresso['progresso'].update_bar(i + 1)
    windowProgresso.close()


# PROGRESSO DE PESQUISANDO PRODUTO
def ProgressoPESQUISA():
    layoutProgresso = [[sg.Text('Pesquisando...')],
                       [sg.ProgressBar(250, orientation='h', size=(20, 20), key='progresso')],
                       [sg.Cancel()]]
    windowProgresso = sg.Window('JPK™', layoutProgresso)
    for i in range(250):
        event, values = windowProgresso.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            menu()
        windowProgresso['progresso'].update_bar(i + 1)
    windowProgresso.close()


# PROGRESSO DE ALTERAR PRODUTOS
def ProgressoAlterar():
    layoutProgresso = [[sg.Text('Alterando produto')],
                       [sg.ProgressBar(250, orientation='h', size=(20, 20), key='progresso')],
                       [sg.Cancel()]]
    windowProgresso = sg.Window('JPK™', layoutProgresso)
    for i in range(250):
        event, values = windowProgresso.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            menu()
        windowProgresso['progresso'].update_bar(i + 1)
    windowProgresso.close()


# MENU INICIAL
def menu():
    layoutInicio = [
        [sg.Text("SELECIONE UMA OPÇÃO: ")],
        [sg.Button("Sou Empresa"), sg.Button("Sou Cliente")],
        [sg.Text("\n\n")],
        [sg.Button("FECHAR")],
        [sg.Text("\nDesenvolvido por JPK Serviços™")]
    ]
    janelaInicio = sg.Window("JPK MARKETPLACE", layoutInicio, size=(300, 200))
    while True:
        evento, valores = janelaInicio.Read()
        janelaInicio.close()
        if evento == "FECHAR" or evento == sg.WIN_CLOSED:
            break
        if evento == "Sou Empresa":
            Empresa1()
        if evento == "Sou Cliente":
            Cliente1()


# MENU DE SELEÇÃO DA EMPRESA (QUERO ME CADASTRAR) / (JÁ SOU CADASTRADO)
def Empresa1():
    # CRIANDO O LAYOUT DA SELEÇÃO
    layoutEmpresa1 = [
        [sg.Text("SELECIONE UMA OPÇÃO: ")],
        [sg.Button("Quero me cadastrar"), sg.Button("Já sou cadastrado")],
        [sg.Text('\n\n')],
        [sg.Button("VOLTAR")],
        [sg.Text("\nDesenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa1 = sg.Window("JPK MARKETPLACE", layoutEmpresa1, size=(300, 200))
    while True:
        evento, valores = janelaEmpresa1.Read()
        janelaEmpresa1.close()
        if evento == "Fechar" or evento == sg.WIN_CLOSED:
            break
        if evento == "Quero me cadastrar":
            Empresa2()
        if evento == "Já sou cadastrado":
            Empresa3()
        if evento == "VOLTAR":
            menu()


# MENU PARA CADASTRAR EMPRESA
def Empresa2():
    layoutEmpresa2 = [
        [sg.Text("Digite seu login: ")],
        [sg.InputText(key="loginEmpresa")],
        [sg.Text("Digite sua senha: ")],
        [sg.InputText(key="senhaEmpresa", password_char="*")],
        [sg.Text("Digite seu CNPJ (somente números): ")],
        [sg.InputText(key="CNPJ")],
        [sg.Text("Digite o nome da empresa: ")],
        [sg.InputText(key="nomeEmpresa")],
        [sg.Text("Digite o número de contato: ")],
        [sg.InputText(key="numEmpresa")],
        [sg.Text("Endereço: ")],
        [sg.InputText(key="endEmpresa")],
        [sg.Text("CEP:")],
        [sg.InputText(key="cepEmpresa")],
        [sg.Text("")],
        [sg.Button("CONCLUIR CADASTRO"), sg.Button("CANCELAR")],
        [sg.Text("\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa2 = sg.Window("JPK MARKETPLACE", layoutEmpresa2, size=(400, 520))
    checkEmpresa = False
    while True:
        arquivo2 = open("empresas.txt", "a", encoding="utf-8")
        evento, valores = janelaEmpresa2.Read()
        janelaEmpresa2.close()
        if evento == "FECHAR" or evento == sg.WIN_CLOSED:
            break
        if evento == "CANCELAR":
            menu()
        if evento == "CONCLUIR CADASTRO":
            if evento == sg.WIN_CLOSED or evento == "CANCELAR" or evento == "Fechar":
                break
            ProgressoC()
            arquivo = open("empresas.txt", "r", encoding="utf-8")
            checkEmpresa2 = False
            for linha in arquivo.readlines():
                arq = linha.split("-")
                valores['loginEmpresa3'] = arq[0].strip()
                if valores['loginEmpresa'] == valores['loginEmpresa3']:
                    checkEmpresa = True
                    break
                valores['CNPJ2'] = arq[2].strip()
                if valores['CNPJ'] == valores['CNPJ2']:
                    checkEmpresa2 = True
                    break
                arquivo.close()
            if checkEmpresa2:
                sg.popup("O CNPJ inserido já existe")
                Empresa1()
            if checkEmpresa:
                sg.popup("O login inserido já existe")
                Empresa1()
            if not checkEmpresa and not checkEmpresa2:
                arquivo2.write(
                    f" {valores['loginEmpresa']} - {valores['senhaEmpresa']} - {valores['CNPJ']} - {valores['nomeEmpresa']} - {valores['numEmpresa']} - {valores['endEmpresa']} - {valores['cepEmpresa']}\n")
                arquivo2.close()
                sg.popup("Sua conta foi criada com sucesso")
                Empresa1()
            janelaEmpresa2.close()

# MENU DE LOGIN DA EMPRESA
def Empresa3():
    layoutEmpresa3 = [
        [sg.Text("Digite seu login: ")],
        [sg.InputText(key="loginEmpresa")],
        [sg.Text("Digite sua senha: ")],
        [sg.InputText(key="senhaEmpresa", password_char="*")],
        [sg.Button('ENTRAR'), sg.Button("CANCELAR")],
        [sg.Text("\n\n\n\n\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa3 = sg.Window("JPK MARKETPLACE", layoutEmpresa3, size=(300, 300))
    while True:
        evento, valores = janelaEmpresa3.Read()
        janelaEmpresa3.close()
        if evento == sg.WIN_CLOSED:
            break
        if evento == "CANCELAR":
            menu()
        if evento == "ENTRAR":
            ProgressoL()
            arquivo = open("empresas.txt", "r")
            for linha in arquivo.readlines():
                arq = linha.split("-")
                if not "loginEmpresa" in arq:
                    sg.popup("Bem vindo!")
                    Empresa4()
                    break
            else:
                sg.popup("Login ou senha invalidos!")
                Empresa3()
            arquivo.close()
            if evento == sg.WIN_CLOSED:
                break
            if evento == "CANCELAR":
                menu()

# MENU DE OPÇÕES PARA A EMPRESA
def Empresa4():
    layoutEmpresa4 = [
        [sg.Text("SELECIONE UMA OPÇÃO: ")],
        [sg.Button("Cadastrar Produtos"), sg.Button("Alterar produtos/preços")],
        [sg.Button("Consultar lista de produtos"), sg.Button("Pesquisar Produto")],
        [sg.Text("\n")],
        [sg.Button("ENCERRAR PROGRAMA"), sg.Button("RETORNAR AO MENU")],
        [sg.Text("\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa4 = sg.Window("JPK MARKETPLACE", layoutEmpresa4, size=(400, 250))
    while True:
        evento, valores = janelaEmpresa4.Read()
        janelaEmpresa4.close()
        if evento == "ENCERRAR PROGRAMA" or evento == sg.WIN_CLOSED:
            break
        if evento == "Cadastrar Produtos":
            Empresa5()
        if evento == "Consultar lista de produtos":
            Empresa6()
        if evento == "Alterar produtos/preços":
            Empresa7()
        if evento == "Pesquisar Produto":
            Empresa8()
        if evento == "RETORNAR AO MENU":
            menu()

# OPÇÃO DE CADASTRAR PRODUTO
def Empresa5():
    layoutEmpresa5 = [
        [sg.Text("Código do produto: "), sg.InputText(key="codProd")],
        [sg.Text("Vendido por: "), sg.InputText(key="empresaVende")],
        [sg.Text("Nome do produto: "), sg.InputText(key="nomeProd")],
        [sg.Text("Valor R$: (00,00)"), sg.InputText(key="valorProd")],
        [sg.Text("Categoria: "), sg.InputText(key="catProd")],
        [sg.Button("CADASTRAR"), sg.Button("CANCELAR")],
        [sg.Text("\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa5 = sg.Window("JPK MARKETPLACE", layoutEmpresa5, size=(400, 250))
    while True:
        arquivo = open("produtos.txt", "a", encoding="utf-8")
        evento, valores = janelaEmpresa5.Read()
        janelaEmpresa5.close()
        check2 = False
        arq = open('produtos.txt', 'r', encoding="utf-8")
        if evento == "CADASTRAR":
            ProgressoP()
            for linha in arq.readlines():
                arq2 = linha.split('-')
                if valores['codProd'] == arq2[0].strip():
                    check2 = True
            if check2:
                sg.popup('Esse codigo ja foi cadastrado')
                Empresa5()
            if not check2:
                arquivo.write(
                    f" {valores['codProd']} - {valores['empresaVende']} - {valores['nomeProd']} - {valores['valorProd']} - {valores['catProd']}\n")
                arquivo.close()
                sg.Listbox(values=('empresaVende'))
                sg.popup("Produto cadastrado com sucesso!")
                Empresa5()

        if evento == "CANCELAR":
            menu()
        if evento == sg.WIN_CLOSED:
            break

        # LISTANDO TODOS OS PRODUTOS


def Empresa6():
    arq = open('produtos.txt', 'r', encoding="utf-8")
    arq2 = arq.read()
    arq.close()
    layoutEmpresa6 = [
        [sg.Text("Código-Empresa-Produto-Preço-Categoria")],
        [sg.Text(arq2)],
        [sg.Button('CANCELAR')]
    ]
    janelaEmpresa6 = sg.Window("JPK MARKETPLACE", layoutEmpresa6, size=(500, 700))
    while True:
        evento, valores = janelaEmpresa6.Read()
        janelaEmpresa6.close()
        if evento == "CANCELAR":
            menu()
        if evento == sg.WIN_CLOSED:
            break


# OPÇÃO DE PESQUISAR O PRODUTO
def Empresa8():
    layoutEmpresa8 = [
        [sg.Text("Nome do produto para pesquisa: "), sg.InputText(key="nomeProdpesq")],
        [sg.Button("PESQUISAR"), sg.Button("FECHAR")],
        [sg.Text("Desenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa8 = sg.Window("JPK MARKETPLACE", layoutEmpresa8, size=(400, 100))
    while True:
        evento, valores = janelaEmpresa8.Read()
        janelaEmpresa8.Close()
        arq = open('produtos.txt', 'r', encoding="utf-8")
        check21 = False
        if evento == "PESQUISAR":
            ProgressoPESQUISA()
            for linha in arq.readlines():
                arq2 = linha.split('-')
                if valores["nomeProdpesq"] in linha:
                    check21 = True
                    arq3= arq2
            if check21:
                sg.popup(f'Loja:{arq3[1].strip()}\nProduto:{arq3[2].strip()}\nPreço:R${arq3[3].strip()}')
                Empresa8()
            if not check21:
                sg.popup('Item da pesquisa não encontrado')
                Empresa8()
        if evento == "FECHAR":
            menu()
        if evento == sg.WIN_CLOSED:
            break

# ALTERAR PROD/PREÇO
def Empresa7():
    layoutEmpresa7 = [
        [sg.Text("O que deseja alterar:")],
        [sg.Button("PREÇO"), sg.Button("NOME")],
        [sg.Text("\n")],
        [sg.Button("FECHAR")],
        [sg.Text("\n\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa7 = sg.Window("JPK MARKETPLACE", layoutEmpresa7, size=(300, 200))

    while True:
        evento, valores = janelaEmpresa7.Read()
        janelaEmpresa7.close()

        if evento == "FECHAR":
            Empresa4()
        if evento == sg.WIN_CLOSED:
            break
        if evento == "PREÇO":
            Empresa9()
        if evento == "NOME":
            Empresa10()

# ALTERAR PREÇO
def Empresa9():
    layoutEmpresa9 = [
        [sg.Text("Alterar preço do produto:")],
        [sg.Text("Codigo do produto: "), sg.InputText(key="codProd")],
        [sg.Text("Novo preço: R$"), sg.InputText(key="novoPreço")],
        [sg.Button("ALTERAR"), sg.Button("FECHAR")],
        [sg.Text("\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa9 = sg.Window("JPK MARKETPLACE", layoutEmpresa9, size=(300, 200))
    while True:
        evento, valores = janelaEmpresa9.read()
        janelaEmpresa9.Close()
        if evento == "FECHAR":
            menu()
        if evento == sg.WIN_CLOSED:
            break
        if evento == "ALTERAR":
            produtos = open("produtos.txt", "r", encoding="utf-8")
            substituto = ''
            ProgressoAlterar()
            for produto in produtos:
                codigo = produto.split('-')[0].strip()
                if codigo == valores["codProd"]:
                    substituto = substituto + produto.replace(produto.split('-')[3].strip(), valores["novoPreço"])
                else:
                    substituto = substituto + produto
            produtos = open("produtos.txt", "w", encoding="utf-8")
            produtos.write(substituto)
            produtos.close()
            sg.popup("Preço alterado com sucesso")
            Empresa7()

# ALTERAR NOME
def Empresa10():
    # layout08
    layoutEmpresa10 = [
        [sg.Text("Alterar nome do produto:")],
        [sg.Text("Codigo do produto: "), sg.InputText(key="codProd")],
        [sg.Text("Novo nome: "), sg.InputText(key="novoNome")],
        [sg.Button("ALTERAR"), sg.Button("FECHAR")],
        [sg.Text("\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaEmpresa10 = sg.Window("JPK MARKETPLACE", layoutEmpresa10, size=(300, 200))
    while True:
        evento, valores = janelaEmpresa10.read()
        janelaEmpresa10.Close()
        if evento == "FECHAR":
            Empresa7()
        if evento == sg.WIN_CLOSED:
            break
        if evento == "ALTERAR":
            produtos = open("produtos.txt", "r", encoding="utf-8")
            substituto = ''
            ProgressoAlterar()
            for produto in produtos:
                codigo = produto.split('-')[0].strip()
                if codigo == valores["codProd"]:
                    substituto = substituto + produto.replace(produto.split('-')[2].strip(), valores["novoNome"])
                else:
                    substituto = substituto + produto
            produtos = open("produtos.txt", "w", encoding="utf-8")
            produtos.write(substituto)
            produtos.close()
            sg.popup("Preço alterado com sucesso")
            Empresa7()
            []

# MENU DE SELEÇÃO DO CLIENTE
def Cliente1():
    layoutCliente1 = [
        [sg.Text("SELECIONE UMA OPÇÃO: ")],
        [sg.Button("Quero me cadastrar"), sg.Button("Já sou cadastrado")],
        [sg.Text('\n\n')],
        [sg.Button("VOLTAR")],
        [sg.Text("\nDesenvolvido por JPK Serviços™")]
    ]
    janelaCliente1 = sg.Window("JPK MARKETPLACE", layoutCliente1, size=(300, 200))
    while True:
        evento, valores = janelaCliente1.Read()
        janelaCliente1.close()
        if evento == "FECHAR" or evento == sg.WIN_CLOSED:
            break
        if evento == "Quero me cadastrar":
            Cliente2()
        if evento == "Já sou cadastrado":
            Cliente3()
        if evento == "VOLTAR":
            menu()

# MENU DE CADASTRO DO CLIENTE
def Cliente2():
    layoutCliente2 = [
        [sg.Text("Digite seu login: ")],
        [sg.InputText(key="loginCliente")],
        [sg.Text("Digite sua senha: ")],
        [sg.InputText(key="senhaCliente", password_char="*")],
        [sg.Text("Digite o seu nome: ")],
        [sg.InputText(key="nomeCliente")],
        [sg.Text("Digite seu Email: ")],
        [sg.InputText(key="email")],
        [sg.Text("Digite o número de contato: ")],
        [sg.InputText(key="numCliente")],
        [sg.Text("Endereço: ")],
        [sg.InputText(key="endCliente")],
        [sg.Text("CEP:")],
        [sg.InputText(key="cepCliente")],
        [sg.Text("")],
        [sg.Button("CONCLUIR CADASTRO"), sg.Button("CANCELAR")],
        [sg.Text("\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaCliente2 = sg.Window("JPK MARKETPLACE", layoutCliente2, size=(400, 520))
    checkCliente = False
    while True:
        arquivo2 = open("clientes.txt", "a", encoding="utf-8")
        evento, valores = janelaCliente2.Read()
        janelaCliente2.close()
        if evento == "FECHAR" or evento == sg.WIN_CLOSED:
            break
        if evento == "CANCELAR":
            menu()
        if evento == "CONCLUIR CADASTRO":
            if evento == sg.WIN_CLOSED or evento == "FECHAR":
                break
            ProgressoC()
            arquivo = open("clientes.txt", "r", encoding="utf-8")
            for linha in arquivo.readlines():
                arq = linha.split("-")
                valores['loginCliente3'] = arq[0].strip()
                if valores['loginCliente'] == valores['loginCliente3']:
                    checkCliente = True
                    break
            arquivo.close()
            if checkCliente:
                sg.popup("O login inserido já existe")
            if not checkCliente:
                arquivo2.write(
                    f" {valores['loginCliente']} - {valores['senhaCliente']} - {valores['nomeCliente']} - {valores['email']} - {valores['numCliente']} - {valores['endCliente']} - {valores['cepCliente']}\n")
                arquivo2.close()
                sg.popup("Sua conta foi criada com sucesso")
            janelaCliente2.close()
            Cliente1()

    arquivo2.close()

# MENU DE LOGIN DO CLIENTE
def Cliente3():
    layoutCliente3 = [
        [sg.Text("Digite seu login: ")],
        [sg.InputText(key="loginCliente2")],
        [sg.Text("Digite sua senha: ")],
        [sg.InputText(key="senhaCliente2", password_char="*")],
        [sg.Button('ENTRAR'), sg.Button("CANCELAR")],
        [sg.Text("\n\n\n\n\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaCliente3 = sg.Window("JPK MARKETPLACE", layoutCliente3, size=(300, 300))
    while True:
        evento, valores = janelaCliente3.Read()
        janelaCliente3.close()
        if evento == sg.WIN_CLOSED:
            break
        if evento == "CANCELAR":
            menu()
        if evento == "ENTRAR":
            ProgressoL()
            arquivo = open('clientes.txt', 'r', encoding="utf-8")
            for linha in arquivo.readlines():
                arq = linha.split("-")
                if valores['loginCliente2'] == arq[0].strip() and valores['senhaCliente2'] == arq[1].strip():
                    sg.popup("Bem Vindo!")
                    if evento == "ENTRAR":
                        Cliente4()
                        break
                else:
                    sg.popup("Login ou senha invalidos!")
                    Cliente3()
                    break
            arquivo.close()


# MENU DE OPERAÇÕES DO CLIENTE
def Cliente4():
    layoutCliente4 = [
        [sg.Text("SELECIONE UMA OPÇÃO: ")],
        [sg.Button("Consultar lista de empresas"), sg.Button("Consultar empresa")],
        [sg.Button("Consultar lista de produtos"), sg.Button("Pesquisar produto")],
        [sg.Text("")],
        [sg.Button("ENCERRAR PROGRAMA"), sg.Button("RETORNAR AO MENU")],
        [sg.Text("\n\n\nDesenvolvido por JPK Serviços™")]
    ]
    janelaCliente4 = sg.Window("JPK MARKETPLACE", layoutCliente4, size=(400, 250))

    while True:
        evento, valores = janelaCliente4.Read()
        janelaCliente4.close()
        if evento == "Encerrar programa" or evento == sg.WIN_CLOSED:
            break
        if evento == "RETORNAR AO MENU":
            menu()
        if evento == "Pesquisar produto":
            Cliente5()
        if evento == "Consultar lista de produtos":
            Cliente6()
        if evento == "Consultar lista de empresas":
            Cliente7()
        if evento == "Consultar empresa":
            Cliente8()


# FUNÇÃO DE PESQUISA CLIENTE
def Cliente5():
    layoutCliente5 = [
        [sg.Text("Nome do produto para pesquisa: "), sg.InputText(key="nomeProdpesq")],
        [sg.Button("PESQUISAR"), sg.Button("FECHAR")],
        [sg.Text("Desenvolvido por JPK Serviços™")]
    ]
    janelaCliente5 = sg.Window("JPK MARKETPLACE", layoutCliente5, size=(400, 100))
    while True:
        evento, valores = janelaCliente5.Read()
        janelaCliente5.Close()
        arq = open('produtos.txt', 'r', encoding="utf-8")
        produtos = arq.readlines()
        check = False
        if evento == "PESQUISAR":
            ProgressoPESQUISA()
            for linha in produtos:
                arq2 = linha.split('-')
                if valores["nomeProdpesq"] in linha:
                    check = True
                    arq3= arq2
            if check:
                sg.popup(f'Loja:{arq3[1].strip()}\nProduto:{arq3[2].strip()}\nPreço:R${arq3[3].strip()}')
                Cliente5()
            else:
                sg.popup('Produto não encontrado')
                Cliente5()
        if evento == "FECHAR":
            menu()
        if evento == sg.WIN_CLOSED:
            break


# LISTANDO TODOS OS PRODUTOS DE CLIENTE
def Cliente6():
    arq = open('produtos.txt', 'r', encoding="utf-8")
    arq2 = arq.read()
    arq.close()
    layoutCliente6 = [
        [sg.Text("Código-Empresa-Produto-Preço-Categoria")],
        [sg.Text(arq2)],
        [sg.Button('CANCELAR')]
    ]

    janelaCliente6 = sg.Window("JPK MARKETPLACE", layoutCliente6, size=(800, 700))
    while True:
        evento, values = janelaCliente6.Read()
        janelaCliente6.close()
        if evento == "CANCELAR":
            menu()
        if evento == sg.WIN_CLOSED:
            break


# LISTA DE EMPRESAS
def Cliente7():
    arq = open('empresas.txt', 'r', encoding="utf-8")
    lista = []
    for i in arq:
        queb = i.split('-')
        lista.append(queb[3])

    layoutCliente7 = [
        [sg.Text("Empresas")],
        [sg.Text(lista)],
        [sg.Button('FECHAR')]
    ]
    janelaCliente7 = sg.Window("JPK MARKETPLACE", layoutCliente7, size=(1300, 500))
    while True:
        evento, values = janelaCliente7.Read()
        janelaCliente7.close()
        if evento == "FECHAR":
            menu()
        if evento == sg.WIN_CLOSED:
            break


# LISTA AS INFORMAÇÕES DAS EMPRESAS
def Cliente8():
    arq = open('empresas.txt', 'r', encoding="utf-8")
    arq2 = arq.read()
    layoutCliente8 = [
        [sg.Text("login - senha - Cnpj - empresa - telefone - endereço - CEP:")],
        [sg.Text(arq2)],
        [sg.Button('FECHAR')]
    ]

    janelaCliente8 = sg.Window("JPK MARKETPLACE", layoutCliente8, size=(1300, 500))
    while True:
        evento, values = janelaCliente8.Read()
        janelaCliente8.close()
        if evento == "FECHAR":
            menu()
        if evento == sg.WIN_CLOSED:
            break


menu()