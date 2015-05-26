from tkinter import *
import urllib.request
import random


class MainWindow:
    def __init__(self, master):
        frame = Frame(master, width=800, height=650)
        frame.pack()

        text_frame = Frame(master)

        entry_label = Label(text_frame)
        entry_label["text"] = "Enter url"
        entry_label.pack(side=LEFT)

        entry_widget = Entry(text_frame)
        entry_widget["width"] = 50
        entry_widget.pack(side=LEFT)

        # Get the text value of the entry
        text_value = entry_widget.get()

        text_frame.pack()

        button_save_url = Button(frame, text="Make image", command=lambda: self.download_file_from_url(text_value))
        button_save_url.pack()

    def download_file_from_url(self, input_url):
        if not input_url:
            return

        print("test")

        r = random.randrange(1,100)
        file_name = "image" + str(r) + ".jpg"

        try:
            urllib.request.urlretrieve(input_url, file_name)
        except Exception:
            print("Cant create an image from the given url")


root = Tk()
w = MainWindow(root)
root.mainloop()
