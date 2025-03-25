from flask import Flask, request, jsonify
from UnleashClient import UnleashClient

# Simulated model functions
def model_a(user_id):
    return [f"Classic pick for {user_id}", "Movie A", "Movie B"]

def model_b(user_id):
    return [f"Fresh pick for {user_id}", "Movie X", "Movie Y"]

# Initialize Unleash client
unleash_client = UnleashClient(
    url="http://localhost:4242/api",
    app_name="streamly-service",
    instance_id="rec-v1",
    environment="production",
    custom_headers={"Authorization": "*:production.31d352b92cca95bac37c9d75bf986580205866f7031392a87d9b38f3"}
)

unleash_client.initialize_client()

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    user_id = request.args.get("user_id", "default-user")
    context = {"userId": user_id}

    if unleash_client.is_enabled("recommendationModelV2", context):
        recommendations = model_b(user_id)
        model_used = "Model B"
    else:
        recommendations = model_a(user_id)
        model_used = "Model A"

    return jsonify({
        "user_id": user_id,
        "model_used": model_used,
        "recommendations": recommendations
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
