from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    revenue = float(data["revenue"])
    expenses = float(data["expenses"])
    electricity = float(data["electricity"])
    waste = float(data["waste"])

    profit = revenue - expenses
    profit_margin = (profit / revenue) * 100 if revenue > 0 else 0

    business_score = 70 if profit_margin > 15 else 40
    sustainability_score = 70 if (electricity + waste) < (0.15 * revenue) else 40

    final_score = int(0.6 * business_score + 0.4 * sustainability_score)

    status = "High Success Chance"
    if final_score < 45:
        status = "High Failure Risk"
    elif final_score < 75:
        status = "Medium Risk"

    return jsonify({
        "profit": profit,
        "business_score": business_score,
        "sustainability_score": sustainability_score,
        "final_score": final_score,
        "status": status
    })

if __name__ == "__main__":
    app.run(debug=True)
