# Making an applictation completely with github copilot


import tkinter as tk
import time

def create_window():
    window = tk.Tk()
    window.title("Typing Speed Test")
    window.geometry("800x600")
    window.configure(bg='black')
    window.config(highlightbackground='grey', highlightthickness=2)  # Add grey border
    return window

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

words = load_words('/home/nasr/python/speetype/words.txt')

def display_words(window, words):
    text_widget = tk.Text(window, wrap='word', height=10, width=80, bg='black', fg='white', bd=0, highlightthickness=0)
    text_widget.pack(pady=20)
    text_widget.insert(tk.END, ' '.join(words[:20]))
    text_widget.config(state=tk.DISABLED)

    input_widget = tk.Entry(window, width=80, bg='black', fg='white', bd=0, highlightthickness=0, insertbackground='white')
    input_widget.pack(pady=20)

    time_label = tk.Label(window, text="", bg='black', fg='white')
    time_label.pack(pady=20)

    start_time = None

    def check_input(event):
        nonlocal start_time
        if start_time is None:
            start_time = time.time()

        typed_text = input_widget.get()
        displayed_text = ' '.join(words[:20])
        if typed_text == displayed_text[:len(typed_text)]:
            input_widget.config(fg='white')
        else:
            input_widget.config(fg='red')

        if event.keysym == 'Return':
            end_time = time.time()
            elapsed_time = end_time - start_time
            time_label.config(text=f"Time taken: {elapsed_time:.2f} seconds")
            input_widget.delete(0, tk.END)
            text_widget.config(state=tk.NORMAL)
            text_widget.delete(1.0, tk.END)
            new_words = words[20:40]  # Get the next set of words
            text_widget.insert(tk.END, ' '.join(new_words))
            text_widget.config(state=tk.DISABLED)
            input_widget.focus()
            start_time = None  # Reset the start time

    input_widget.bind('<KeyRelease>', check_input)

if __name__ == "__main__":
    app = create_window()
    display_words(app, words)
    app.mainloop()
