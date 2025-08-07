import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_bmi_chart(bmi):
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    ranges = [18.5, 24.9, 29.9, 35]
    colors = ["skyblue", "lightgreen", "orange", "red"]

    fig, ax = plt.subplots()
    sns.barplot(x=categories, y=ranges, palette=colors, ax=ax)
    ax.axhline(y=bmi, color="black", linestyle="--", label=f"Your BMI: {bmi}")
    ax.set_ylabel("BMI Value")
    ax.set_title("BMI Categories")

    ax.legend()
    os.makedirs("static/charts", exist_ok=True)
    chart_path = f"static/charts/bmi_chart.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path
