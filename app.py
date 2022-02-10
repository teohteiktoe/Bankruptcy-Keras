#!/usr/bin/env python
# coding: utf-8

# In[14]:


from flask import Flask


# In[15]:


app = Flask(__name__)


# In[16]:


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
        pred = pred[0][0]
        s = "The predicted bankruptcy score is : " + str(pred)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




