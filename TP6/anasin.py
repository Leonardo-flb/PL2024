from lexer import lexer 
import ply.lex as lex



prox_Simb = ('Erro', '', 0, 0)

def parserError(s):
    print("ERRO SINTATICO: ",s)

def rec_term(s):
    global prox_Simb
    if prox_Simb.type == s:
        prox_Simb = lexer.token()
    else:
        parserError(s)

def rec_Language():
    global prox_Simb
    if prox_Simb.type == "INTERROGACAO":
        rec_term ("INTERROGACAO")
        rec_term("ID")
        print("RECONHECIDO P1 : ? cont")
    elif prox_Simb.type == "EXCLAMACAO":
        rec_term("EXCLAMACAO")
        rec_conteudo()
        print("RECONHECIDO P2 : ! cont")
    elif prox_Simb.type == "ID":
        rec_term("ID")
        rec_term("EQUALS")
        rec_conteudo()
        print("RECONHECIDO P3 : ID = cont")
    else:
        parserError(prox_Simb)

def rec_conteudo():
    global prox_Simb
    if prox_Simb.type == "ID":
        rec_term("ID")
        rec_resto()
        print("RECONHECIDO P4 : ID resto")
    elif prox_Simb.type == "NUM":
        rec_term("NUM")
        rec_resto()
        print("RECONHECIDO P5 : NUM resto")
    elif prox_Simb.type == "PA":
        rec_term("PA")
        rec_conteudo()
        rec_term("PF")
        print("RECONHECIDO P6 : ( conteudo )")
    else:
        parserError(prox_Simb)

def rec_resto():
    global prox_Simb
    if prox_Simb.type == "PLUS":
        rec_term("PLUS")
        rec_conteudo()
        print("RECONHECIDO P7 : + conteudo")
    elif prox_Simb.type == "MINUS":
        rec_term("MINUS")
        rec_conteudo()
        print("RECONHECIDO P8 : - conteudo")
    elif prox_Simb.type == "TIMES":
        rec_term("TIMES")
        rec_conteudo()
        print("RECONHECIDO P9 : * conteudo")
    elif prox_Simb.type == "DIVIDE":
        rec_term("DIVIDE")
        rec_conteudo()
        print("RECONHECIDO P10 : / conteudo")
    elif prox_Simb.type == "PF" or prox_Simb.type =="eof":
        print("RECONHECIDO P11 : eof")

    else:
        parserError(prox_Simb)

def rec_Parser(data):
    global prox_Simb
    lexer.input(data)
    prox_Simb = lexer.token()
    rec_Language()
    print("CABOU :///")


t1 = "? a"
t2 = "! a * b"
t3 = "b = a * 2 / (27 - 3)"
t4 = "c = a * b"

rec_Parser(t1)
rec_Parser(t2)
rec_Parser(t3)
rec_Parser(t4)