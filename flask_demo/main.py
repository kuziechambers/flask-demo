from flask_demo.site import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


def main():
    """
    Core project logic

    Args:

    Returns:
    """
    print("hello")
