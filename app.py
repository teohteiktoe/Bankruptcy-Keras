from flask import Flask
app = Flask(__name__)

from flask import request, render_template
from keras.models import load_model 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA, TLTA, WCTA)
        model = load_model("BKR")
        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])
        print(pred)
        try:
            s = "Our predict DBS price is : " + str(pred[0][0])
        except:
            s = "Something went wrong in prediction"
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))

if __name__ == "__main__":
    app.run()





# In[ ]:




