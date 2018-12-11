import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
conn = sqlite3.connect('flowers.db')
c = conn.cursor()



LARGE_FONT= ("Verdana", 12,)
mglobalvar = ''
insperson = ''
inslocation = '' 
insflowername = ''
inssighted = ''
updflower ='Alpine columbine'
updgenus = '' 
updspecies = ''
newupdflower = ''
flowername = 'cook'
def setFlowerName(strn):
    global flowername
    flowername = strn


container = ''
class FlowerStuff(tk.Tk):

    
    def __init__(self, *args, **kwargs):
        global container
        tk.Tk.__init__(self, *args, **kwargs)
        
        # tk.Tk.iconbitmap(self,default='clienticon.ico')
        tk.Tk.wm_title(self, "Flower Database Client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        tk.Tk.geometry(self, '1000x1000')
        

        self.loadFrames()

        self.show_frame(StartPage)

    def loadFrames(self):
        for F in (StartPage, PageOne, PageTwo, Query2, Insert2, Insert3, Insert4, PageThree):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    def loadUpdate2(self):
        frame = Update2(container, self)
        self.frames[Update2] = frame
        frame.grid(row=0, column=0, sticky="nsew")
    def loadInsert(self):
        frame = Insert5(container, self)
        self.frames[Insert5] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        
    def loadUpdate3(self):
        frame = Update3(container, self)
        self.frames[Update3] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def loadUpdate4(self):
        frame = Update4(container, self)
        self.frames[Update4] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def loadUpdate5(self):
        frame = Update5(container, self)
        self.frames[Update5] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        
        self.configure(background='#FFEEEA')
        label = Label(self, text="Start Page",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Query",
            command=lambda: myLambda(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Insert",
            command=lambda: myLambda(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Update",
            command=lambda: myLambda(PageThree))
        button3.pack()
        button4 = ttk. Button(self, text="Save Changes", 
            command=  conn.commit())
        button4.pack()
        def myLambda(page2show):
            
            
            app.loadFrames()
            controller.show_frame(page2show)
            


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        names = ''
        self.configure(background='#FFEEEA')
        label = Label(self, text="Please select a flower from the following list",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)

        self.query = StringVar()
        labelText = 'Please select a flower from the following list: \n'
        c.execute('SELECT DISTINCT NAME FROM SIGHTINGS')
        for row in c: 
            for member in row:
                 names += member + ', '
        Label(self, text=names, wraplength=500,fg='#9CC0EC',bg='#FFEEEA', font = ('fixedsys',15)).pack()
        Entry(self, textvariable=self.query).pack()
        # global flowername
        # flowername = self.query.get()
        button3 = ttk.Button(self, text="Submit",
                        command=lambda: myLambda(self.query.get()))
        button3.pack()
        

        def myLambda(strnaaa):
            global flowername
            flowername = strnaaa
            app.loadFrames()
            controller.show_frame(Query2)

    
class Query2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        label = Label(self, text="Flowers found",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        resultString = 'Last 10 sightings of ' + flowername + "\n\n"
        t = (flowername,)
        c.execute('SELECT * FROM  SIGHTINGS WHERE NAME = ? ORDER BY SIGHTED DESC LIMIT 10',t)
        rows = c.fetchall()
        for row in rows:
            resultString = resultString + row[3] + ': ' + row[1] + ', ' + row[2] + '\n'
        Label(self, text=resultString,fg='#9CC0EC',bg='#FFEEEA', font = ('fixedsys',15)).pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        label = Label(self, text="What flower was it?",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)
        self.query = StringVar()
        Entry(self, textvariable=self.query).pack()

        button3 = ttk.Button(self, text="Submit",
                            command=lambda: myLambda(self.query.get()))
        button3.pack()

        def myLambda(strnaaa):
                global insflowername
                insflowername = strnaaa
                app.loadFrames()
                controller.show_frame(Insert2)


class Insert2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        label = Label(self, text="Who saw it???",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)
        self.query = StringVar()
        Entry(self, textvariable=self.query).pack()

        button3 = ttk.Button(self, text="Submit",
                            command=lambda: myLambda(self.query.get()))
        button3.pack()

        def myLambda(strnaaa):
                global insperson
                insperson = strnaaa
                app.loadFrames()
                controller.show_frame(Insert3)



class Insert3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        label = Label(self, text="Insert the location the flower was spotted at",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)
        self.query = StringVar()
        Entry(self, textvariable=self.query).pack()

        button3 = ttk.Button(self, text="Submit",
                            command=lambda: myLambda(self.query.get()))
        button3.pack()

        def myLambda(strnaaa):
                global inslocation
                inslocation = strnaaa
                app.loadFrames()
                controller.show_frame(Insert4)

class Insert4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        label = Label(self, text="what date was it spotted?",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)
        self.query = StringVar()
        Entry(self, textvariable=self.query).pack()

        button3 = ttk.Button(self, text="Submit",
                            command=lambda: myLambda(self.query.get()))
        button3.pack()

        def myLambda(strnaaa):
                global inssighted
                inssighted = strnaaa
                app.loadInsert()
                controller.show_frame(Insert5)







class Insert5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        label = Label(self, text="Insert complete",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack()
        t = (insflowername,insperson,inslocation,inssighted)
        c.execute('INSERT INTO SIGHTINGS VALUES(?,?,?,?)',t)
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        names2 = ''
        self.configure(background='#FFEEEA')
        label = Label(self, text="Please select a flower from the following list",fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)

        self.query = StringVar()
        labelText = 'Please select a flower from the following list: \n'
        c.execute('SELECT DISTINCT NAME FROM SIGHTINGS')
        for row in c: 
            for member in row:
                names2 += member + ', '
        Label(self, text=names2, wraplength=500,fg='#9CC0EC',bg='#FFEEEA', font = ('fixedsys',15)).pack()
        Entry(self, textvariable=self.query).pack()

        button3 = ttk.Button(self, text="Submit",
                        command=lambda: myLambda(self.query.get()))
        button3.pack()

        def myLambda(strnaaa):
            global updflower
            updflower = strnaaa
            app.loadUpdate2()
            controller.show_frame(Update2)

class Update2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        labelText = 'The current GENUS of ' + updflower + ' is '
        t = (updflower,)
        c.execute('SELECT * FROM FLOWERS WHERE COMNAME = ?',t)
        r = c.fetchone()
        labelText = labelText + r[0] + '.\nWhat would you like the new GENUS to be?'
        label = Label(self, text=labelText,fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)

        self.query = StringVar()
        Entry(self, textvariable=self.query).pack()

        button3 = ttk.Button(self, text="Submit",
                        command=lambda: myLambda(self.query.get()))
        button3.pack()

        def myLambda(strnaaa):
            global updgenus
            updgenus = strnaaa
            app.loadUpdate3()
            controller.show_frame(Update3)

class Update3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        flowername = updflower
        t = (updgenus,flowername)
        c.execute('UPDATE FLOWERS SET GENUS = ? WHERE COMNAME = ?',t)
        labelText = 'The current SPECIES of ' + flowername + ' is '
        t = (flowername,)
        c.execute('SELECT * FROM FLOWERS WHERE COMNAME = ?',t)
        r = c.fetchone()
        labelText = labelText + r[1] + '.\nWhat would you like the new SPECIES to be?'
        label = Label(self, text=labelText,fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))
        label.pack(pady=10,padx=10)
        
        self.query = StringVar()
        Entry(self, textvariable=self.query).pack()
        button3 = ttk.Button(self, text="Submit",  command=lambda: myLambda(self.query.get()))
        button3.pack()

        def myLambda(strnaaa):
            global updspecies
            updspecies = strnaaa
            app.loadUpdate4()
            controller.show_frame(Update4)


class Update4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        updflower
        self.configure(background='#FFEEEA')
        flowername = updflower
        t = (updspecies,flowername)
        c.execute('UPDATE FLOWERS SET SPECIES = ? WHERE COMNAME = ?',t)
        labelText = 'What would you like the new name of ' + flowername + ' to be?'
        label = Label(self, text=labelText,fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))    
        label.pack()    
        
        self.query = StringVar()
        Entry(self, textvariable=self.query).pack()
        button3 = ttk.Button(self, text="Submit",
                        command=lambda: myLambda(self.query.get()))
        button3.pack()


        def myLambda(strnaaa):
            global newupdflower
            newupdflower = strnaaa
            app.loadUpdate5()
            controller.show_frame(Update5)


class Update5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#FFEEEA')
        t = (newupdflower,updflower)
        c.execute('UPDATE FLOWERS SET COMNAME = ? WHERE COMNAME = ?',t)
        c.execute('UPDATE SIGHTINGS SET NAME = ? WHERE NAME = ?',t)
        label = Label(self, text='update complete',fg='#EC8282',bg='#FFEEEA',font = ('fixedsys',15))    
        label.pack()
        
        button1 = ttk.Button(self, text="Back to Home",
            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        def myLambda(strnaaa):
            
            app.loadFrames()
            controller.show_frame(StartPage)

app = FlowerStuff()

app.mainloop()