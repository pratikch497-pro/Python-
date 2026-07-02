import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class RockPaperScissorGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        # Game Variables
        self.player_name = ""
        self.score = 0
        self.computer_score = 0
        self.total = 0
        self.draw = 0
        self.choices = ['stone', 'paper', 'scissor']

        # UI Elements: Name Input Screen
        self.label = Label(text="Welcome! Enter your name to start:", font_size='20sp')
        self.add_widget(self.label)

        self.name_input = TextInput(hint_text="Your Name", multiline=False, size_hint_y=None, height=50)
        self.add_widget(self.name_input)

        self.start_btn = Button(text="Start Game", size_hint_y=None, height=50, background_color=(0, 1, 0, 1))
        self.start_btn.bind(on_press=self.start_game)
        self.add_widget(self.start_btn)

    def start_game(self, instance):
        name = self.name_input.text.strip()
        if name == "":
            self.label.text = "Please enter a valid name!"
            return
        
        self.player_name = name
        self.clear_widgets()

        # New UI Layout for Game
        self.label = Label(text=f"Hello {self.player_name}!\nChoose Stone, Paper, or Scissor.", font_size='18sp', halign='center')
        self.add_widget(self.label)

        # Buttons for Choices
        btn_layout = BoxLayout(spacing=10, size_hint_y=None, height=60)
        for choice in self.choices:
            btn = Button(text=choice.capitalize())
            btn.bind(on_press=lambda btn_obj: self.play_round(btn_obj.text.lower()))
            btn_layout.add_widget(btn)
        self.add_widget(btn_layout)

        # Stats Label
        self.stats_label = Label(text="Score - You: 0 | Computer: 0", font_size='16sp')
        self.add_widget(self.stats_label)

        # Exit/Results Button
        exit_btn = Button(text="End Game & See Stats", size_hint_y=None, height=50, background_color=(1, 0, 0, 1))
        exit_btn.bind(on_press=self.show_results)
        self.add_widget(exit_btn)

    def play_round(self, player_choice):
        computer_choice = random.choice(self.choices)
        self.total += 1

        if player_choice == computer_choice:
            self.draw += 1
            result = f"Draw! Both chose {player_choice}."
        elif (computer_choice == 'stone' and player_choice == 'paper') or \
             (computer_choice == 'paper' and player_choice == 'scissor') or \
             (computer_choice == 'scissor' and player_choice == 'stone'):
            self.score += 1
            result = f"YOU WIN🏆!\nComputer chose {computer_choice}."
        else:
            self.computer_score += 1
            result = f"YOU LOSE.\nComputer chose {computer_choice}."

        self.label.text = result
        self.stats_label.text = f"Score - You: {self.score} | Computer: {self.computer_score}"

    def show_results(self, instance):
        self.clear_widgets()
        if self.total == 0:
            result_text = "NO GAME PLAYED.\nThanks for stopping by!"
        else:
            p_accuracy = (self.score / self.total) * 100
            c_accuracy = (self.computer_score / self.total) * 100
            
            if self.score > self.computer_score:
                winner = f"{self.player_name}, you are the winner!"
            elif self.computer_score > self.score:
                winner = "Computer is the winner."
            else:
                winner = "It's an overall draw!"

            result_text = (
                f"--- THE ACCURACY ---\n"
                f"Total rounds: {self.total}\n"
                f"Draws: {self.draw}\n"
                f"Your Accuracy: {p_accuracy:.1f}%\n"
                f"Computer Accuracy: {c_accuracy:.1f}%\n\n"
                f"RESULT: {winner}\n\n"
                f"Thanks for playing!"
            )

        self.add_widget(Label(text=result_text, font_size='16sp', halign='center'))

class GameApp(App):
    def build(self):
        return RockPaperScissorGame()

if __name__ == '__main__':
    GameApp().run()
