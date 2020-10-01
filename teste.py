
from checagem import processos as pr
i=0
while True:

    pr.criar_conta()
    for log in pr.usuarios:
        print(log.login)

