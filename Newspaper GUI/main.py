#NEWSPAPER GUI
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime

newspaper = Tk()
newspaper.title("Newspaper GUI")
newspaper.config(bg="White")
newspaper.geometry('1600x800')

headline_label = Label(text='''THE PATHAK'S NEWS''',font='''Verdana 50 bold underline''',bg="White")
headline_label.pack(fill=X)

datetimeheadline_label = Label(text='''Date,Time: ''',font='''Times 15 bold''',bg='''White''')
datetimeheadline_label.place(x=370,y=100)

date_label = Label(text=f'''{datetime.now()}''',font='''Helvetica 18 underline''',bg="White")
date_label.place(x=370,y=125)

trending_label = Label(text='''Trending''',font='''Verdana 20 bold''')
trending_label.place(x=90,y=135,width=180)

free_label = Label(text='''Free Daily News!''',font='''Verdana 20 italic''',bg='''Red''',fg='''Yellow''',relief=RIDGE)
free_label.place(x=60,y=20)

latestnews_label = Label(text='''Latest News''',font='''Verdana 25 bold''',bg='''White''')
latestnews_label.place(x=60,y=70)

adver_label = Label(text='''Advertisement 
Corner''',font='''Roman 20 bold''')
adver_label.place(x=1275,y=20,width=200)

image11 = Image.open('''image11.jpg''')
photo11 = ImageTk.PhotoImage(image11)
trendphoto_label = Label(image=photo11)
trendphoto_label.place(x=20,y=200)

trend_label = Label(text='''"Magnificent but fragile: 
For Cheetahs at Kuno, 
expert list worries.''',font='''Verdana 10 bold''',bg='''White''')
trend_label.place(x=140,y=200)

line1_label = Label(text='''---------------------------------------------------------------''',bg='''White''')
line1_label.place(x=20,y=270)

image12 = Image.open('''image12.jpg''')
photo12 = ImageTk.PhotoImage(image12)
trendphoto2_label = Label(image=photo12)
trendphoto2_label.place(x=20,y=300)

trend2_label = Label(text='''Video: Queen grandchildren 
stands vigil,prince harry in 
military attire.''',font='''Verdana 10 bold''',background='''White''')
trend2_label.place(x=130,y=300)

line2_label = Label(text='''---------------------------------------------------------------''',bg='''White''')
line2_label.place(x=20,y=380)

image13 = Image.open('''image13.jpg''')
photo13 = ImageTk.PhotoImage(image13)
trendphoto3_label = Label(image=photo13)
trendphoto3_label.place(x=20,y=410)

trend3_label = Label(text='''Mumbai teacher gets
stuck in moving 
lift doors at 
school,dies.''',font='''Verdana 10 bold''',bg='''White''')
trend3_label.place(x=140,y=410)

line3_label = Label(text='''---------------------------------------------------------------''',bg='''White''')
line3_label.place(x=20,y=490)

image4 = Image.open('''image14.jpg''')
photo4 = ImageTk.PhotoImage(image4)
trendphoto4_label = Label(image=photo4)
trendphoto4_label.place(x=20,y=515)

trend4_label = Label(text='''BEAUTY:
Ananya Pandey 
Italian summer 
beauty.''',font='''Verdana 10 bold''',bg='''White''')
trend4_label.place(x=140,y=520)

line5_label = Label(text='''---------------------------------------------------------------''',bg='''White''')
line5_label.place(x=20,y=630)

image5 = Image.open('''image15.jpg''')
photo5 = ImageTk.PhotoImage(image5)
trendphoto5_label = Label(image=photo5)
trendphoto5_label.place(x=20,y=650)

trend5_label = Label(text='''FOOD:\n7-Best diabaetic recipies \nfor you.''',font='''Verdana 10 bold''',bg='''White''')
trend5_label.place(x=140,y=670)

adver1 = Image.open('''adver.jpg''')
photoadver = ImageTk.PhotoImage(adver1)
adver_label = Label(image=photoadver)
adver_label.place(x=1250,y=110)

adver2 = Image.open('''adver2.jpg''')
photoadver2 = ImageTk.PhotoImage(adver2)
adver2_label = Label(image=photoadver2)
adver2_label.place(x=1250,y=450)

newsimage1 = Image.open('''image1.jpg''')
photonews1 = ImageTk.PhotoImage(newsimage1)
news1photo_label = Label(image=photonews1)
news1photo_label.place(x=370,y=175)

news1hl_label = Label(text='''"Don't start this nonsense": India great Gautam\nGambhir on changing Virat Kohli's batting position.''',font='''Verdana 15 bold''',bg='''White''',relief=RIDGE)
news1hl_label.place(x=590,y=177)

date1_label = Label(text='''Sunday September 18,2022''',font='''Verdana 10 italic''',bg='''White''',fg='''Grey''')
date1_label.place(x=588,y=235)

news1_label = Label(text='''Kohli's ton against Afghanistan came while he was opening the batting
for India. This has led many to ponder whether Kohli, who generally
bats at No. 3 in T20Is, can be used as an opener.''',font='''Verdana 12''',bg='''White''',fg='''Grey''')
news1_label.place(x=588,y=260)

newsimage2 = Image.open('''image4.jpg''')
photonews2 = ImageTk.PhotoImage(newsimage2)
news2photo_label = Label(image=photonews2)
news2photo_label.place(x=370,y=375)

news2hl_label = Label(text='''Japan issues rare 'Special Warning' ahead of
powerful typhoon.''',font='''Verdana 15 bold''',bg='''White''',relief=RIDGE)
news2hl_label.place(x=590,y=376,width=585)

date2_label = Label(text='''Sunday September 18,2022''',font='''Verdana 10 italic''',bg='''White''',fg='''Grey''')
date2_label.place(x=588,y=435)

news2_label = Label(text='''Thousands of people were in shelters in southwestern Japan on Sunday
as powerful Typhoon Nanmadol churned towards the region, prompting 
authorities to urge nearly three million residents to evacuate.''',font='''Verdana 12''',bg='''White''',fg='''Grey''')
news2_label.place(x=588,y=460)

newsimage3 = Image.open('''image7.jpg''')
photonews3 = ImageTk.PhotoImage(newsimage3)
news3photo_label= Label(image=photonews3)
news3photo_label.place(x=370,y=570)

news3hl_label = Label(text='''Chabahar port development to boost India-Iran 
relations: Iran president.''',font='''Verdana 15 bold''',bg='''White''',relief=RIDGE)
news3hl_label.place(x=590,y=571,width=585)

date3_label = Label(text='''Sunday September 18,2022''',font='''Verdana 10 italic''',bg='''White''',fg='''Grey''')
date3_label.place(x=588,y=630)

news3_label = Label(text='''Terming the relations between India and Iran as "friendly and cordial",
Iranian President Ebrahim Raisi said the Chabahar-Central Asia transit
route can help both nations strengthen the grounds for cooperation.''',font='''Verdana 12''',bg='''White''',fg='''Grey''')
news3_label.place(x=588,y=650)





newspaper.mainloop()