from flask import Flask, render_template
import mysql.connector
import os
import json
from datetime import datetime

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    "host": "host",
    "user": "user",
    "password": "password",
    "database": "database"
}

# Rota para a página inicial
@app.route('/')
def projeto():
    # Conectar ao banco de dados
    conexao = mysql.connector.connect(**db_config)

    # Criar um objeto cursor para interagir com o banco de dados
    cursor = conexao.cursor()

    # Exemplo de consulta SELECT
    consulta = "SELECT * FROM Dados"
    cursor.execute(consulta)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()
    vl_ = []
    temp = []
    for i in resultados:
        vl_.append(i[1])
        temp.append(i[2])

    vl_ph = json.dumps(vl_)
    vl_temp = json.dumps(temp)
    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    conexao.close()

    # Renderizar a página HTML com os resultados
    return render_template('index.html', resultados=resultados, vl_ph = vl_ph, vl_temp = vl_temp)

@app.route('/grupo/')
def grupo():
    return render_template('grupo.html')

# Garantir que o aplicativo só será executado se este script for o principal
if __name__ == "__main__":
    # Obter a porta do ambiente do Heroku ou usar 5000 como padrão
    port = int(os.environ.get("PORT", 5000))
    
    # Executar o aplicativo na porta especificada
    app.run(host="0.0.0.0", port=port)
