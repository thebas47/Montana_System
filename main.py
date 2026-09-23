from interface import CliInterfaces as msg
from workers.sheet_work import SheetWorks
from workers.pdf_work import PdfWorks

import time

time.sleep(2)
msg.logo()

#time.sleep(2)
#user = input('\nQual seu nome?\n>>> ')

msg.salute("Usuário")
time.sleep(2)

while True:
    msg.catalogue()
    opt = input('>>> ')

    match opt:
        case '1':
            print('Você acessou a rotina de conciliação bancária.')
        case '2':
            print("Você acessou a rotina de classificação de notas fiscais")
        case '3':
            print('Voce esta acessando a rotina de planilhas')
            SheetWorks.load_sheet()
        case '4':
            print("Você está acessando a rotina de PDFs")
            PdfWorks.load_pdf()
        case 'exit':
            print('Obrigado por usar o Montana!')
            break
