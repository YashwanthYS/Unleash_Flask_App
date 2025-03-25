import requests

model_a_count = 0
model_b_count = 0

url = "http://127.0.0.1:5000/recommend"


for i in range(100):
    user_id = f"user{i}"
    response = requests.get(url, params={"user_id": user_id})

    if response.status_code != 200:
        print(f"[ERROR] User {user_id}: Failed with status code {response.status_code}")
        continue

    data = response.json()
    model = data.get("model_used")
    
    if model == "Model A":
        model_a_count += 1
    elif model == "Model B":
        model_b_count += 1
    else:
        print(f"[WARNING] Unexpected model for user {user_id}: {model}")

print("\n=== Rollout Summary ===")
print(f"Model A users: {model_a_count}")
print(f"Model B users: {model_b_count}")
print(f"Model A %: {model_a_count} %")
print(f"Model B %: {model_b_count} %")
