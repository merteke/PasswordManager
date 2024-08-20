from tkinter import *
import random
from tkinter import messagebox
import json


    


#Global Var
BLACKPEARL_COLOR="#070f2b"
BLUEZODIAC_COLOR="#1b1a55"
DUSKYBLUE_COLOR="#535c91"
BLUEBELL_COLOR="#9290c3"
TEXT_FONT="New Amsterdam"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




#passwords.txt
def save():
    website=web_text.get()
    e_mail=email_text.get()
    password=password_text.get()
    new_data={website:{"E-mail":e_mail,"Password":password}}
    
    if len(website)==0 or len(e_mail)==0 or len(password)==0:
        messagebox.showinfo(title="Oops!",message="Please make sure you dont left any informations empty.")
        
    elif messagebox.askokcancel(title="Confirm",message="Do you want to save information?"):
        with open("passwords.txt","a") as password_txt:
            password_txt.write(f"{website} | {e_mail} | {password}\n")
        try:
            with open("passwords.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("passwords.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file,indent=4)
        finally:
            password_text.delete(0,END)
            email_text.delete(0,END)
            web_text.delete(0,END)


#Search password mechanism
def search():
    website=web_text.get()
    with open("passwords.json","r") as data:
        data_dict=json.load(data)
        try:
            messagebox.showinfo(title=f"{website} information",message=data_dict[website])
        except:
            messagebox.showerror(message="No information available!")
        
    
    
    
        



#Generate Random password
def generate():
    global LETTERS,NUMBERS,SYMBOLS
    password_text.delete(0,END)
    random_password=[]
    letter_n=random.randint(8,10)
    number_n=random.randint(2,4)
    symbol_n=random.randint(2,4)
    pass_len=letter_n+number_n+symbol_n
    for _ in range(letter_n):
        random_password.append(random.choice(LETTERS))
    for _ in range(number_n):
        random_password.append(random.choice(NUMBERS))
    for _ in range(symbol_n):
        random_password.append(random.choice(SYMBOLS))
    random.shuffle(random_password)
    random_password="".join(random_password)
    password_text.insert(0,string=random_password)
    password_text.clipboard_append(string=random_password)
    
    

    
#UI setup
window=Tk()
window.minsize(height=600,width=600)
window.config(bg=BLACKPEARL_COLOR)
window.title("Password Generator")
x=(1920/2)-(600/2)
y=(1080/2)-(600/2)
window.geometry(f'{600}x{600}+{int(x)}+{int(y)}')



canvas=Canvas(width=200,height=200,bg=BLACKPEARL_COLOR,highlightthickness=0)
img=PhotoImage(file="lock_resize.png")
canvas.create_image(100,100,image=img)
canvas.place(x=300,y=0,anchor="n")

#Website
web_label=Label(text="Website:",font=(TEXT_FONT,16,"bold"))
web_label.place(x=75,y=200,anchor="n")
web_label.config(bg=BLACKPEARL_COLOR,fg=BLUEBELL_COLOR)
web_text=Entry(font=(TEXT_FONT,16,"normal"),fg=BLUEZODIAC_COLOR)
web_text.place(x=212,y=200,width=175,height=30,anchor="n")

#Email
email_label=Label(text="E-Mail:",font=(TEXT_FONT,16,"bold"))
email_label.place(x=85,y=250,anchor="n")
email_label.config(bg=BLACKPEARL_COLOR,fg=BLUEBELL_COLOR)
email_text=Entry(font=(TEXT_FONT,16,"normal"),fg=BLUEZODIAC_COLOR)
email_text.place(x=300,y=250,width=350,height=30,anchor="n")

#Password
password_label=Label(text="Password:",font=(TEXT_FONT,16,"bold"))
password_label.place(x=65,y=300,anchor="n")
password_label.config(bg=BLACKPEARL_COLOR,fg=BLUEBELL_COLOR)
password_text=Entry(font=(TEXT_FONT,8,"normal"),fg=BLUEZODIAC_COLOR)
password_text.place(x=212,y=300,width=175,height=30,anchor="n")


#Generate Button
generate_button=Button(text="Generate Password",font=(TEXT_FONT,12,"bold"),fg=BLUEZODIAC_COLOR,bg=BLUEBELL_COLOR,command=generate)
generate_button.place(x=400,y=300,width=175,height=30,anchor="n")

#ADD BUTTON
save_button=Button(text="Save",font=(TEXT_FONT,12,"bold"),fg=BLUEZODIAC_COLOR,bg=BLUEBELL_COLOR,command=save)
save_button.place(x=300,y=400,width=175,height=30,anchor="n")

#Search button
search_button=Button(text="Search",font=(TEXT_FONT,12,"bold"),fg=BLUEZODIAC_COLOR,bg=BLUEBELL_COLOR,command=search)
search_button.place(x=400,y=200,width=175,height=30,anchor="n")




























window.mainloop()