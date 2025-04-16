from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get user input from the request
        user_input = request.json["message"]

        # Tokenize the user input
        inputs = tokenizer.encode(user_input, return_tensors="pt")

        # Generate a response using the model
        outputs = model.generate(inputs, max_length=50, num_return_sequences=1)

        # Decode the generated response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)})

# This is needed for Render deployment (binds to 0.0.0.0 and uses PORT env)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
@app.route("/")
def home():
    return "Your AI app is running! Use the /chat endpoint to send a POST request."

