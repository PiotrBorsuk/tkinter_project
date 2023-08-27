from tkinter import *
import dim_metrics
from tkinter import filedialog
from tkcalendar import DateEntry

root = Tk()
root.title('GA4 connector')
root.geometry("500x500")
dim_list = dim_metrics.dims
metrics = dim_metrics.metrics
current_row = 0

filter_options = ('contains','>','<','does not contain')
my_dir='' # string to hold directory path
def my_fun():
    my_dir = filedialog.askdirectory() # select directory
    l2.config(text=my_dir) # update the text of Label with directory path

l1=Label(root, text='Dimensions', font=('Helvetica 15'),
      background="gray74")
l1.grid(row=current_row, column=0, padx=20, sticky='w')
current_row+=1
def get_date():
    selected_date = cal1.get()
    print(f"Selected date: {selected_date}")

menu = StringVar()
menu.set("Choose var")


dim_variables = []
for element in dim_list:
    var_ejecutar = f"global {element}"
    exec(var_ejecutar)

    var_ejecutar = f"{element}=DoubleVar()"
    exec(var_ejecutar)

    dim_variables.append(f"{element}")

    var_ejecutar = f"""l = Checkbutton(root, text=\"{str(element)}\", 
        variable={element},onvalue = 1,offvalue = 0)"""
    exec(var_ejecutar)

    var_ejecutar = "l.grid(row=current_row,column=0,padx=20,pady=0,sticky='w')"
    current_row+=1
    exec(var_ejecutar)

metric_label=Label(root, text='metrics', font=('Helvetica 15'),
      background="gray74")
current_row+=1
metric_label.grid(row=current_row,column=0,padx=20,sticky='w')
current_row+=1

metrics_vars = []
for element in metrics:
    print(element)
    var_ejecutar = f"global {element}"
    exec(var_ejecutar)

    var_ejecutar = f"{element}=DoubleVar()"
    exec(var_ejecutar)

    dim_variables.append(f"{element}")

    var_ejecutar = f"""l = Checkbutton(root, text=\"{str(element)}\", 
        variable={element},onvalue = 1,offvalue = 0)"""
    exec(var_ejecutar)

    var_ejecutar = "l.grid(row=current_row,column=0,padx=20,pady=0,sticky='w')"
    current_row+=1
    exec(var_ejecutar)

    current_row+=1

filtering_label=Label(root, text='Filters', font=('Helvetica 15'),
      background="gray74")
filtering_label.grid(row=current_row,column=0,padx=20,sticky='w')
current_row+=1

cal1 = DateEntry(root, date_pattern="yyyy-mm-dd")
cal1.grid(row=current_row,column=0,padx=20,pady=10,sticky='w')

cal2 = DateEntry(root, date_pattern="yyyy-mm-dd")
cal2.grid(row=current_row,column=1,padx=0,pady=10,sticky='w')
current_row += 1

drop = OptionMenu(root, menu, *(dim_list+metrics))
drop.grid(row=current_row, column=0, padx=20, pady=0, sticky='w')
current_row += 1

b1=Button(root,text='Select directory', font=22,
    command=lambda:my_fun(),bg='lightgreen')
b1.grid(row=current_row, column=0,padx=0,pady=20)
l2=Label(root,text=my_dir, bg='yellow',font=18)
l2.grid(row=current_row, column=1,padx=2)
date_btn = Button(root, text="Click Here To Return a Date ", command=get_date)

print(get_date())
root.mainloop()  # Keep the window open