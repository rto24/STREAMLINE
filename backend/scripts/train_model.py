import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_dataset(file_path):
  with open(file_path, "r") as f:
    return json.load(f)

def create_prompts(dataset):
  """
  Converts the dataset into structured prompts.
  """
  prompts = []
  for example in dataset:
      prompt = f"Input: {example['input']}\nOutput: {example['output']}"
      prompts.append(prompt)
  return prompts

if __name__ == "__main__":
  dataset_path = "backend/data/train.json"
  dataset = load_dataset(dataset_path)
  prompts = create_prompts(dataset)

  with open("backend/data/prompts.json", "w") as f:
    json.dump(prompts, f, indent=2)

  print("Prompts created and saved. You can use these with GPT-4 during inference.")