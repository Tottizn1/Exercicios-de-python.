"""1 Pergunte o nome de usuário
2 Pergunte a senha
3 Verifique se os dados estão corretos
4 Se estiverem corretos → Login realizado com sucesso!
5 Se estiverem errados → Usuário ou senha incorretos!
"""

name = input ("What is your name?")
password = input ("What is your password?")

if name == "Ruan" and password == "0102":
    print ("Username and password correct. acess granted!")

else:   
     print("Username or password incorrect. Access denied.")