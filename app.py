from flask import Flask, jsonify, request
import re
import pwinput

app = Flask(__name__)

@app.route('/graphql', methods=['POST'])
def valida_senha(nome, senha):
     if nome == senha:
          return "Erro: a senha não deve ser igual ao nome."

     if len(senha)< 6:
          flag = -1
          return "A senha deve conter no mínimo 6 caracteres."

     elif not re.search("[a-z]", senha):
          flag = -1

     elif not re.search("[A-Z]", senha):
          flag = -1
          return "A senha deve conter no mínimo um caracter MAIÚSCULO."

     elif not re.search("[0-9]", senha):
          flag = -1
          return "A senha deve conter no mínimo um número."

     elif not re.search("[!@#$%^&*?]", senha):
          flag = -1
          return "A senha deve conter no mínimo um caracter especial."

     elif re.search("\s", senha):
          flag = -1

     else:
          flag = 0
          return "Login com sucesso."

     if flag == -1:
          return "Senha inválida. "
     return jsonify(app)

if __name__=='__main__':
     nome = input('Digite seu login: ')
     senha = pwinput.pwinput("Digite sua senha: ")
     validacao = valida_senha(nome,senha)
app.run(port=5000, host='localhost', debug=True)     
