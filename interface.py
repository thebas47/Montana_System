# Destinado a mensagens e interfaces
class CliInterfaces:

    def logo():
        print(r"""Montana System ™
=         =             
= =     = =  = = =  =    =  = = =   =    =    =    =
=  =   =  =  =   =  = =  =    =    = =   = =  =   = =
=   = =   =  = = =  =  = =    =   =   =  =  = =  =   =
        """)

    def salute(user):
        print(f"\nSeja bem vindo ao Montana System ™ {user}!")

    def catalogue():
        print(r"""
Qual rotina pretende acessar?
1 - Conciliação Bancária
2 - Classificação de Notas
3 - Leitor de Planilhas
4 - Leitor de PDFs              
exit - Para Sair do Programa
        """)
