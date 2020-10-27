#calclex.py
#Daniel Carvalho e Yonathan Uchoa
from sly import Lexer
import sys

class CalcLexer(Lexer):
    # Lista dos tokens da linguagem
    tokens = {NUM, PLUS, MINUS, TIMES, EQUAL, LESS, AND, NOT, COLON, SCOLON, DOT,
    LPAREN, RPAREN, LBRACK, RBRACK, LBRACE, RBRACE, ID, KEYWORD}
    
    # Ignora espaço em branco
    ignore = ' \t'
    
    #Ignora comentario de linha
    ignore_linecomment = r'//.*'
    
    # Ignora comentario de bloco
    @_(r'\/\*(\*(?!\/)|[^*])*\*\/')
    def ignore_blockcomment(self, tok):
        self.lineno += tok.value.count('\n')
    
    # Conta as linhas do codigo analisado
    @_(r'\n+')
    def ignore_newline(self, tok):
        self.lineno += tok.value.count('\n')
    
    # Expressões regulares para tokens
    NUM     = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'\-'
    TIMES   = r'\*'
    EQUAL   = r'\='
    LESS    = r'\<'
    AND     = r'(&&)'
    NOT     = r'\!'
    COLON   = r'\,'
    SCOLON  = r'\;'
    DOT     = r'\.'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACK  = r'\['
    RBRACK  = r'\]'
    LBRACE  = r'\{'
    RBRACE  = r'\}'
    
    #Encontra um identificador e verifica se ele e uma palavra reservada
    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, tok):
        #lista de palavras reservadas
        keywords = ["if", "else", "while" ,"boolean", "true", "false", "int", "string", "main", "void", "return",
                    "class", "new", "this", "lenght", "public", "static", "system", "out", "println"]
        value = tok.value.lower() #ignora o case do id encontrado
        #verifica se o id encontrado esta na lista de palavras reservadas e caso sim muda o tipo do token para "KEYWORD"
        if value in (str.lower() for str in keywords): 
            tok.type = 'KEYWORD'
        return tok
        
    #Tratamento de erros (Modo panico)
    def error(self, tok):
        #Mensagem de erro
        print('Linha: %d - Caractere ilegal: "%s"\n' % (self.lineno, tok.value[0]))
        self.index += 1 #Pula o caractere ilegal

if __name__ == '__main__':
    caminho = sys.argv[1] #Le o nome do arquivo de entrada como argumento 
    arquivo = open(caminho, 'r') #Abre o arquivo informado
    data = arquivo.read() # Le o arquivo informado 
    lexer = CalcLexer() #Inicializa o analisador lexico
    print()
    for tok in lexer.tokenize(data): #laço que identifica os tokens no arquivo e imprime esses tokens e suas informações
        print('[ %d, %s, "%s" ]\n' % (tok.lineno, tok.type, tok.value))
    arquivo.close() #fecha o arquivo