"""
Operadores lógicos
and or not

and - Todas as condições devem ser verdadeira
      se qualquer valor falso o resultado é falso
São considerados falsy
0 0.0 '' False

tbm existe o tipo None que é usado para representar um não valor

"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '0000'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'E' and senha_digitada != senha_permitida:
    print('Senha incorreta')
else:
    print('Sair')