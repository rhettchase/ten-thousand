welcome_message = "Welcome to Ten Thousand\n(y)es to play or (n)o to decline"

def play():
    print(welcome_message)
    response = input("> ")
    if response.lower() == "n":
        print("OK. Maybe another time")

if __name__ == "__main__":
    play()