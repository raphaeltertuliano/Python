#Crie um código em Python que teste se o site Pudim está acessível pelo
#computador usado.
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.request.URLError:
    print('\033[31mO site não está acessível no momento\033[m')
else:
    print('\033[32mConsegui abrir o site com sucesso\033[m')

