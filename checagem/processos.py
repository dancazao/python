from checagem import gerenciar as gr

usuarios = []

def criar_conta():
    login = input("Cadastre o Login: ")
    senha = input("Cadastre a Senha: ")
    usuario= gr.User(login,senha)
    usuarios.append(usuario)
    return login, senha


def acesso():

    login = input("Login: ")
    senha=input("Senha: ")
    cod=-1
    for log in usuarios:
        cod+=1
        if log.login==login:
            if log.senha==senha:
                return "Logado com sucesso",cod
            else:
                return "Senha invalida",-1
    return "Login invalido",-1


def dinheiro(cod):
    saldo=usuarios[cod]
    print(saldo.saldo)

def ad_dinheiro(cod):
    din=input("Valor: ")
    din=int(din)
    usuarios[cod].saldo+=din
    print(usuarios[cod].saldo)

def saque(cod):
    din=input("Valor: ")
    din=int(din)
    if din>usuarios[cod].saldo:
        print("saldo insuficiente")
    else:
        usuarios[cod].saldo-=din
    print(usuarios[cod].saldo)