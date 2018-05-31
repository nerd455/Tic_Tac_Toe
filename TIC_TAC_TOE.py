import tkinter

ans=[0,0,0,0,0,0,0,0,0,0]
global turn
turn=0
#############################################################################################################################

def typ_x_b1(event):
    
    if ans[1]==0:
         b1['text']='X'
         b1['bg']='white'
         b1['fg']='black'
         global turn         
         turn+=1
         ans[1]='x'
    print(ans)
    print(turn)
    
def typ_x_b2(event):
    
    
    if ans[2]==0:
        b2['text']='X'
        b2['bg']='white'
        b2['fg']='black'
        global turn
        turn+=1
        ans[2]='x'
    print(ans)
    print(turn)
    
def typ_x_b3(event):

    if ans[3]==0:
         b3['text']='X'
         b3['bg']='white'
         b3['fg']='black'
         global turn
         turn+=1
         ans[3]='x'
    print(ans)
    print(turn)

def typ_x_b4(event):
   
    if ans[4]==0:
         b4['text']='X'
         b4['bg']='white'
         b4['fg']='black'
         global turn 
         turn+=1
         ans[4]='x'
    print(ans)
    print(turn)
    
def typ_x_b5(event):
    
    if ans[5]==0:
        b5['text']='X'
        b5['bg']='white'
        b5['fg']='black'
        global turn 
        turn+=1
        ans[5]='x'
    print(ans)
    print(turn)
    
def typ_x_b6(event):
    
    if ans[6]==0:
        b6['text']='X'
        b6['bg']='white'
        b6['fg']='black'
        global turn 
        turn+=1
        ans[6]='x'
    print(ans)
    print(turn)
    
def typ_x_b7(event):
    
    if ans[7]==0:
        b7['text']='X'
        b7['bg']='white'
        b7['fg']='black'
        global turn 
        turn+=1
        ans[7]='x'
    print(ans)
    print(turn)
    
def typ_x_b8(event):
    
    if ans[8]==0:
        b8['text']='X'
        b8['bg']='white'
        b8['fg']='black'
        global turn    
        turn+=1
        ans[8]='x'
    print(ans)
    print(turn)
    
def typ_x_b9(event):
   
    if ans[9]==0:
        b9['text']='X'
        b9['bg']='white'
        b9['fg']='black'
        global turn
        turn+=1
        ans[9]='x'
    print(ans)
    print(turn)
    
####################################################################################################################   
   
def typ_o_b1(event):
    
    if ans[1]==0:
        b1['text']='O'
        b1['bg']='white'
        b1['fg']='black'
        global turn
        turn+=1
        ans[1]='o'
    print(ans)
    print(turn)
    
def typ_o_b2(event):
    
    if ans[2]==0:
        b2['text']='O'
        b2['bg']='white'
        b2['fg']='black'
        global turn
        turn+=1
        ans[2]='o'
    print(ans)
    print(turn)
    
def typ_o_b3(event):
    
    if ans[3]==0:
        b3['text']='O'
        b3['bg']='white'
        b3['fg']='black'
        global turn 
        turn+=1
        ans[3]='o'
    print(ans)
    print(turn)

def typ_o_b4(event):
    
    if ans[4]==0:
        b4['text']='O'
        b4['bg']='white'
        b4['fg']='black'
        global turn 
        turn+=1
        ans[4]='o'
    print(ans)
    print(turn)
    
def typ_o_b5(event):
    
    if ans[5]==0:
        b5['text']='O'
        b5['bg']='white'
        b5['fg']='black'
        global turn
        turn+=1
        ans[5]='o'
    print(ans)
    print(turn)
    
def typ_o_b6(event):
    
    if ans[6]==0:
        b6['text']='O'
        b6['bg']='white'
        b6['fg']='black'
        global turn 
        turn+=1
        ans[6]='o'
    print(ans)
    print(turn)
    
def typ_o_b7(event):
    
    if ans[7]==0:
        b7['text']='O'
        b7['bg']='white'
        b7['fg']='black'
        global turn 
        turn+=1
        ans[7]='o'
    print(ans)
    print(turn)
    
def typ_o_b8(event):
    
    if ans[8]==0:
        b8['text']='O'
        b8['bg']='white'
        b8['fg']='black'
        global turn 
        turn+=1
        ans[8]='o'
    print(ans)
    print(turn)
    
def typ_o_b9(event):
    
    if ans[9]==0:
        b9['text']='O'
        b9['bg']='white'
        b9['fg']='black'
        global turn 
        turn+=1
        ans[9]='o'
    print(ans)
    print(turn)
    
def result(event):
    if ans[1]=='x' and ans[2]=='x' and ans[3]=='x':
            la['text']='HURRAH! MR.X ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[4]=='x' and ans[5]=='x' and ans[6]=='x':
            la['text']='HURRAH! MR.X ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[7]=='x' and ans[8]=='x' and ans[9]=='x':
            la['text']='HURRAH! MR.X ...WON\nYou can PLAY ANYTIME YOU WANT'
            
        
    elif ans[1]=='x' and ans[4]=='x' and ans[7]=='x':
            la['text']='HURRAH! MR.X ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[2]=='x' and ans[5]=='x' and ans[8]=='x':
            la['text']='HURRAH! MR.X ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[3]=='x' and ans[6]=='x' and ans[9]=='x':
            la['text']='HURRAH! MR.X ...WON\nYou can PLAY ANYTIME YOU WANT' 
            
        
    elif ans[1]=='x' and ans[5]=='x' and ans[9]=='x':
            la['text']='HURRAH! MR.X ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[3]=='x' and ans[5]=='x' and ans[7]=='x':
            la['text']='HURRAH! MR.X ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    
    
    elif ans[1]=='o' and ans[2]=='o' and ans[3]=='o':
            la['text']='HURRAH! MR.O ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[4]=='o' and ans[5]=='o' and ans[6]=='o':
            la['text']='HURRAH! MR.O ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[7]=='o' and ans[8]=='o' and ans[9]=='o':
            la['text']='HURRAH! MR.O ...WON\nYou can PLAY ANYTIME YOU WANT'
            
        
    elif ans[1]=='o' and ans[4]=='o' and ans[7]=='o':
            la['text']='HURRAH! MR.O ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[2]=='o' and ans[5]=='o' and ans[8]=='o':
            la['text']='HURRAH! MR.O ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[3]=='o' and ans[6]=='o' and ans[9]=='o':
            la['text']='HURRAH! MR.O ...WON\nYou can PLAY ANYTIME YOU WANT'
            
        
    elif ans[1]=='o' and ans[5]=='o' and ans[9]=='o':
            la['text']='HURRAH! MR.O ...WON\nYou can PLAY ANYTIME YOU WANT'
            
    elif ans[3]=='o' and ans[5]=='o' and ans[7]=='o':
            la['text']='HURRAH! MR.O ...WON\nYou can PLAY ANYTIME YOU WANT'


    else:
        la['text']='FUCK YOU BOTH.....NO ONE WON\nYou can PLAY ANYTIME YOU WANT'

#################################################################################################################### 

root=tkinter.Tk()
root.title('TIC_TAC_TOE')

la=tkinter.Label(root,text='Mr.X use LEFT_CLICK\nMR.O use RIGHT_CLICK',font='Ariel 16 bold')
f=tkinter.Frame(root)

b1=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')
b2=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')
b3=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')

b4=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')
b5=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')
b6=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')

b7=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')
b8=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')
b9=tkinter.Button(f,bg='black',fg='white',width=6,height=5,bd=5,font='Ariel  ',text='Click\nMe')

lab_result=tkinter.Button(root,text='Once Finished Click Me!!!!',bd=5,bg='white',fg='black',font='Ariel 16 bold')

la.pack(side='top',pady=5)
f.pack(side='top')

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

lab_result.pack(padx=5)

b1.bind('<Button-1>',typ_x_b1)
b2.bind('<Button-1>',typ_x_b2)
b3.bind('<Button-1>',typ_x_b3)
b4.bind('<Button-1>',typ_x_b4)
b5.bind('<Button-1>',typ_x_b5)
b6.bind('<Button-1>',typ_x_b6)
b7.bind('<Button-1>',typ_x_b7)
b8.bind('<Button-1>',typ_x_b8)
b9.bind('<Button-1>',typ_x_b9)
 
b1.bind('<Button-3>',typ_o_b1)
b2.bind('<Button-3>',typ_o_b2)
b3.bind('<Button-3>',typ_o_b3)
b4.bind('<Button-3>',typ_o_b4)
b5.bind('<Button-3>',typ_o_b5)
b6.bind('<Button-3>',typ_o_b6)
b7.bind('<Button-3>',typ_o_b7)
b8.bind('<Button-3>',typ_o_b8)
b9.bind('<Button-3>',typ_o_b9)

lab_result.bind('<Button-1>',result)
lab_result.bind('<Button-3>',result)

root.mainloop()