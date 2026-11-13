"""Fetch and summarize users from the public JSONPlaceholder API."""
import json
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users(url: str = API_URL) -> list[dict]:
    request = Request(url, headers={"User-Agent": "CSE103-Lab3/1.0"})
    with urlopen(request, timeout=15) as response:
        if response.status != 200:
            raise RuntimeError(f"Unexpected HTTP status: {response.status}")
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, list):
        raise ValueError("Expected the API response to be a JSON array.")
    return data


def summarize_users(users: list[dict]) -> list[dict]:
    return [
        {
            "id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email"),
            "city": user.get("address", {}).get("city"),
        }
        for user in users
    ]


def main() -> None:
    try:
        users = fetch_users()
        summary = summarize_users(users)
        print(f"Total users received: {len(summary)}")
        for user in summary:
            print(f'{user["id"]}. {user["name"]} (@{user["username"]}) — {user["email"]}')
        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(users, file, indent=2, ensure_ascii=False)
        print("Saved raw API response to users.json")
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, ValueError, RuntimeError) as error:
        print(f"API request failed: {error}")
        print("Check your internet connection and try again.")


if __name__ == "__main__":
    main()
