from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "chave"

def formatar_numero(numero):
    return int(numero) if numero.is_integer() else numero

@app.route("/")
def index():
    historico = session.get("historico",[])
    return render_template("index.html", historico=historico) 

@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacao = request.form["operacao"]

        resultado = None
        simbolo = ""

        if operacao == "soma":
            resultado = num1 + num2
            simbolo = "+"
        
        elif operacao == "subtracao":
            resultado = num1 - num2
            simbolo = "-"

        elif operacao == "multiplicacao":
            resultado = num1 * num2
            simbolo = "×"

        elif operacao == "divisao":
            if num2 == 0:
                return render_template("index.html", resultado=">>> ERRO <<< Divisão por zero!", historico=session.get("historico",[]))
            resultado = num1 / num2
            simbolo = "÷"
        else:
            return render_template("index.html", resultado=">>> ERRO <<< Operação Inválida!",historico=session.get("historico",[])) 

        resultado_formatado = formatar_numero(resultado)       

        calculo = f"{formatar_numero(num1)} {simbolo} {formatar_numero(num2)} = {resultado_formatado}"

        historico = session.get("historico",[])
        historico.insert(0,calculo)
        session["historico"] = historico[:5]

        return render_template("index.html", resultado=f"Resultado = {resultado_formatado}", historico=historico)
    
    except ValueError:
        return render_template("index.html", resultado=">>> ERRO <<< Digite valores númericos válidos!", historico=session.get("historico",[]))
    
if __name__ == "__main__":
    app.run(debug=True)