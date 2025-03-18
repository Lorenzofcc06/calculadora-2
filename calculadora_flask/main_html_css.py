from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacao = request.form["operacao"]

        if operacao == "soma":
            resultado = num1 + num2
        
        elif operacao == "subtracao":
            resultado = num1 - num2

        elif operacao == "multiplicacao":
            resultado = num1 * num2

        elif operacao == "divisao":
            if num2 == 0:
                return render_template("index.html", resultado=">>> ERRO <<< Divisão por zero!")
            resultado = num1 / num2
        else:
            return render_template("index.html", resultado=">>> ERRO <<< Operação Inválida!")        
        return render_template("index.html", resultado=f"Resultado = {resultado}")
    
    except ValueError:
        return render_template("index.html", resultado=">>> ERRO <<< Digite valores númericos válidos!")
    
if __name__ == "__main__":
    app.run(debug=True)