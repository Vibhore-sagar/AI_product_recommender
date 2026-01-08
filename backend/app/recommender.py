import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_recommendations(preference: str, products: list):
    product_text = "\n".join(
        [f"{p.name} - ${p.price} - {p.features}" for p in products]
    )

    prompt = f"""
User preference: {preference}

Available products:
{product_text}

Recommend suitable products ONLY from the list.
Return only product names separated by commas.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
