from flask import Flask, render_template 


app = Flask(__name__,template_folder="templates",static_folder="static")


@app.get("/")
def index():
    return render_template("index.html",title="Главная страница ")


if __name__ == "__main__":
    app.run( debug=True,)
