import tkinter

root = tkinter.Tk()
root.geometry("800x500")
root.title("Router Planner App")

#entry = tkinter.Entry(root)
#entry.pack()


def Confirm():
    with open("stations.txt", "r") as f: 
        if user_input.get() in f.read(): 
            alabel = tkinter.Label(root, text="You have confirmed " + user_input.get()).pack()
        else: 
            blabel = tkinter.Label(root, text="Not found").pack()

user_input = tkinter.Entry(root)
user_input.insert(0, "From")
user_input.pack()

button = tkinter.Button(root, text="Enter", command=Confirm)
button.pack()

user_input = tkinter.Entry(root)
user_input.insert(0, "To")
user_input.pack()

button = tkinter.Button(root, text="Enter", command=Confirm)
button.pack(pady=20)


            
            


root.mainloop()
