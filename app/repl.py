from app.command_handler import CommandHandler

class REPL:
    def __init__(self):
        self.handler = CommandHandler()

    def start(self):
        print("Interactive Calculator")
        print("Type a command (add, subtract, multiply, divide) followed by two numbers, or 'exit' to quit.")


        while True:
            user_input = input("Enter command: ").strip().split()
            if not user_input:
                continue
            if user_input[0].lower() == "exit":
                print("Exiting...")
                break
            if len(user_input) != 3:
                print("Invalid input. Please enter: command number1 number2")
                continue

            command_name, num1, num2 = user_input
            try:
                num1 = float(num1)
                num2 = float(num2)
                result = self.handler.execute(command_name, num1, num2)
                print("Result:", result)
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    REPL().start()