from flask import Flask, request, jsonify
import anthropic
import os

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("CLAUDE_API_KEY"))

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Analyze this trading data and identify support, resistance and order blocks: {data}"
        }]
    )
    
    return jsonify({"analysis": message.content[0].text})

@app.route('/')
def home():
    return "TradingView-Claude Bridge is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
