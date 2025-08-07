from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def get_fitness_plan(condition, age, gender):
    prompt = f"""
    The user is {age} years old, {gender}, and classified as {condition}.
    Create two separate tables in pure HTML (no Markdown):
    1. A daily diet plan for one week with columns: Day, Breakfast, Lunch, Dinner, Snacks.
    2. A workout plan for one week with columns: Day, Workout, Duration.
    Keep the tables clean, compact, and visually balanced for web display.
    Do not include extra explanations — only return the HTML tables.
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    html_tables = response.choices[0].message.content.strip()

    parts = html_tables.split("</table>")
    diet_plan = parts[0] + "</table>" if len(parts) > 0 else ""
    workout_plan = parts[1] + "</table>" if len(parts) > 1 else ""

    return diet_plan, workout_plan
