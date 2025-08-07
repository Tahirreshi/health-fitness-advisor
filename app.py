from flask import Flask, render_template, request
from utils.health_calc import calculate_bmi, classify_health
from utils.groq_ai import get_fitness_plan
from utils.visualizer import plot_bmi_chart
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        height = float(request.form["height"]) / 100  # cm to m
        weight = float(request.form["weight"])
        age = int(request.form["age"])
        gender = request.form["gender"]

        bmi = calculate_bmi(weight, height)
        condition = classify_health(bmi)

        diet_plan, workout_plan = get_fitness_plan(condition, age, gender)

        chart_path = plot_bmi_chart(bmi)
        
        return render_template("result.html", bmi=bmi, condition=condition,
                               diet_plan=diet_plan, workout_plan=workout_plan,
                               chart_path=chart_path)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
