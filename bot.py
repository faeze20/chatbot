from mykey import my_api_key
import openai
my_api_key ="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"
openai.api_key =my_api_key

# messages=[]
# while True:
#         message=input("user: ")
#         if message:
#             messages.append({"role": "user", "content": message})
#             result = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        
#         reply=result.choices[0].message.content
#         print(f"chatgpt: {reply}")

from tkinter import *
# import tkinter as tk

window=Tk()
window.title("ChatBot")
window.minsize(500,600)
window.maxsize(600,700)
window.resizable(width=False,height=False)
window.geometry("500x600")

# """create labels"""

label1=Label(window,text="write your massage")
# label1.grid(row=1,column=7)
label1.pack()


"""create Text for input multiple line values from user"""
msg=Text(window,width=50,height=10)
# msg.grid(row=3,column=1)
msg.pack()




                          
# # print(completion.choices[0].message.content)
# # print(completion)
def chatbot():
    
    messages=[]
    while True:
        message=msg.get("1.0", "end-1c")
        if message:
            messages.append({"role": "user", "content": message})
            result = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        
        reply=result.choices[0].message.content
        text2.insert(END,f"chatgpt: {reply}\n")
        
def clear_data():
    msg.delete("1.0", "end") 
    
    
           
        
# """create buttons """        

Button(window,text="Submit",bg="yellow",fg="black",command=chatbot).pack()
# .grid(row=4,column=8)

button2=Button(window,text="clear_Data",command=clear_data,bg="green")
# button2.grid(row=4,column=7)
button2.pack()






"""create empty labels"""
text2=Text(window, width=60, height=20)
# define widget
scrollbar = Scrollbar(window)
# اتصال Scrollbar به ویجت Text
text2.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text2.yview)
text2.pack()
scrollbar.pack()
# text2.insert(END, "متن خروجی")
# text2.grid()
text2.pack()
window.mainloop()
