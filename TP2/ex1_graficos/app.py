# app.py

from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
from ex1_map import armazenar_passos, Algoritmos

app = Flask(__name__)

def gerar_grafico(dados, titulo):
    plt.figure(figsize=(10, 5))
    plt.plot(list(dados.keys()), list(dados.values()), marker='o')
    plt.title(titulo)
    plt.xlabel('Entrada')
    plt.ylabel('Quantidade de Passos')
    plt.grid(True)

    # Salva o gráfico em um objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    # Codifica o gráfico em base64
    graphic = base64.b64encode(image_png).decode('utf-8')
    return graphic

@app.route('/')
def home():
    # Gera os dados para cada função
    passos_funcao1 = armazenar_passos(Algoritmos.funcao1)
    passos_funcao2 = armazenar_passos(Algoritmos.funcao2)
    passos_funcao3 = armazenar_passos(Algoritmos.funcao3)

    # Gera os gráficos para cada conjunto de dados
    grafico1 = gerar_grafico(passos_funcao1, 'Passos para funcao1 (O(n))')
    grafico2 = gerar_grafico(passos_funcao2, 'Passos para funcao2 (O(n^2))')
    grafico3 = gerar_grafico(passos_funcao3, 'Passos para funcao3 (O(2^n))')

    # Renderiza a página HTML com os gráficos
    return render_template('index.html', grafico1=grafico1, grafico2=grafico2, grafico3=grafico3)

if __name__ == '__main__':
    app.run(debug=True)
