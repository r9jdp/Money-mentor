from flask import Flask, request , render_template , jsonify,redirect , send_file
import gemini

app = Flask(__name__)

mainList = []

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == 'POST':
        prompt1 = request.form["salary"]
        prompt2 = request.form["goal"]
        prompt3 = request.form["needs"]
        prompt4 = request.form["message"]

        global mainList
        mainList = mainList + [prompt1,prompt2,prompt3,prompt4]

        # return jsonify({"recommendations" : (gemini.gemini(prompt1,prompt2,prompt3,prompt4))})
        mylist = []
        for items in gemini.gemini(prompt1,prompt2,prompt3,prompt4):
            mylist.append([items["action"],items["amount"]])
        graph_data = {"params" : mylist}
        print(mainList)
        return render_template("result.html" , data = gemini.gemini(prompt1,prompt2,prompt3,prompt4) , salary = request.form["salary"] , graph_data = graph_data)
    else:
        return render_template("index.html")

@app.route("/taxation/csv")
def csv_download():
    return send_file("./static/Taxation.csv")

@app.route("/taxation", methods=["POST","GET"])
def taxation():
    if request.method == "GET":
        return render_template("taxation.html" )
    if request.method=="POST":
        age = request.form["age"]
        location = request.form["location"]
        family = request.form["family"]
        investment = request.form["investment"]
        debt = request.form["debt"]
        global mainList
        value = gemini.Taxation(age,location,family,investment,debt,salary=mainList[0],needs=mainList[1],goal=mainList[2],message=mainList[3])
        gemini.csv({"Tax Redemption methods" : value} , "Taxation")
        return render_template("Taxation_result.html" , taxData = value)


if __name__ == "__main__":
    app.run(debug = True)