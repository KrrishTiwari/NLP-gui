from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API
class NLPAPP:

  def __init__(self):
      #GUI OF LOGIN PAGE
      self.root = Tk()
      self.root.title("NLP App")
      self.root.geometry("500x700")
      self.root.configure(bg= "#757272")
      self.root.iconbitmap("resources/favicon.ico")

      self.dbo = Database()
      self.apio = API()
      self.login_gui()
      self.root.mainloop()



  def login_gui(self):
      self.clear()
      heading = Label(self.root,text ="Welcome to NLPApp", bg= "#757272", fg= "white")
      heading.pack(pady= (30,30))
      heading.configure(font=("verdana",25,"bold"))

      label1 = Label(self.root,text= "Enter Email:",bg="#757272", fg="white" )
      label1.pack(pady=(10,10))
      self.email = Entry(self.root,width= 35)
      self.email.pack(pady=(10,10), ipady=5)

      label2 = Label(self.root, text="Enter Password:", bg="#757272", fg="white")
      label2.pack(pady=(10, 10))
      self.password = Entry(self.root, width=35, show="*")
      self.password.pack(pady=(10, 10), ipady=5)

      login_button = Button(self.root, text= "Login", width=25, height=2, command=self.perf_login)
      login_button.pack(pady=(40,15),ipady = 5)

      label3 = Label(self.root, text="Not a Member?")
      label3.pack(pady=(15, 15))

      redirect_button = Button(self.root, text="Register NOW:",command=self.register)
      redirect_button.pack(pady=(10, 10))


  def register(self):
#clear the existing gui
      self.clear()
      heading = Label(self.root,text ="Welcome to NLPApp", bg= "#757272", fg= "white")
      heading.pack(pady= (30,30))
      heading.configure(font=("verdana",25,"bold"))

      label0= Label(self.root,text= "Enter Name:",bg="#757272", fg="white" )
      label0.pack(pady=(10,10))
      self.name = Entry(self.root,width= 35)
      self.name.pack(pady=(10,10), ipady=5)


      label1 = Label(self.root,text= "Enter Email:",bg="#757272", fg="white" )
      label1.pack(pady=(10,10))
      self.email = Entry(self.root,width= 35)
      self.email.pack(pady=(10,10), ipady=5)

      label2 = Label(self.root, text="Enter Password:", bg="#757272", fg="white")
      label2.pack(pady=(10, 10))
      self.password = Entry(self.root, width=35, show="*")
      self.password.pack(pady=(10, 10), ipady=5)

      login_button = Button(self.root, text= "Register", width=25, height=2,command=self.perf_registration)
      login_button.pack(pady=(40,15),ipady = 5)

      label3 = Label(self.root, text="Already a Member?")
      label3.pack(pady=(15, 15))

      redirect_button = Button(self.root, text="Login NOW:",command=self.login_gui)
      redirect_button.pack(pady=(10, 10))


  def clear(self):
      for i in self.root.pack_slaves():
          i.destroy()

  def perf_registration(self):
      name = self.name.get().strip()
      email = self.email.get().strip()
      password = self.password.get()

      if not name or not email or not password:
          messagebox.showerror("Error:", "All fields are required")
          return

      response = self.dbo.add_data(name, email, password)
      if response == 1:
          messagebox.showinfo("Success:", "Registration Successful")
          self.login_gui()
      else:
          messagebox.showerror("Error:", "Email Already Exists")

  def perf_login(self):
      email = self.email.get()
      password = self.password.get()
      response = self.dbo.search(email,password)
      if response == 1:
          messagebox.showinfo("Success:", "Login Successful")
          self.home_gui()
      else:
          messagebox.showerror("Error:","Incorrect Email/Password")

  def home_gui(self):
      self.clear()
      heading = Label(self.root,text ="Welcome to NLPApp", bg= "#757272", fg= "white")
      heading.pack(pady= (30,30))
      heading.configure(font=("verdana",25,"bold"))

      sentiment_button = Button(self.root, text= "Sentiment Analysis", width=25, height=2,command=self.sentiment_gui)
      sentiment_button.pack(pady=(15,15),ipady = 5)

      ner_button = Button(self.root, text= "Named Entity Recognition", width=25, height=2,command=self.ner_gui)
      ner_button.pack(pady=(15,15),ipady = 5)

      emotion_button = Button(self.root, text= "Emotion Prediction ", width=25, height=2,command=self.emotion_gui)
      emotion_button.pack(pady=(15,15),ipady = 5)

      logout_button = Button(self.root, text="Logout:",command=self.login_gui)
      logout_button.pack(pady=(10, 10))

  def sentiment_gui(self):
      self.clear()
      heading = Label(self.root, text="Welcome to NLPApp", bg="#757272", fg="white")
      heading.pack(pady=(30, 30))
      heading.configure(font=("verdana", 25, "bold"))

      heading4 = Label(self.root, text="Sentiment Analysis", bg="#757272", fg="black")
      heading4.pack(pady=(10, 15))
      heading4.configure(font=("verdana", 15, "bold"))

      label1 = Label(self.root,text= "Enter Text:",bg="#757272", fg="white" )
      label1.pack(pady=(10,10))
      self.sentiment_input = Entry(self.root, width=30)
      self.sentiment_input.pack(pady=(5,10),ipady= 5)

      sentiment_button = Button(self.root, text="Analise The Sentiment", width=25, height=2, command=self.do_sentiment)
      sentiment_button.pack(pady=(15, 15), ipady=5)
      self.sentiment_result = Label(self.root, text="", bg="#757272", fg="white")
      self.sentiment_result.pack(pady=(10, 10))
      self.sentiment_result.configure(font=('verdana',13,"bold"))

      goback_button = Button(self.root, text="Go Back ", width=25, height=2, command=self.home_gui)
      goback_button.pack(pady=(15, 15), ipady=5)

  def do_sentiment(self):
      text = self.sentiment_input.get().strip()
      result = self.apio.sentiment(text)
      print(result)
      self.sentiment_result['text'] = result


  def ner_gui(self):
      self.clear()
      heading = Label(self.root, text="Welcome to NLPApp", bg="#757272", fg="white")
      heading.pack(pady=(30, 30))
      heading.configure(font=("verdana", 25, "bold"))

      heading4 = Label(self.root, text="Named Entity Recognition", bg="#757272", fg="black")
      heading4.pack(pady=(10, 15))
      heading4.configure(font=("verdana", 15, "bold"))

      label1 = Label(self.root, text="Enter Text:", bg="#757272", fg="white")
      label1.pack(pady=(10, 10))
      self.ner_input = Entry(self.root, width=30)
      self.ner_input.pack(pady=(5, 10), ipady=5)

      ner_button = Button(self.root, text="Find Entities", width=25, height=2, command=self.do_ner)
      ner_button.pack(pady=(15, 15), ipady=5)
      self.ner_result = Label(self.root, text="", bg="#757272", fg="white")
      self.ner_result.pack(pady=(10, 10))
      self.ner_result.configure(font=('verdana', 13, "bold"))

      goback_button = Button(self.root, text="Go Back ", width=25, height=2, command=self.home_gui)
      goback_button.pack(pady=(15, 15), ipady=5)

  def do_ner(self):
      text = self.ner_input.get().strip()
      result = self.apio.ner(text)
      print(result)
      self.ner_result['text'] = result

  def emotion_gui(self):
      self.clear()
      heading = Label(self.root, text="Welcome to NLPApp", bg="#757272", fg="white")
      heading.pack(pady=(30, 30))
      heading.configure(font=("verdana", 25, "bold"))

      heading4 = Label(self.root, text="Emotion Prediction", bg="#757272", fg="black")
      heading4.pack(pady=(10, 15))
      heading4.configure(font=("verdana", 15, "bold"))

      label1 = Label(self.root, text="Enter Text:", bg="#757272", fg="white")
      label1.pack(pady=(10, 10))
      self.emotion_input = Entry(self.root, width=30)
      self.emotion_input.pack(pady=(5, 10), ipady=5)

      emotion_button = Button(self.root, text="Predict Emotion", width=25, height=2, command=self.do_emotion)
      emotion_button.pack(pady=(15, 15), ipady=5)
      self.emotion_result = Label(self.root, text="", bg="#757272", fg="white")
      self.emotion_result.pack(pady=(10, 10))
      self.emotion_result.configure(font=('verdana', 13, "bold"))

      goback_button = Button(self.root, text="Go Back ", width=25, height=2, command=self.home_gui)
      goback_button.pack(pady=(15, 15), ipady=5)

  def do_emotion(self):
      text = self.emotion_input.get().strip()
      result = self.apio.emotion(text)
      print(result)
      self.emotion_result['text'] = result






nlp = NLPAPP()