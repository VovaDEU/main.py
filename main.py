import random
import PySimpleGUI as sg

class NumberGuesser:
    def __init__(self, target_number):
        self.target_number = target_number

    def guess_number(self, user_guess):
        try:
            user_guess = int(user_guess)

            if user_guess < self.target_number:
                print("Загадане число більше.")
            elif user_guess > self.target_number:
                print("Загадане число менше.")
            else:
                print(f"Вітаємо! Ви вгадали число {self.target_number}")

        except ValueError:
            print("Будь ласка, введіть ціле число.")

class InputHandler:
    def get_user_input(self):
        layout = [
            [sg.Text('Спробуйте вгадати число від 1 до 100:')],
            [sg.Text('Вгадайте число'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

        window = sg.Window('Window Title', layout)
        event, values = window.read()
        window.close()

        return values[0] if event != sg.WIN_CLOSED and event != 'Cancel' else None

def main():
    target_number = random.randint(1, 100)
    input_handler = InputHandler()
    game = NumberGuesser(target_number)

    while True:
        user_input = input_handler.get_user_input()

        if user_input is None:
            break

        game.guess_number(user_input)

if __name__ == "__main__":
    main()
