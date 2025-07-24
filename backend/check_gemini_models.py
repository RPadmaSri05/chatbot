import google.generativeai as genai

genai.configure(api_key="AIzaSyD9XsbBku0pyzHvoavHkWbw-zDzcRBr0yk")

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

response = model.generate_content("Say hello!")
print(response.text)

