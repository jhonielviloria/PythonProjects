import os
import tkinter as tk
from tkinter import filedialog


def renameFiles():
    dir = e_dir.get()
    file_type = e_ftypes.get()
    new_filename = e_new_fname.get()
    i = int(e_index.get())

    for file in os.listdir(dir):
        fullpath = os.path.join(dir, file)
        if os.path.isfile(fullpath) and os.path.splitext(fullpath)[1] == file_type:
            new_fullpath = os.path.join(dir, new_filename + f'{i}' + file_type)
            os.rename(fullpath, new_fullpath)
            i += 1


def selectDir():
    path = filedialog.askdirectory(initialdir=os.getcwd(), title="Select Folder")
    e_dir.delete(0, tk.END)
    e_dir.insert(0, path)


root = tk.Tk()
root.title("File Rename Tool")
lbl_dir = tk.Label(root, text="Directory")
lbl_dir.grid(row=0, column=0)

lbl_new_fname = tk.Label(root, text="Enter new filename")
lbl_new_fname.grid(row=1, column=0)

e_dir = tk.Entry(root)
e_dir.insert(0, os.getcwd())
e_dir.grid(row=0, column=1)

e_new_fname = tk.Entry(root)
e_new_fname.insert(0, "new filename")
e_new_fname.grid(row=1, column=1)

btn_rename = tk.Button(root, text="Rename Files", command=renameFiles)
btn_rename.grid(row=2, column=1)

btn_dir = tk.Button(root, text="Select Directory", command=selectDir)
btn_dir.grid(row=0, column=3)

# Other Features:
lbl_other = tk.Label(root, text="Other options:")
lbl_other.grid(row=3, column=0)

lbl_index = tk.Label(root, text="Filename index:")
lbl_index.grid(row=4, column=0)

e_index = tk.Entry(root)
e_index.insert(0, 0)
e_index.grid(row=4, column=1)

lbl_ftypes = tk.Label(root, text="Filetype:")
lbl_ftypes.grid(row=5, column=0)

e_ftypes = tk.Entry(root)
e_ftypes.insert(0, ".txt")
e_ftypes.grid(row=5, column=1)


root.mainloop()