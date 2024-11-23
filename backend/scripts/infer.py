import openai
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from backend.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY  
print(OPENAI_API_KEY)
def generate_recommendations(input_text, model="gpt-4"):
  """
  Use GPT-4 via OpenAI API to generate music recommendations.
  """
  try:
    messages = [
      {"role": "system", "content": "You are an AI assistant that provides music recommendations based on user preferences."},
      {"role": "user", "content": input_text}
    ]

    response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      max_tokens=300,
      temperature=0.7,
    )

    return response.choices[0].message.content
  except Exception as e:
    print(f"Error generating recommendations: {e}")
    return None

if __name__ == "__main__":
  # Example input
  input_text = (
    "User likes tracks: Blinding Lights (danceability: 0.514, tempo: 171.005, energy: 0.740), "
    "Take My Breath (danceability: 0.592, tempo: 121.987, energy: 0.780). "
    "User's top artists: The Weeknd, Ariana Grande. "
    "User's top genres: pop, electropop, r&b, funk, dance pop, soul. "
    "Recommend 5 songs that match the user's taste in music."
  )

  recommendations = generate_recommendations(input_text)
  print("Recommendations:\n", recommendations)