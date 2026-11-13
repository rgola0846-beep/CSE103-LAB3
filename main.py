def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to CSE103 Lab 3."


def main() -> None:
    print(greet("Rohit"))
    print("Repository: CSE103-LAB3")
    print("Topics: Git, GitHub, Markdown, debugging, and APIs.")


if __name__ == "__main__":
    main()
