# pip install google-genai
# Acessar o site google studio ia e pegar a chave da API e colcar no "TOKEN"
import json
from google import genai
from google.genai import types
prompt = ""
token = ''
client = genai.Client(api_key=token)

def str_to_dict(data: str) -> dict | None:
    try:
        return json.loads(data)
    except Exception as e:
        return {"erro": e, "resp": data}

with open("teste.md", encoding="utf-8") as e:
    for line in e.readlines():
        prompt += line

contents = [
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]

user_content = types.Content(role="user", parts=[types.Part.from_text(text=input(":> "))])
contents.append(user_content)
response = client.models.generate_content(model="gemini-2.5-flash", contents=contents)
text = response.text.strip("```json").strip("```").strip()
respt = str_to_dict(text)
print(f"Type: {type(respt)} Resp: {respt}")