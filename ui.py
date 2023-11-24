import os
import tkinter as tk
import tkinter.messagebox       # doesn't come with original tkinter
import paperselection
path = "D:\\Study\\Uni\\Yr1"

window = tk.Tk()
window.geometry('920x500')
global course 

# Get the Courses Listbox
file_name_list = paperselection.get_courses(path)
listbox_course = tk.Listbox(window,width=40,height=len(file_name_list),selectmode = "MULTIPLE")
for i in range(len(file_name_list)):
    listbox_course.insert(i,file_name_list[i])



def select_courses(listbox):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    if selected_indices:
        index =selected_indices[0]
        course = listbox.get(index)
        


# Bottom to trigger the further menu
btn_selected = tk.Button(master=window, text="Select", command=lambda:course == select_courses(listbox_course))
btn_selected.pack(side="bottom")

'''
file_inner_name_list = paperselection.get_courses(os.path.join(path,course))
listbox = tk.Listbox(window,width=40,height=len(file_inner_name_list),selectmode = "MULTIPLE")
for i in range(len(file_inner_name_list)):
    listbox.insert(i,file_inner_name_list[i])
'''
listbox_course.pack()

window.mainloop()