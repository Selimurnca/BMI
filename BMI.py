from tkinter import *


#Screen
window = Tk()
window.title("Python Tkinter")
window.minsize(width=200,height=350)
window.configure(background="#4b81ac")
#func
def bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Santimetreyi metreye çeviriyoruz.
        if weight <= 5 or weight > 500:
            result_label.config(text="Kilo geçersiz!",font=("Arial", 16 , "bold") , fg="red")
            return
        if height <= 0.5 or height > 3:
            result_label.config(text="Boy geçersiz!",font=("Arial", 16 ,"bold") , fg="red")
            return

        bmi_result = weight / (height * height)

        if bmi_result < 18.5:
            result_text = f"BMI: {bmi_result:.2f} - Zayıf"
            result_label.config(text=result_text, font=("Arial", 16, "bold"), fg="green")
        elif bmi_result < 25:
            result_text = f"BMI: {bmi_result:.2f} - Normal"
            result_label.config(text=result_text, font=("Arial", 16, "bold"), fg="darkgreen")
        elif bmi_result < 30:
            result_text = f"BMI: {bmi_result:.2f} - Fazla Kilolu"
            result_label.config(text=result_text, font=("Arial", 16, "bold"), fg="blue")
        else:
            result_text = f"BMI: {bmi_result:.2f} - Obez"
            result_label.config(text=result_text, font=("Arial", 16, "bold"), fg="darkblue")

    except ValueError:
        result_label.config(text="Lütfen geçerli bir sayı girin!", fg="red")






#Label
result_label = Label(text="", font=("Arial", 15) , bg="#4b81ac")
result_label.grid(row=9, column=0,padx=5,pady=5 )




weight_label = Label(text="Enter your weight(kg)",font=("Arial", 15,"bold"),fg="white",bg="#4b81ac")
weight_label.grid(row=0,column=0,padx=5,pady=5)

height_label = Label(text="Enter your height(cm)",font=("Arial",15, "bold"),fg="white",bg="#4b81ac")
height_label.grid(row=3,column=0,padx=5,pady=5)

#Entry
entry_weight = Entry(width=10)
entry_weight.grid(row=2,column=0,padx=10,pady=10)

entry_height = Entry(width=10)
entry_height.grid(row=4,column=0,padx=10,pady=10)

#Button
submit = Button(text="Submit",command=bmi, bg="#4b81ac",fg="white",font=("Arial",15,"bold"))
submit.grid(row=6,column=0,padx=5,pady=5)
















window.mainloop()
