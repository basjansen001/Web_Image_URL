from tkinter import *
from urllib import request
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

        text_frame.pack()

        button_save_url = Button(frame, text="Make image", command= lambda: self.download_file_from_url(entry_widget))
        button_save_url.pack()

    def download_file_from_url(self, input_url):
        r = random.randrange(1,100)
        img_response = request.urlopen(input_url).read()
        image_file = open("image" + str(r) + ".jpg", "w")
        print(image_file.name)
        try:
            image_file.write(img_response)
        except Exception:
            print("Cant create an image from the given url")
        finally:
            image_file.close()


root = Tk()
w = MainWindow(root)
root.mainloop()