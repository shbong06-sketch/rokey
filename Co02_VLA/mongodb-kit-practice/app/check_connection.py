from database import (
    check_connection,
    close_connection,
)


def main():
    try:
        result = check_connection()

        print("MongoDB connection successful")
        print(f"Ping result: {result}")

    except Exception as error:
        print("MongoDB connection failed")
        print(f"Error: {error}")
        raise

    finally:
        close_connection()


if __name__ == "__main__":
    main()