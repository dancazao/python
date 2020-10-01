from checagem import processos as pr


def menu():
    entrada=input("1.Login\n2.Cadastrar\n")
    entrada=int(entrada)
    if entrada==1:
        s,c=pr.acesso()
        print(s)
        pos_menu(c)
    elif entrada == 2:
        pr.criar_conta()
        menu()
    else:
        menu()

def pos_menu(c):

        if c!=-1:
            entrada1=input("1.Saldo\n2.Saque\n3.Deposito\n4.sair\n")
            entrada1=int(entrada1)
            if entrada1==1:
                pr.dinheiro(c)
            elif entrada1==2:
                pr.saque(c)
            elif entrada1==3:
                pr.ad_dinheiro()
            elif entrada1==4:
                return 0
            else:
                menu()
            pos_menu(c)
        else:
            menu()



def main():
    menu()

main()
