# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby
from flask import Flask, render_template, request

# , redirect, url_for

app = Flask(__name__)

@app.route("/")
def vitej():
    return render_template("vitej.html")

@app.route("/form")
def form():
    recenze = request.args.get("recenze")
    if recenze == "nic":
        return render_template("form.html", jinja_var = "uživatel byl příliš líný na napsání recenze")
    return render_template("form.html", jinja_var = recenze)
    # recenze = request.args.get("recenze")
    # if recenze == "nic":
    #     return render_template("/form", jinja_var = "uživatel byl příliš líný na napsání recenze")
#    else:
#      return render_template("/form", jinja_var = recenze)
   


# request.form.get("???")
# print("???")
# cursor.execute("???")
# if request.method == "POST"


if __name__ == "__main__": #aplikace se spustí pouze když je soubor spuštěn přímo
    app.run(debug=True) #umožňuje automatický restart kodu a zobrazování chybových hlášek
