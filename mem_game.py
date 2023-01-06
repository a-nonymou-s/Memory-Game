#Author : ANONY

import random
import tkinter as tk

class MemoryGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.stage = 1
        self.chances = 2
        self.numbers_frame = tk.Frame(self, bg="light blue")
        self.numbers_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.numbers_label = tk.Label(self.numbers_frame, text="", font=("Helvetica", 32), bg="light blue")
        self.numbers_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.entry = tk.Entry(self, font=("Helvetica", 32))
        self.submit_button = tk.Button(self, text="Submit", font=("Helvetica", 32), command=self.check_answer)
        self.title("Memory Game")
        self.iconphoto(False, tk.PhotoImage(file='memory.png'))

    def show_numbers(self):
        self.entry.pack_forget()
        self.submit_button.pack_forget()
        self.numbers = []
        for i in range(self.stage):
            number = str(random.randint(1, 10))
            while number in self.numbers:
                number = str(random.randint(1, 10))
            self.numbers.append(number)
        self.display_number(0)
        
    def display_number(self, index):
        if index < self.stage:
            self.numbers_label.config(text=self.numbers[index])
            self.after(1000, lambda: self.display_number(index + 1))
        else:
            self.hide_numbers()
            
    def hide_numbers(self):
        self.numbers_label.config(text="")
        self.entry.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.entry.focus_set()
        self.submit_button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
    def destroy_label(self, label):
        label.destroy()
        
    def check_answer(self):
        user_answer = str(self.entry.get())
        correct = " ".join(self.numbers)
        if user_answer == correct:
            if self.stage == 8:
                label1 = tk.Label(self, text="Congratulations! You won the game!", font=("Helvetica", 32))
                label1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                label2 = tk.Label(self, text=":)", font=("Helvetica", 32))
                label2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                self.after(3000, self.destroy_label, label1)
                self.after(3000, self.destroy_label, label2)
                self.after(3000, self.quit)  
            else:
                self.stage += 1
                label3 = tk.Label(self, text="Congratulations! Progressing to stage {}".format(self.stage), font=("Helvetica", 32))
                label3.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                self.chances = 3
                self.after(3000, self.destroy_label, label3)
                self.after(3000, self.show_numbers)  # Schedule the show_numbers method to be called after 3 seconds
        else:
            self.chances -= 1
            if self.chances > 0:
                label4 = tk.Label(self, text="Incorrect. {} chances remaining.".format(self.chances), font=("Helvetica", 32))
                label4.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                self.after(3000, self.destroy_label, label4)
                self.after(3000, self.show_numbers)  # Schedule the show_numbers method to be called after 3 seconds
            else:
                label5 = tk.Label(self, text="You lost the game.", font=("Helvetica", 32))
                label5.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                self.after(3000, self.destroy_label, label5)
                self.after(5000, self.quit)

if __name__ == "__main__":
    game = MemoryGame()
    game.show_numbers()
    game.mainloop()
