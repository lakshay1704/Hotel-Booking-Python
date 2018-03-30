import pickle
import os
import time
import random

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class airplane:                                             #class for airplane booking
    def __init__(self):
        self.first_name=''
        self.last_name=''
        self.age=0
        self.gender=''
        self.Class=''
        self.destination=''
        self.origin=''
        self.charges=0
        self.code=0
    def inputdata_a(self):                                  #inputs data for airplane ticket
        print'**********************'
        print 'please wait -->'
        print '*********************'
        time.sleep(1)
        self.first_name=raw_input('Please enter your first name -->')
        self.last_name=raw_input('Please enter your last name -->')
        self.age=input('Please enter your age -->')
        self.gender=raw_input('Please enter M for MALE  and F for Female -->')
        self.Class=raw_input('Please enter the class you want to travel in B for Buisness and E for Economy -->')
        self.origin=raw_input('Please enter your origin -->')
        self.destintion=raw_input('Please enter you destination place *mumbai,chennai,kolkata,banglore,dubai,newyork,california,vancouver,toronto,london,paris*')
        airplane.display_data_a(self)
    def display_data_a(self):                                   #to display the tickets booked
        print '***************************'
        print '**Your tickets are booked**'
        airplane.code_generator(self)                       #calling code generator function
        airplane.calc_charges_a(self)                           #calling to calculate charges
        
    def details_a(self):                                        #function called when to display all records and every thing
        print '***************************'
        print 'Here are the details'
        print '***************************'
        time.sleep(2)
        print 'First Name-->',self.first_name
        print 'last name-->',self.last_name
        print 'age of the person-->',self.age
        print 'gender-->',self.gender
        print 'class of the seat-->',self.Class
        print 'Origin place of the flight-->',self.origin
        print'Destination place of the flight-->',self.destination
             
        print 'code of the ticket-->',self.code
        print 'charges applied on the ticket',self.charges
    def calc_charges_a(self):                                   #function to calculate ticket charges
        
        ec={'mumbai':1000,'chennai':1500,'kolkata':1200,'banglore':1350,'dubai':4000,'newyork':6500,'california':6400,'vancouver':6550,'toronto':6700,'london':5500,'paris':5200}
        bc={'mumbai':2000,'chennai':2500,'kolkata':2200,'banglore':2350,'dubai':5000,'newyork':7500,'california':7400,'vancouver':7550,'toronto':7700,'london':6500,'paris':6200}
        if self.Class in ('b','B'):                                                                             #prices of tickets stored in a dictionary
            if bc.has_key(self.destination):                                                                #ec dictionary for economy class
                self.charges=bc.get(self.destination)+0.05*(bc.get(self.destination))               #bc dictionary for buisness classes
                print 'Charges after tax-->',self.charges
            else:
                self.charges=4250+4250*0.05
                print 'Charges after tax-->',self.charges
        if self.Class in ('e','E'):
            if ec.has_key(self.destination):
                self.charges=ec.get(self.destination)+0.1*(ec.get(self.destination))
                print 'Charges after tax-->',self.charges
            else:
                self.charges=5250+5250*0.1
                print 'Charges after tax-->',self.charges
    def code_generator(self):                                                           #code generator function random
        l=['gYtpe4NB','OsOgGTjh','nEfneEJM','bQgLkKyM','mbdGg3rW','pg8j4wNg','AM2bLUBS','H3der9ez']
        self.code=random.choice(l)
        print 'Your ticket Code for the journey is','<<',self.code,'>>'
        print '------------------------------------------------'
    def update_a(self):                                                             #function to update records
        self.first_name=raw_input('Please enter your first name -->')
        self.last_name=raw_input('Please enter your last name -->')
        self.age=input('Please enter your age -->')
        self.gender=raw_input('Please enter M for MALE  and F for Female -->')
        self.Class=raw_input('Please enter the class you want to travel in B for Buisness and E for Economy -->')
        self.origin=raw_input('Please enter your origin -->')
        self.destintion=raw_input('Please enter you destination place *mumbai,chennai,kolkata,banglore,dubai,newyork,california,vancouver,toronto,london,paris*')
        airplane.code_generator(self)
        airplane.calc_charges_a(self)
        
        
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def add_a():                                                  #function calling the input data function of the class
    a=airplane()
    a.inputdata_a()
    myfile=file('airplane.txt','ab')
    pickle.dump(a,myfile)
    myfile.close()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def show_a():                                             #function calling the display function of the class
    try:
        a=airplane()                                                   
        myfile=file('airplane.txt','rb')
        while True:
            a=pickle.load(myfile)       
            a.details_a()
    except EOFError:
        myfile.close()
        return
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def search_a():                               #function to search the data of the desired function
    try:
        a=airplane()
        myfile=file('airplane.txt','rb')
        name=raw_input('Please enter the name of the person')
        while True:
            a=pickle.load(myfile)                
            if a.first_name==name:
                a.details_a()
        myfile.close() 
    except EOFError:
        myfile.close()
        return
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def edit_a():                           #function to edit the records
    try:
        a=airplane()
        myfile=file('airplane.txt','rb')
        myfile1=file('temp.txt','wb')
        name=raw_input('Please enter the name on the ticket-->')
        while True:
            a=pickle.load(myfile)
            if a.first_name==name:
                a.update_a()
            pickle.dump(a,myfile1)
        myfile.close()
        myfile1.close()
    except EOFError:
        myfile.close()
        myfile1.close()
        os.remove('airplane.txt')
        os.rename('temp.txt','airplane.txt')
        return
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    
def remove_a():                             #function to remove records
    try:
        a=airplane()
        myfile=file('airplane.txt','rb')
        myfile1=file('temp.txt','wb')
        name=raw_input('Please enter the name on the ticket')
        while True:
            a=pickle.load(myfile)
            if a.first_name!=name:
                pickle.dump(a,myfile1)
        myfile.close()
        myfile1.close()
    except EOFError:
        myfile.close()
        myfile1.close()
        os.remove('airplane.txt')
        os.rename('temp.txt','airplane.txt')
        return


class hoteldata:
    
    def __init__(self):
        self.first_name=''
        self.last_name=''
        self.email=''
        self.arrival_date=''
        self.depature_date=''
        self.cost=0
        self.cab=''
        self.room_type=''
        self.cab_cost=0
        self.rooms=''
    def inputdata(self):                                                                        #to input the details of the room holder
        print '----------------------'
        print 'Please wait-->'
        print '-----------------------'
        time.sleep(2)
        self.first_name=raw_input('Please enter your first name-->')
        self.last_name=raw_input('Please enter your last name-->')
        self.email=raw_input('Please enter your email ID-->')
        self.room_type=raw_input('Please enter room type delux or normal')
        hoteldata.display_room(self)                                    #calling function to display the details of the room types
        self.arrival_date=raw_input('Please enter your arrival date__(dd/mm/yy)-->')
        self.departure_date=raw_input('Please enter your depature date__(dd/mm/yy)-->')
        self.room_num=input('Enter the number of rooms wanted')
        self.cab=raw_input('Please enter yes to avail pickup (Rs. 5 per KM)')
        
        if self.cab=='yes':
            hoteldata.cab(self)                                     #calling cab function details for cab
        else:pass
        
        hoteldata.calc_charges(self)
        hoteldata.display(self)                     # to display the rooms are booked
    def display(self):
        print '--------------------------------'
        print '**Please wait**'
        print '-------------------------------'
        time.sleep(2)
        print '**rooms booked**'
        print 'Room booked on the name-->',self.first_name
        print 'Arrival Date-->',self.arrival_date
        print 'departure Date-->',self.departure_date
        print 'number of rooms-->',self.room_num
        print 'cab-->',self.cab
        hoteldata.rooms(self)
        hoteldata.total_cost(self)                              #calling total cost 
    def rooms(self):
        l=[]
        j=101
        for i in range(self.room_num):
            l.append(j+1)                                                       #alloting rooms
            j+=1
        self.rooms=str(l)
        print 'rooms-->',self.rooms 
    def display_room(self):
        if self.room_type in ('delux','Delux'):
            print '*************************************'
            print 'in delux room you get the following things absolutely Free-->'
            print '------> FREE!!! wifi'                                                                #displaying information about room type
            print '-------->FREE!!! membership of gymnasium'
            print '--------->FREE!!! access to swimming pool'
            print '---------->FREE!!! breakfast for two days'
            print '-------------------------------------------------'
        if self.room_type in ('normal','Normal'):
            print '-----------------------------------------------'
            print'FREE !!! wifi'
            print 'FREE !!! breakfast for two days'
            print '-----------------------------------------------'
        else:
            pass
        
    def details(self):                                                         #to display the details of the person
        print '------------------------------------------'
        print 'here are the details<--->'
        print '------------------------------------------'
        time.sleep(2)
        print 'first_name-->',self.first_name
        print 'last name-->',self.last_name
        print 'email ID-->',self.email
        print 'arrival date-->',self.arrival_date
        print 'departure date-->',self.departure_date
        print 'number of rooms booked-->',self.room_num
        print 'rooms alloted-->',self.rooms
        print 'pickup service',self.cab
        print '----------------------------------------------'
       
        hoteldata.total_cost(self)
    def total_cost(self):                                                   #calculating total cost
        print '------------------------'
        print 'total cost -->',self.cost+self.cab_cost
        print '------------------------'
    def calc_charges(self):                                     #calculating charges
        if self.room_type in ('delux','Delux'):
            self.cost=self.room_num*4570
            print '----------------------------------------------'
            print ' room charges  applied-->',self.cost
            print '----------------------------------------------'
        if self.room_type in ('normal','Normal'):
            self.cost=self.room_num*3499
            print '----------------------------------------------'
            print 'room charges applied-->',self.cost
            print '----------------------------------------------'
    def update(self):                                                           #to edit any data of the person
        self.email=raw_input('Please enter your new email ID')
        self.arrival_date=raw_input('Please enter your new arrival date__(dd/mm/yy)')
        self.departure_date=raw_input('Please  enter your departure date__(dd/mm/yy)')
    def cab(self):
        print '-----------------------------------------------'                                         #entering details for the cab
        print 'please wait-->'
        print '-----------------------------------------------'
        time.sleep(2)
        self.arrival_time=raw_input('Please enter your arrival time(hh:mm)')
        self.pickup_site=raw_input('Enter your pickup site')
        self.km=input('Distance from the hotel (km)')
        self.cab_cost=5*self.km
        print '------------------------------------------------'
        print 'cab cost -->',self.cab_cost
        print '------------------------------------------------'
        
    def cab_cost(self):
        print 'cab cost-->',self.cab_cost
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def add():                                                  #function calling the input data function of the class
    h=hoteldata()
    h.inputdata()
    myfile=file('hoteldata.txt','ab')
    pickle.dump(h,myfile)
    myfile.close()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def show():                                             #function calling the display function of the class
    try:
        h=hoteldata()                                                   
        myfile=file('hoteldata.txt','rb')
        while True:
            h=pickle.load(myfile)             
            h.details()
    except EOFError:
        myfile.close()
        return
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def search():                               #function to search the data of the desired function
    try:
        h=hoteldata()
        myfile=file('hoteldata.txt','rb')
        name=raw_input('Please enter the name of the person')
        while True:
            h=pickle.load(myfile)             
            if h.first_name==name:
                h.details()
        myfile.close() 
    except EOFError:
        myfile.close()
        return
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def edit():     #function to edit the details of the person room holder
    try:
        h=hoteldata()
        myfile=file('hoteldata.txt','rb')
        myfile1=file('temp.txt','wb')
        name=raw_input('Please enter the name of the room holder-->')
        while True:
            h=pickle.load(myfile)
            if h.first_name==name:
                h.update()
            pickle.dump(h,myfile1)
        myfile.close()
        myfile1.close()
    except EOFError:
        myfile.close()
        myfile1.close()
        os.remove('hoteldata.txt')
        os.rename('temp.txt','hoteldata.txt')
        return
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    
def remove():                                       #to delete the records of the room holder
    try:
        h=hoteldata()
        myfile=file('hoteldata.txt','rb')
        myfile1=file('temp.txt','wb')
        name=raw_input('Please enter the name of the room holder')
        while True:
            h=pickle.load(myfile)
            if h.first_name!=name:
                pickle.dump(h,myfile1)
        myfile.close()
        myfile1.close()
    except EOFError:
        myfile.close()
        myfile1.close()
        os.remove('hoteldata.txt')
        os.rename('temp.txt','hoteldata.txt')
        return
    
#MAIN PROGRAM            

print '           ________________WELCOME TO THE BEST  AIRLINE AND HOTEL BOOKING PORTAL____________________'
print 'Get the best hotel at the lowest price for just Rs. 3499 per night'
print 'Get the best flying experience'
print '---------------------------------------------------------------------------------'

print '---------------------------------------------------------------------------------'
def main1():
    while True:
        print 'Please wait'
        time.sleep(2)
        print 'press 1 to book a hotel room'
        print '-----'
        print 'press 2 to display the data'
        print '-----'
        print 'press 3 to display a specific data'
        print '-----'
        print 'press 4 to edit the records'
        print '-----'                                                                                   #function calling hotelclass
        print 'press 5 to delete specific data'
        print '-----'
        print 'press 0 to exit'
        n=input('enter your choice to proceed')
        if n==1:
            add()
        elif n==2:
            show()
        elif n==3:
            search()
        elif n==4:
            edit()
        elif n==5:
            remove()
        elif n==0:
            print 'Thankyou for giving us the opportunity'
            return
        else:
            pass
            
    
        
def main2():
    while True:
        print 'Please wait'                                                                 #function calling the airplane class
        time.sleep(2)
        print 'press 1 to book a airline ticket'
        print '-----'
        print 'press 2 to display  all the details'
        print '-----'
        print 'press 3 to display specific records'
        print '-----'
        print 'press 4 to edit the details'
        print '-----'
        print 'press 5 to to cancel the flight'
        print '-----'
        print 'press 0 to exit'
        n=input('enter your choice to proceed')
        if n==1:
            add_a()
        elif n==2:
            show_a()
        elif n==3:
            search_a()
        elif n==4:
            edit_a()
        elif n==5:
            remove_a()
        elif n==0:
            print 'Thankyou for giving us the opportunity'
            return
        else:
            pass

def reset():                                                        #function to reset the database
    admin=raw_input('Enter administartor name-->')
    admin_pass=raw_input('Enter administrator password-->')
    if admin=='Lakshay':
        if admin_pass=='Bhatia':
            print 'resetting...'
            time.sleep(3)
            os.remove('airplane.txt')
            os.remove('hotel_data.txt')
            print 'reset successful'
    else:
        print 'Wrong username or password'

def main():                             #function to call for hotel or airline booking or reset or exit
    while True:
        ah=raw_input('Enter A to book an AIRPLANE or H to book a HOTEL or R to RESET DATABASE or E to EXIT')
        if ah in('A' ,'a'):
            main2()
        if ah in ('H' , 'h'):
            main1()
        if ah in ('R','r'):
            reset()
        if ah in ('e' , 'E'):
            print'Thanks for coming'
            break
        


def login():                                                #for login asking uname and password
    d={'Lakshay':'Bhatia'}
    print 'PLEASE ENTER THE USERNAME AND PASSWORD TO CONTINUE'
    uname=raw_input('Enter your username-->')
    password=raw_input('Enter password for the same-->')
    if d.has_key(uname):
        p=d.get(uname)
        if p==password:
            main()
    else:
        print '**I think you entered a wrong username or password**'
        return
login()
