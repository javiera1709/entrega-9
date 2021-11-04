import re
from flask import Flask, render_template, request
app = Flask(__name__)   



@app.route("/eleccion")
def elige():
    return render_template("intento desesperado.html")

@app.route("/proyecto")
def muestra_proyecto():
    return render_template("nuestro_proyecto.html")

@app.route('/')          
def hello_world():
    return render_template("nosotros.html")

@app.route("/Menú" , methods=['POST'])          
def menu():
    proteina = request.form ["proteina"]
    proteina2 = request.form ["proteina2"]
    proteina3 = request.form ["proteina3"]
    fruta = request.form ["fruta"]
    fruta2 = request.form ["fruta2"]
    fruta3 = request.form ["fruta3"]
    vegetales = request.form ["vegetales"]
    vegetales2 = request.form ["vegetales2"]
    vegetales3 = request.form ["vegetales3"]
    Legumbres = request.form ["Legumbres"]
    Legumbres2 = request.form ["Legumbres2"]
    Legumbres3 = request.form ["Legumbres3"]
    if proteina=="vacio" and  fruta=="vacio" and vegetales=="vacio" and Legumbres=="vacio":
        result = "esto funciona"

    return render_template("result.html", 
    proteina=proteina,
    proteina2=proteina2,
    proteina3=proteina3,
    fruta=fruta,
    fruta2=fruta2,
    fruta3=fruta3,
    vegetales=vegetales,
    vegetales2=vegetales2,
    vegetales3=vegetales3,
    Legumbres=Legumbres,
    Legumbres2=Legumbres2,
    Legumbres3=Legumbres3, 
    result=result)





if __name__=="__main__":   
    app.run(debug=True)    
