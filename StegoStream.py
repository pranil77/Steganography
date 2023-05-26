import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import Image,ImageTk
import os
from tkinter import filedialog
import PyPDF2
from fpdf import FPDF
import textwrap
from stegano import lsb
import cv2
import numpy as np
from tkinter import font








def pdfextract():
    hello=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PDF file","*.pdf"),("PDF File","*.pdf")))
    a = PyPDF2.PdfFileReader(hello)
    global extracted_text
    extracted_text=""
    for i in range(0,5):
        extracted_text +=a.getPage(i).extractText()
    print(extracted_text)
    text1.insert(END,extracted_text)




def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)


        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')


def createPdf():
    kroot = tk.Tk()
    kroot.title("Video Encryption :")

    pdfname = tk.Label(kroot, text="Enter the new PDF name :")
    pdfname.pack()

    pdfname= tk.Entry(kroot)
    pdfname.pack()

    def take_input2():
        global PDFname
        PDFname=pdfname.get()
        kroot.destroy()        
        output_filename = PDFname
        #file = open(input_filename)
        text11 = lsb.reveal(filename)
        text_to_pdf(text11,output_filename)
        SAVED=Label(root,text="PDF SUCCESSFULLY SAVED",bg="green",font="arial")
        SAVED.place(x=190,y=60,width=440,height=20)
        

    
    save_button = tk.Button(kroot, text="Save", command=take_input2)
    save_button.pack()
    kroot.mainloop()


def Wordextract():
    import docx2txt
    sss = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("Word file","*.docx"),("Word file","*.doc"),("All Files","*.doc")))
    dcc=docx2txt.process(sss)
    print(dcc)
    text1.insert(END,dcc)


def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG file","*.png"),("JPG file","*.jpg")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=440,height=345)
    lbl.image=img
    imgname=Label(root,text=filename,bg="red",font="arial")
    imgname.place(x=190,y=60,width=440,height=20)



def hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)



def show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)


def save():
        secret.save("hidden.png")


def input_video_parameters():
    root = tk.Tk()
    root.title("Video Encryption :")

    frame_no_label = tk.Label(root, text="Enter the frame number where you want to embed data :")
    frame_no_label.pack()

    frame_no_entry = tk.Entry(root)
    frame_no_entry.pack()


    # Create the key label and entry widget
    key_label = tk.Label(root, text="Enter key:")
    key_label.pack()

    key_entry = tk.Entry(root)
    key_entry.pack()


    def take_input():
        global frame_no ,message,key_1
        frame_no = frame_no_entry.get()
        message=text1.get(1.0,END)
        key_1=key_entry.get()
        root.destroy()
        cap=cv2.VideoCapture(inputtt)
        vidcap = cv2.VideoCapture(inputtt)    
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        frame_width = int(vidcap.get(3))
        frame_height = int(vidcap.get(4))

        size = (frame_width, frame_height)
        out = cv2.VideoWriter(inputtt,fourcc, 25.0, size)
        global max_frame
        max_frame=0;
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            max_frame+=1
        cap.release()
        print("Total number of Frame in selected Video :",max_frame)
        print(frame_no)
        n=int(frame_no)
        frame_number = 0
        while(vidcap.isOpened()):
            frame_number += 1
            ret, frame = vidcap.read()
            if ret == False:
                break
            if frame_number == n:    
                change_frame_with = embed(frame)
                frame_ = change_frame_with
                frame = change_frame_with
            out.write(frame)
        global aa
        aa=frame_
        
        print("\nEncoded the data successfully in the video file.")
        
    
    global aaaa
    aaaa=take_input
    # Create the login button
    login_button = tk.Button(root, text="Encrypt", command=take_input)
    login_button.pack()
    # Create the error label to display validation errors
    error_label = tk.Label(root, fg="red")
    error_label.pack()
    root.mainloop()
    return aaaa
    
    # Start the main loop
    
            
def input_video_parameters1(frameee):

    # Create the main window
    root = tk.Tk()
    root.title("Video Decryption")
    
        # Create the fame no label and entry widget
    frame_no_label = tk.Label(root, text="Enter the frame number where you want to extract the data :")
    frame_no_label.pack()

    frame_no_entry = tk.Entry(root)
    frame_no_entry.pack()


    # Create the key label and entry widget
    key_label1 = tk.Label(root, text="Enter key:")
    key_label1.pack()

    key_entry = tk.Entry(root)
    key_entry.pack()
    

    def take_input():
        global frame_no_2 ,key_2
        frame_no_2 = frame_no_entry.get()
        key_2=key_entry.get()
        root.destroy()
        cap = cv2.VideoCapture(inputtt)
        max_frame=0;
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            max_frame+=1
        print("Total number of Frame in selected Video :",max_frame)
        print("Enter the secret frame number from where you want to extract data")
        n=int(frame_no_2)
        vidcap = cv2.VideoCapture(inputtt)
        frame_number = 0
        while(vidcap.isOpened()):
            frame_number += 1
            ret, frame = vidcap.read()
            if ret == False:
                break
            if frame_number == n:
                extract(frameee)
                return
    
    # Create the login button
    login_button = tk.Button(root, text="Decrypt", command=take_input)
    login_button.pack()

    # Create the error label to display validation errors
    error_label = tk.Label(root, fg="red")
    error_label.pack()
    


def msgtobinary(msg):
    if type(msg) == str:
        result= ''.join([ format(ord(i), "08b") for i in msg ])
    
    elif type(msg) == bytes or type(msg) == np.ndarray:
        result= [ format(i, "08b") for i in msg ]
    
    elif type(msg) == int or type(msg) == np.uint8:
        result=format(msg, "08b")

    else:
        raise TypeError("Input type is not supported in this function")
    
    return result

    
def KSA(key):
    key_length = len(key)
    S=list(range(256)) 
    j=0
    for i in range(256):
        j=(j+S[i]+key[i % key_length]) % 256
        S[i],S[j]=S[j],S[i]
    return S



def PRGA(S,n):
    i=0
    j=0
    key=[]
    while n>0:
        n=n-1
        i=(i+1)%256
        j=(j+S[i])%256
        S[i],S[j]=S[j],S[i]
        K=S[(S[i]+S[j])%256]
        key.append(K)
    return key



def preparing_key_array(s):
    return [ord(c) for c in s]


    
def encryption(plaintext):
    print("Enter the key : ")
    key=key_1
    key=preparing_key_array(key)

    S=KSA(key)

    keystream=np.array(PRGA(S,len(plaintext)))
    plaintext=np.array([ord(i) for i in plaintext])

    cipher=keystream^plaintext
    ctext=''
    for c in cipher:
        ctext=ctext+chr(c)
    return ctext




def decryption(ciphertext):
    print("Enter the key : ")
    key=key_2
    key=preparing_key_array(key)

    S=KSA(key)

    keystream=np.array(PRGA(S,len(ciphertext)))
    ciphertext=np.array([ord(i) for i in ciphertext])

    decoded=keystream^ciphertext
    dtext=''
    for c in decoded:
        dtext=dtext+chr(c)
    return dtext



def embed(frame):
        print(message)
        data=message
        data=encryption(data)
        print("The encrypted data is : ",data)
        if (len(data) == 0): 
            raise ValueError('Data entered to be encoded is empty')

        data +='*^*^*'
    
        binary_data=msgtobinary(data)
        length_data = len(binary_data)
    
        index_data = 0
    
        for i in frame:
            for pixel in i:
                r, g, b = msgtobinary(pixel)
                if index_data < length_data:
                    pixel[0] = int(r[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data < length_data:
                    pixel[1] = int(g[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data < length_data:
                    pixel[2] = int(b[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data >= length_data:
                    break
            return frame





def extract(frame):
        data_binary = ""
        final_decoded_msg = ""
        for i in frame:
            for pixel in i:
                r, g, b = msgtobinary(pixel) 
                data_binary += r[-1]  
                data_binary += g[-1]  
                data_binary += b[-1]  
                total_bytes = [ data_binary[i: i+8] for i in range(0, len(data_binary), 8) ]
                decoded_data = ""
                for byte in total_bytes:
                    decoded_data += chr(int(byte, 2))
                    if decoded_data[-5:] == "*^*^*": 
                        for i in range(0,len(decoded_data)-5):
                            final_decoded_msg += decoded_data[i]
                        final_decoded_msg = decryption(final_decoded_msg)
                        print("\n\nThe Encoded data which was hidden in the Video was :--\n",final_decoded_msg)
                        text1.insert(END,final_decoded_msg)
                        return 



def select_video():
    global inputtt 
    inputtt=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("Video file","*.mp4"),("Video file","*.mp4"),("All Files","*.mov")))
    piacc = "backgroundvid.png"
    img=Image.open(piacc)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=460,height=340)
    lbl.image=img
    vidname=Label(root,text=inputtt,bg="#03ffe7",font="arial")
    vidname.place(x=190,y=60,width=440,height=20)
    



def encode_vid_data():
    cap=cv2.VideoCapture(inputtt)
    vidcap = cv2.VideoCapture(inputtt)    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    frame_width = int(vidcap.get(3))
    frame_height = int(vidcap.get(4))

    size = (frame_width, frame_height)
    out = cv2.VideoWriter(inputtt,fourcc, 25.0, size)
    global max_frame
    max_frame=0;
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        max_frame+=1
    cap.release()
    print("Total number of Frame in selected Video :",max_frame)
    input_video_parameters()
    print(frame_no)
    n=int(frame_no)
    frame_number = 0
    while(vidcap.isOpened()):
        frame_number += 1
        ret, frame = vidcap.read()
        if ret == False:
            break
        if frame_number == n:    
            change_frame_with = embed(frame)
            frame_ = change_frame_with
            frame = change_frame_with
        out.write(frame)
    
    print("\nEncoded the data successfully in the video file.")
    return frame_



def decode_vid_data(frame_):
    cap = cv2.VideoCapture(inputtt)
    max_frame=0;
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        max_frame+=1
    print("Total number of Frame in selected Video :",max_frame)
    print("Enter the secret frame number from where you want to extract data")
    n=int(frame_no_2)
    vidcap = cv2.VideoCapture(inputtt)
    frame_number = 0
    while(vidcap.isOpened()):
        frame_number += 1
        ret, frame = vidcap.read()
        if ret == False:
            break
        if frame_number == n:
            extract(frame_)
            return




def select_audio():
    global nameoffile
    nameoffile=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("Audio file","*.mp3"),("Audio file","*.wav")))
    pisscc = "backgrounddaud.png"
    img=Image.open(pisscc)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=460,height=340)
    lbl.image=img
    audname=Label(root,text=nameoffile,bg="red",font="arial")
    audname.place(x=190,y=60,width=440,height=20)


def encode_aud_data():
    import wave
    song = wave.open(nameoffile, mode='rb')

    nframes=song.getnframes()
    frames=song.readframes(nframes)
    frame_list=list(frames)
    frame_bytes=bytearray(frame_list)
    

    data = text1.get(1.0,END)

    res = ''.join(format(i, '08b') for i in bytearray(data, encoding ='utf-8'))     
    print("\nThe string after binary conversion :- " + (res))   
    length = len(res)
    print("\nLength of binary after conversion :- ",length)

    data = data + '*^*^*'

    result = []
    for c in data:
        bits = bin(ord(c))[2:].zfill(8)
        result.extend([int(b) for b in bits])

    j = 0
    for i in range(0,len(result),1): 
        res = bin(frame_bytes[j])[2:].zfill(8)
        if res[len(res)-4]== result[i]:
            frame_bytes[j] = (frame_bytes[j] & 253)      #253: 11111101
        else:
            frame_bytes[j] = (frame_bytes[j] & 253) | 2
            frame_bytes[j] = (frame_bytes[j] & 254) | result[i]
        j = j + 1
    
    frame_modified = bytes(frame_bytes)
    
    root = tk.Tk()
    root.title("Save Audio File:")

    file_name_label = tk.Label(root, text="Enter the name of the encrypted file :")
    file_name_label.pack()

    file_name_entry = tk.Entry(root)
    file_name_entry.pack()
    def take_input():
        stegofile=file_name_entry.get()
        root.destroy()
        with wave.open(stegofile, 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)
        print("\nEncoded the data successfully in the audio file.")    
        song.close()
    login_button = tk.Button(root, text="Save", command=take_input)
    login_button.pack()
    root.mainloop()


# In[12]:


def decode_aud_data():
    import wave
    song = wave.open(nameoffile, mode='rb')
    nframes=song.getnframes()
    frames=song.readframes(nframes)
    frame_list=list(frames)
    frame_bytes=bytearray(frame_list)

    extracted = ""
    p=0
    for i in range(len(frame_bytes)):
        if(p==1):
            break
        res = bin(frame_bytes[i])[2:].zfill(8)
        if res[len(res)-2]==0:
            extracted+=res[len(res)-4]
        else:
            extracted+=res[len(res)-1]
    
        all_bytes = [ extracted[i: i+8] for i in range(0, len(extracted), 8) ]
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "*^*^*":
                
                text1.insert(END,decoded_data[:-5])
                #print("The Encoded data was :--",decoded_data[:-5])
                p=1
                break









root=Tk()
root.title("StegoStream")
#setting window size
width=1090
height=650
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)
bgg=ImageTk.PhotoImage(file="background5.png")
Label(root,text="cyber sciencs",bg="red",font="arial",image=bgg).place(x=0,y=0)



def about_us():
    # Create a frame to hold all of the contents
    
    frame = tk.Frame(root, bg="#F5F5F5", width=990, height=651)
    frame.place(x=158,y=0)

    # Define a custom font
    font = ("Helvetica", 14)

    # Add a title label with the project name
    project_name_label = tk.Label(frame, text="Welcome to our StegoStream Project", font=("Helvetica", 28, "bold"), fg="#262626", bg="#F5F5F5")
    project_name_label.pack(pady=50)

    # Add a label with the main description
    description_label = tk.Label(frame, text="Our team specializes in providing cutting-edge solutions for secure and covert information transfer through images, audio, and video files. Our advanced algorithms enable us to embed messages seamlessly within digital media, making it virtually impossible to detect the presence of hidden information. We are committed to customer satisfaction and aim to provide an exceptional user experience, and believe in the importance of education and raising awareness of steganography and its potential uses.", font=font, fg="#444444", bg="#F5F5F5", wraplength=880, justify="center")
    description_label.pack(pady=20)

    # Add a label with information about the team
    team_label = tk.Label(frame, text="Our team consists of experts in cryptography, data security, and software development, bringing together a wealth of knowledge and experience to deliver innovative and reliable solutions for our clients. We are constantly researching and implementing the latest technologies to ensure that our software stays ahead of the curve in terms of security and functionality.", font=font, fg="#444444", bg="#F5F5F5", wraplength=880, justify="center")
    team_label.pack(pady=20)

    # Add a separator line
    separator = tk.Frame(frame, height=2, width=880, bg="#CCCCCC")
    separator.pack(pady=20)

    # Add a label with a thank you message
    thank_you_label = tk.Label(frame, text="Thank you for choosing our Steganography Project for your secure data transfer needs. Our commitment to innovation, reliability, and customer satisfaction means that you can trust us to provide the highest level of security and peace of mind.", font=font, fg="#444444", bg="#F5F5F5", wraplength=880, justify="center")
    thank_you_label.pack(pady=20)

    # Add a footer label with the project name and copyright
    footer_label = tk.Label(frame, text="StegoStream Project © 2023", font=("Helvetica", 10), fg="#262626", bg="#F5F5F5")
    footer_label.pack(side="bottom", pady=10)



def contact_us():
    contact=tk.Frame(root)
    contact.configure(width=935,height=651)
    contact.place(x=158,y=0)

    # Create a heading label
    heading_font = font.Font(family="Arial", size=24, weight="bold")
    heading_label = tk.Label(contact, text="Contact Us", font=heading_font, bg="#f0f0f0", fg="#333", padx=20, pady=20)
    heading_label.grid(row=0, column=0, columnspan=2)

    # Create labels and entry fields for name, email, message, and phone number
    label_font = font.Font(family="Arial", size=16)
    entry_font = font.Font(family="Arial", size=14)
    name_label = tk.Label(contact, text="Name:", font=label_font, bg="#f0f0f0", fg="#333", padx=20, pady=10)
    name_label.grid(row=1, column=0, sticky="w")
    name_entry = tk.Entry(contact, font=entry_font, width=50, bd=2, relief="groove")
    name_entry.grid(row=1, column=1, pady=10)

    email_label = tk.Label(contact, text="Email:", font=label_font, bg="#f0f0f0", fg="#333", padx=20, pady=10)
    email_label.grid(row=2, column=0, sticky="w")
    email_entry = tk.Entry(contact, font=entry_font, width=50, bd=2, relief="groove")
    email_entry.grid(row=2, column=1, pady=10)

    phone_label = tk.Label(contact, text="Phone Number:", font=label_font, bg="#f0f0f0", fg="#333", padx=20, pady=10)
    phone_label.grid(row=3, column=0, sticky="w")
    phone_entry = tk.Entry(contact, font=entry_font, width=50, bd=2, relief="groove")
    phone_entry.grid(row=3, column=1, pady=10)

    message_label = tk.Label(contact, text="Message:", font=label_font, bg="#f0f0f0", fg="#333", padx=20, pady=10)
    message_label.grid(row=4, column=0, sticky="w")
    message_entry = tk.Text(contact, font=entry_font, width=50, height=10, wrap="word", bd=2, relief="groove")
    message_entry.grid(row=4, column=1, pady=10)

    # Create a submit button
    submit_button = tk.Button(contact, text="Submit", font=label_font, bg="#4CAF50", fg="white", width=10, bd=2, relief="raised", command=lambda: submit_message())
    submit_button.grid(row=5, column=1, pady=(20, 50), sticky="e")

    # Add a confirmation message label
    confirmation_label = tk.Label(contact, font=label_font, bg="#f0f0f0", fg="#4CAF50")
    confirmation_label.grid(row=6, column=0, columnspan=2, pady=(0, 50))

    # Add a footer label
    footer_font = font.Font(family="Arial", size=12)
    footer_label = tk.Label(contact, text="© 2023 Contact Us, Inc. All rights reserved.", font=footer_font, bg="#f0f0f0", fg="#333")
    footer_label.grid(row=7, column=0, columnspan=2, pady=(20, 0), padx=20, sticky="w")
    footer_frame = tk.Frame(contact, bg="#333")

    # Add content to the footer
    tk.Label(footer_frame, text="Follow us on social media:", fg="#fff", bg="#333", font=("Arial", 10)).pack(pady=10)
    social_frame = tk.Frame(footer_frame, bg="#333")
    tk.Label(social_frame, text="Facebook", fg="#fff", bg="#333", font=("Arial", 10)).pack(side="left")
    tk.Label(social_frame, text="Twitter", fg="#fff", bg="#333", font=("Arial", 10)).pack(side="left", padx=20)
    tk.Label(social_frame, text="Instagram", fg="#fff", bg="#333", font=("Arial", 10)).pack(side="left")
    social_frame.pack()
    

    # Define a function to handle submitting the form
    def submit_message():
        name = name_entry.get()
        email = email_entry.get()
        phone_number = phone_entry.get()
        message = message_entry.get("1.0", "end-1c")
        confirmation_label.config(text=f"Thank you, {name}! Your message has been sent.")
        name_entry.delete(0, "end")
        email_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        message_entry.delete("1.0", "end")




def home_page():
    Homeframe=tk.Frame(root)
    Homeframe.pack_propagate(False)
    Homeframe.configure(width=935,height=651)
    Homeframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(Homeframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    
    
    GButton_346=tk.Button(Homeframe)
    GButton_346["bg"] = "#7be37b"
    ft = tkFont.Font(size=38)
    GButton_346["font"] = ft
    GButton_346["fg"] = "#000000"
    GButton_346["text"] = "SENDER"
    GButton_346.place(x=100,y=200,width=309,height=254)
    GButton_346["command"] = sender

    GButton_317=tk.Button(Homeframe)
    GButton_317["bg"] = "#00ced1"
    ft = tkFont.Font(size=38)
    GButton_317["font"] = ft
    GButton_317["fg"] = "#000000"
    GButton_317["text"] = "RECEIVER"
    GButton_317.place(x=530,y=200,width=309,height=254)
    GButton_317["command"] = receiver

    GLabel_709=tk.Label(Homeframe)
    GLabel_709["bg"] = "#ffb800"
    ft = tkFont.Font(family='Times',size=16)
    GLabel_709["font"] = ft
    GLabel_709["fg"] = "White"
    GLabel_709["justify"] = "left"
    GLabel_709["text"] = "On which end you re using this Application ?"
    GLabel_709.place(x=100,y=100,width=379,height=30)

    #GLabel_779=tk.Frame(root)
    #GLabel_779.pack_propagate(False)
    #GLabel_779.configure(width=935,height=651)
    #GLabel_779.place(x=156,y=0)






    #setting title

def sender():
    senderframe=tk.Frame(root)
    senderframe.pack_propagate(False)
    senderframe.configure(width=935,height=651)
    senderframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(senderframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    

    GButton_423=tk.Button(senderframe)
    GButton_423["bg"] = "#ff0000"
    GButton_423["cursor"] = "arrow"
    ft = tkFont.Font(family='Times',size=40)
    GButton_423["font"] = ft
    GButton_423["fg"] = "#000000"
    GButton_423["justify"] = "center"
    GButton_423["text"] = "IMAGE"
    GButton_423["relief"] = "groove"
    GButton_423.place(x=10,y=200,width=290,height=254)
    GButton_423["command"] = image_sender
    

    GButton_38=tk.Button(senderframe)
    GButton_38["bg"] = "#01aaed"
    ft = tkFont.Font(family='Times',size=40)
    GButton_38["font"] = ft
    GButton_38["fg"] = "#000000"
    GButton_38["justify"] = "center"
    GButton_38["text"] = "Audio"
    GButton_38["relief"] = "groove"
    GButton_38.place(x=320,y=200,width=290,height=254)
    GButton_38["command"] = Audio_sender
    

    GButton_229=tk.Button(senderframe)
    GButton_229["bg"] = "#ffb800"
    ft = tkFont.Font(family='Times',size=40)
    GButton_229["font"] = ft
    GButton_229["fg"] = "#000000"
    GButton_229["justify"] = "center"
    GButton_229["text"] = "Video"
    GButton_229["relief"] = "groove"
    GButton_229.place(x=630,y=200,width=290,height=254)
    GButton_229["command"] = video_sender



def receiver():
    receiverframe=tk.Frame(root)
    receiverframe.pack_propagate(False)
    receiverframe.configure(width=935,height=651)
    receiverframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(receiverframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    

    GButton_423=tk.Button(receiverframe)
    GButton_423["bg"] = "#ff0000"
    GButton_423["cursor"] = "arrow"
    ft = tkFont.Font(family='Times',size=40)
    GButton_423["font"] = ft
    GButton_423["fg"] = "#000000"
    GButton_423["justify"] = "center"
    GButton_423["text"] = "IMAGE"
    GButton_423["relief"] = "groove"
    GButton_423.place(x=10,y=200,width=290,height=254)
    GButton_423["command"] = image_receiver
    

    GButton_38=tk.Button(receiverframe)
    GButton_38["bg"] = "#01aaed"
    ft = tkFont.Font(family='Times',size=40)
    GButton_38["font"] = ft
    GButton_38["fg"] = "#000000"
    GButton_38["justify"] = "center"
    GButton_38["text"] = "Audio"
    GButton_38["relief"] = "groove"
    GButton_38.place(x=320,y=200,width=290,height=254)
    GButton_38["command"] = audio_receiver
    

    GButton_229=tk.Button(receiverframe)
    GButton_229["bg"] = "#ffb800"
    ft = tkFont.Font(family='Times',size=40)
    GButton_229["font"] = ft
    GButton_229["fg"] = "#000000"
    GButton_229["justify"] = "center"
    GButton_229["text"] = "Video"
    GButton_229["relief"] = "groove"
    GButton_229.place(x=630,y=200,width=290,height=254)
    GButton_229["command"] = video_receiver


def image_sender():
    imagesenderframe=tk.Frame(root)
    imagesenderframe.configure(width=935,height=651)
    imagesenderframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(imagesenderframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    GLabel_958=tk.Label(imagesenderframe)
    GLabel_958["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_958["font"] = ft
    GLabel_958["fg"] = "#333333"
    GLabel_958["justify"] = "center"
    GLabel_958["text"] = ""
    GLabel_958.place(x=30,y=80,width=440,height=345)
    global lbl
    lbl=Label(GLabel_958,bg="black")
    lbl.place(x=0,y=0)
    GLabel_958.place(x=30,y=80,width=440,height=345)
    


    GLabel_629=tk.Label(imagesenderframe)
    GLabel_629["bg"] = "#ffffff"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_629["font"] = ft
    GLabel_629["fg"] = "#333333"
    GLabel_629["justify"] = "center"
    GLabel_629["text"] = ""
    GLabel_629.place(x=470,y=80,width=440,height=345)
    global text1
    text1=Text(GLabel_629,font="robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=400)

    Scrollbar1=Scrollbar(GLabel_629)
    Scrollbar1.place(x=420,y=0,height=400)
    Scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=Scrollbar1.set)



    GButton_318=tk.Button(imagesenderframe)
    GButton_318["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=20)
    GButton_318["font"] = ft
    GButton_318["fg"] = "#ffffff"
    GButton_318["justify"] = "center"
    GButton_318["text"] = "Select Image"
    GButton_318.place(x=30,y=450,width=432,height=105)
    GButton_318["command"] = showimage
    
    
    GButton_303=tk.Button(imagesenderframe)
    GButton_303["bg"] = "#2fff2f"
    ft = tkFont.Font(family='Times',size=20)
    GButton_303["font"] = ft
    GButton_303["fg"] = "#ffffff"
    GButton_303["justify"] = "center"
    GButton_303["text"] = "Encrypt"
    GButton_303.place(x=470,y=450,width=205,height=45)
    GButton_303["command"] = hide
   

    GButton_339=tk.Button(imagesenderframe)
    GButton_339["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=20)
    GButton_339["font"] = ft
    GButton_339["fg"] = "#ffffff"
    GButton_339["justify"] = "center"
    GButton_339["text"] = "Save"
    GButton_339.place(x=700,y=450,width=205,height=45)
    GButton_339["command"] = save
  
    GButton_565=tk.Button(imagesenderframe)
    GButton_565["bg"] = "#ff0000"
    ft = tkFont.Font(family='Times',size=20)
    GButton_565["font"] = ft
    GButton_565["fg"] = "#ffffff"
    GButton_565["justify"] = "center"
    GButton_565["text"] = "Select PDF"
    GButton_565.place(x=470,y=510,width=205,height=45)
    GButton_565["command"] = pdfextract
   

    GButton_480=tk.Button(imagesenderframe)
    GButton_480["bg"] = "#1e90ff"
    ft = tkFont.Font(family='Times',size=20)
    GButton_480["font"] = ft
    GButton_480["fg"] = "#ffffff"
    GButton_480["justify"] = "center"
    GButton_480["text"] = "Select Word"
    GButton_480.place(x=700,y=510,width=204,height=45)
    GButton_480["command"] = Wordextract


    





def video_sender():
    videosenderframe=tk.Frame(root)
    videosenderframe.configure(width=935,height=651)
    videosenderframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(videosenderframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    GLabel_958=tk.Label(videosenderframe)
    GLabel_958["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_958["font"] = ft
    GLabel_958["fg"] = "#333333"
    GLabel_958["justify"] = "center"
    GLabel_958["text"] = ""
    GLabel_958.place(x=30,y=80,width=440,height=345)
    global lbl
    lbl=Label(GLabel_958,bg="black")
    lbl.place(x=0,y=0)
    GLabel_958.place(x=30,y=80,width=440,height=345)
    


    GLabel_629=tk.Label(videosenderframe)
    GLabel_629["bg"] = "#ffffff"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_629["font"] = ft
    GLabel_629["fg"] = "#333333"
    GLabel_629["justify"] = "center"
    GLabel_629["text"] = ""
    GLabel_629.place(x=470,y=80,width=440,height=345)
    global text1
    text1=Text(GLabel_629,font="robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=400)

    Scrollbar1=Scrollbar(GLabel_629)
    Scrollbar1.place(x=420,y=0,height=400)
    Scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=Scrollbar1.set)


    GButton_318=tk.Button(videosenderframe)
    GButton_318["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=20)
    GButton_318["font"] = ft
    GButton_318["fg"] = "#ffffff"
    GButton_318["justify"] = "center"
    GButton_318["text"] = "Select Video"
    GButton_318["relief"] = "groove"
    GButton_318.place(x=30,y=440,width=437,height=47)
    GButton_318["command"] = select_video

    GButton_303=tk.Button(videosenderframe)
    GButton_303["bg"] = "#2fff2f"
    ft = tkFont.Font(family='Times',size=20)
    GButton_303["font"] = ft
    GButton_303["fg"] = "#ffffff"
    GButton_303["justify"] = "center"
    GButton_303["text"] = "Encode Video"
    GButton_303["relief"] = "groove"
    GButton_303.place(x=470,y=440,width=439,height=47)
    global anana
    GButton_303["command"] = input_video_parameters

    GButton_565=tk.Button(videosenderframe)
    GButton_565["bg"] = "#ff0000"
    ft = tkFont.Font(family='Times',size=20)
    GButton_565["font"] = ft
    GButton_565["fg"] = "#ffffff"
    GButton_565["justify"] = "center"
    GButton_565["text"] = "Select PDF"
    GButton_565["relief"] = "groove"
    GButton_565.place(x=470,y=500,width=439,height=45)
    GButton_565["command"] = pdfextract

    GButton_480=tk.Button(videosenderframe)
    GButton_480["bg"] = "#1e90ff"
    ft = tkFont.Font(family='Times',size=20)
    GButton_480["font"] = ft
    GButton_480["fg"] = "#ffffff"
    GButton_480["justify"] = "center"
    GButton_480["text"] = "Select Word"
    GButton_480["relief"] = "groove"
    GButton_480.place(x=30,y=500,width=436,height=45)
    GButton_480["command"] = Wordextract



def video_receiver():
    videoreceiverframe=tk.Frame(root)
    videoreceiverframe.configure(width=935,height=651)
    videoreceiverframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(videoreceiverframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    GLabel_958=tk.Label(videoreceiverframe)
    GLabel_958["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_958["font"] = ft
    GLabel_958["fg"] = "#333333"
    GLabel_958["justify"] = "center"
    GLabel_958["text"] = ""
    GLabel_958.place(x=30,y=80,width=440,height=345)
    global lbl
    lbl=Label(GLabel_958,bg="black")
    lbl.place(x=0,y=0)
    GLabel_958.place(x=30,y=80,width=440,height=345)
    


    GLabel_629=tk.Label(videoreceiverframe)
    GLabel_629["bg"] = "#ffffff"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_629["font"] = ft
    GLabel_629["fg"] = "#333333"
    GLabel_629["justify"] = "center"
    GLabel_629["text"] = ""
    GLabel_629.place(x=470,y=80,width=440,height=345)
    global text1
    text1=Text(GLabel_629,font="robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=400)

    Scrollbar1=Scrollbar(GLabel_629)
    Scrollbar1.place(x=420,y=0,height=400)
    Scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=Scrollbar1.set)


    GButton_318=tk.Button(videoreceiverframe)
    GButton_318["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=20)
    GButton_318["font"] = ft
    GButton_318["fg"] = "#ffffff"
    GButton_318["justify"] = "center"
    GButton_318["text"] = "Select Video"
    GButton_318["relief"] = "groove"
    GButton_318.place(x=30,y=440,width=437,height=105)
    GButton_318["command"] = select_video

    GButton_303=tk.Button(videoreceiverframe)
    GButton_303["bg"] = "#2fff2f"
    ft = tkFont.Font(family='Times',size=20)
    GButton_303["font"] = ft
    GButton_303["fg"] = "#ffffff"
    GButton_303["justify"] = "center"
    GButton_303["text"] = "Decode Video"
    GButton_303["relief"] = "groove"
    GButton_303.place(x=470,y=440,width=439,height=47)
    GButton_303["command"] = lambda:input_video_parameters1(aa)

    GButton_480=tk.Button(videoreceiverframe)
    GButton_480["bg"] = "#ff0000"
    ft = tkFont.Font(family='Times',size=20)
    GButton_480["font"] = ft
    GButton_480["fg"] = "#ffffff"
    GButton_480["justify"] = "center"
    GButton_480["text"] = "Export as PDF"
    GButton_480["relief"] = "groove"
    GButton_480.place(x=470,y=500,width=436,height=45)
    GButton_480["command"] = createPdf



    



def Audio_sender():
    audiosenderframe=tk.Frame(root)
    audiosenderframe.configure(width=935,height=651)
    audiosenderframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(audiosenderframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    GLabel_958=tk.Label(audiosenderframe)
    GLabel_958["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_958["font"] = ft
    GLabel_958["fg"] = "#333333"
    GLabel_958["justify"] = "center"
    GLabel_958["text"] = ""
    GLabel_958.place(x=30,y=80,width=440,height=345)
    global lbl
    lbl=Label(GLabel_958,bg="black")
    lbl.place(x=0,y=0)
    GLabel_958.place(x=30,y=80,width=440,height=345)
    


    GLabel_629=tk.Label(audiosenderframe)
    GLabel_629["bg"] = "#ffffff"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_629["font"] = ft
    GLabel_629["fg"] = "#333333"
    GLabel_629["justify"] = "center"
    GLabel_629["text"] = ""
    GLabel_629.place(x=470,y=80,width=440,height=345)
    global text1
    text1=Text(GLabel_629,font="robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=400)

    Scrollbar1=Scrollbar(GLabel_629)
    Scrollbar1.place(x=420,y=0,height=400)
    Scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=Scrollbar1.set)

    GButton_318=tk.Button(audiosenderframe)
    GButton_318["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=20)
    GButton_318["font"] = ft
    GButton_318["fg"] = "#ffffff"
    GButton_318["justify"] = "center"
    GButton_318["text"] = "Select Audio"
    GButton_318["relief"] = "groove"
    GButton_318.place(x=30,y=440,width=437,height=47)
    GButton_318["command"] = select_audio

    GButton_303=tk.Button(audiosenderframe)
    GButton_303["bg"] = "#2fff2f"
    ft = tkFont.Font(family='Times',size=20)
    GButton_303["font"] = ft
    GButton_303["fg"] = "#ffffff"
    GButton_303["justify"] = "center"
    GButton_303["text"] = "Encode Audio"
    GButton_303["relief"] = "groove"
    GButton_303.place(x=470,y=440,width=439,height=47)
    GButton_303["command"] = encode_aud_data

    GButton_565=tk.Button(audiosenderframe)
    GButton_565["bg"] = "#ff0000"
    ft = tkFont.Font(family='Times',size=20)
    GButton_565["font"] = ft
    GButton_565["fg"] = "#ffffff"
    GButton_565["justify"] = "center"
    GButton_565["text"] = "Select PDF"
    GButton_565["relief"] = "groove"
    GButton_565.place(x=470,y=500,width=439,height=45)
    GButton_565["command"] = pdfextract

    GButton_480=tk.Button(audiosenderframe)
    GButton_480["bg"] = "#1e90ff"
    ft = tkFont.Font(family='Times',size=20)
    GButton_480["font"] = ft
    GButton_480["fg"] = "#ffffff"
    GButton_480["justify"] = "center"
    GButton_480["text"] = "Select Word"
    GButton_480["relief"] = "groove"
    GButton_480.place(x=30,y=500,width=436,height=45)
    GButton_480["command"] = Wordextract



def image_receiver():
    imagereceiverframe=tk.Frame(root)
    imagereceiverframe.configure(width=935,height=651)
    imagereceiverframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(imagereceiverframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    GLabel_958=tk.Label(imagereceiverframe)
    GLabel_958["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_958["font"] = ft
    GLabel_958["fg"] = "#333333"
    GLabel_958["justify"] = "center"
    GLabel_958["text"] = ""
    GLabel_958.place(x=30,y=80,width=440,height=345)
    global lbl
    lbl=Label(GLabel_958,bg="black")
    lbl.place(x=0,y=0)
    GLabel_958.place(x=30,y=80,width=440,height=345)
    


    GLabel_629=tk.Label(imagereceiverframe)
    GLabel_629["bg"] = "#ffffff"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_629["font"] = ft
    GLabel_629["fg"] = "#333333"
    GLabel_629["justify"] = "center"
    GLabel_629["text"] = ""
    GLabel_629.place(x=470,y=80,width=440,height=345)
    global text1
    text1=Text(GLabel_629,font="robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=400)

    Scrollbar1=Scrollbar(GLabel_629)
    Scrollbar1.place(x=420,y=0,height=400)
    Scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=Scrollbar1.set)

    GButton_318=tk.Button(imagereceiverframe)
    GButton_318["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=20)
    GButton_318["font"] = ft
    GButton_318["fg"] = "#ffffff"
    GButton_318["justify"] = "center"
    GButton_318["text"] = "Select Image"
    GButton_318["relief"] = "groove"
    GButton_318.place(x=30,y=440,width=434,height=105)
    GButton_318["command"] = showimage

    GButton_303=tk.Button(imagereceiverframe)
    GButton_303["bg"] = "#2fff2f"
    ft = tkFont.Font(family='Times',size=20)
    GButton_303["font"] = ft
    GButton_303["fg"] = "#ffffff"
    GButton_303["justify"] = "center"
    GButton_303["text"] = "Decode Image"
    GButton_303["relief"] = "groove"
    GButton_303.place(x=470,y=440,width=439,height=47)
    GButton_303["command"] = show

    GButton_480=tk.Button(imagereceiverframe)
    GButton_480["bg"] = "#ff0000"
    ft = tkFont.Font(family='Times',size=20)
    GButton_480["font"] = ft
    GButton_480["fg"] = "#ffffff"
    GButton_480["justify"] = "center"
    GButton_480["text"] = "Export as PDF"
    GButton_480["relief"] = "groove"
    GButton_480.place(x=470,y=500,width=436,height=45)
    GButton_480["command"] = createPdf


def audio_receiver():
    audioreceiverframe=tk.Frame(root)
    audioreceiverframe.configure(width=935,height=651)
    audioreceiverframe.place(x=158,y=0)
    photo = PhotoImage(file="background5.png")
    label=Label(audioreceiverframe,image=photo)
    label.image=photo
    label.place(x=0,y=0)

    GLabel_958=tk.Label(audioreceiverframe)
    GLabel_958["bg"] = "#000000"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_958["font"] = ft
    GLabel_958["fg"] = "#333333"
    GLabel_958["justify"] = "center"
    GLabel_958["text"] = ""
    GLabel_958.place(x=30,y=80,width=440,height=345)
    global lbl
    lbl=Label(GLabel_958,bg="black")
    lbl.place(x=0,y=0)
    GLabel_958.place(x=30,y=80,width=440,height=345)
    


    GLabel_629=tk.Label(audioreceiverframe)
    GLabel_629["bg"] = "#ffffff"
    ft = tkFont.Font(family='Times',size=10)
    GLabel_629["font"] = ft
    GLabel_629["fg"] = "#333333"
    GLabel_629["justify"] = "center"
    GLabel_629["text"] = ""
    GLabel_629.place(x=470,y=80,width=440,height=345)
    global text1
    text1=Text(GLabel_629,font="robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
    text1.place(x=0,y=0,width=430,height=400)

    Scrollbar1=Scrollbar(GLabel_629)
    Scrollbar1.place(x=420,y=0,height=400)
    Scrollbar1.configure(command=text1.yview)
    text1.configure(yscrollcommand=Scrollbar1.set)


    GButton_318=tk.Button(audioreceiverframe)
    GButton_318["bg"] = "#00ced1"
    ft = tkFont.Font(family='Times',size=20)
    GButton_318["font"] = ft
    GButton_318["fg"] = "#ffffff"
    GButton_318["justify"] = "center"
    GButton_318["text"] = "Select Audio"
    GButton_318["relief"] = "groove"
    GButton_318.place(x=30,y=440,width=434,height=105)
    GButton_318["command"] = select_audio

    GButton_303=tk.Button(audioreceiverframe)
    GButton_303["bg"] = "#2fff2f"
    ft = tkFont.Font(family='Times',size=20)
    GButton_303["font"] = ft
    GButton_303["fg"] = "#ffffff"
    GButton_303["justify"] = "center"
    GButton_303["text"] = "Decode Audio"
    GButton_303["relief"] = "groove"
    GButton_303.place(x=470,y=440,width=439,height=47)
    GButton_303["command"] = decode_aud_data

    GButton_480=tk.Button(audioreceiverframe)
    GButton_480["bg"] = "#ff0000"
    ft = tkFont.Font(family='Times',size=20)
    GButton_480["font"] = ft
    GButton_480["fg"] = "#ffffff"
    GButton_480["justify"] = "center"
    GButton_480["text"] = "Export as PDF"
    GButton_480["relief"] = "groove"
    GButton_480.place(x=470,y=500,width=436,height=45)
    GButton_480["command"] = createPdf




GLabel_854=tk.Label(root)
GLabel_854["activebackground"] = "#252836"
GLabel_854["activeforeground"] = "#252836"
GLabel_854["anchor"] = "center"
GLabel_854["bg"] = "#252836"
ft = tkFont.Font(family='Times',size=10)
GLabel_854["font"] = ft
GLabel_854["fg"] = "#333333"
GLabel_854["justify"] = "center"
GLabel_854["text"] = ""
GLabel_854.place(x=0,y=0,width=158,height=651)

Home=tk.Button(root)
Home["activebackground"] = "#252836"
Home["activeforeground"] = "#252836"
Home["bg"] = "#252836"
ft = tkFont.Font(family='Times',size=13)
Home["font"] = ft
Home["fg"] = "#ffffff"
Home["justify"] = "left"
Home["text"] = "Home"
Home["relief"] = "groove"
Home.place(x=20,y=30,width=127,height=30)
Home["command"] = home_page




GButton_385=tk.Button(root)
GButton_385["activebackground"] = "#252836"
GButton_385["activeforeground"] = "#252836"
GButton_385["anchor"] = "center"
GButton_385["bg"] = "#252836"
ft = tkFont.Font(family='Times',size=13)
GButton_385["font"] = ft
GButton_385["fg"] = "#ffffff"
GButton_385["justify"] = "left"
GButton_385["text"] = "Contact Us"
GButton_385["relief"] = "groove"
GButton_385.place(x=20,y=70,width=127,height=30)
GButton_385["command"] = contact_us

GButton_603=tk.Button(root)
GButton_603["activebackground"] = "#252836"
GButton_603["activeforeground"] = "#252836"
GButton_603["anchor"] = "center"
GButton_603["bg"] = "#252836"
ft = tkFont.Font(family='Times',size=13)
GButton_603["font"] = ft
GButton_603["fg"] = "#ffffff"
GButton_603["justify"] = "left"
GButton_603["text"] = "About Us"
GButton_603["relief"] = "groove"
GButton_603.place(x=20,y=110,width=127,height=30)
GButton_603["command"] = about_us


GLabel_190=tk.Label(root)
GLabel_190["bg"] = "#fad400"
ft = tkFont.Font(family='Times',size=10)
GLabel_190["font"] = ft
GLabel_190["fg"] = "#333333"
GLabel_190["justify"] = "center"
GLabel_190["text"] = ""
GLabel_190.place(x=10,y=30,width=4,height=30)

GLabel_118=tk.Label(root)
GLabel_118["bg"] = "#fad400"
ft = tkFont.Font(family='Times',size=10)
GLabel_118["font"] = ft
GLabel_118["fg"] = "#333333"
GLabel_118["justify"] = "center"
GLabel_118["text"] = ""
GLabel_118.place(x=10,y=70,width=4,height=30)

GLabel_37=tk.Label(root)
GLabel_37["bg"] = "#fad400"
ft = tkFont.Font(family='Times',size=10)
GLabel_37["font"] = ft
GLabel_37["fg"] = "#333333"
GLabel_37["justify"] = "center"
GLabel_37["text"] = ""
GLabel_37.place(x=10,y=110,width=4,height=30)





GButton_346=tk.Button(root)
GButton_346["bg"] = "#7be37b"
ft = tkFont.Font(size=38)
GButton_346["font"] = ft
GButton_346["fg"] = "#000000"
GButton_346["text"] = "SENDER"
GButton_346.place(x=260,y=180,width=309,height=254)
GButton_346["command"] = sender

GButton_317=tk.Button(root)
GButton_317["bg"] = "#00ced1"
ft = tkFont.Font(size=38)
GButton_317["font"] = ft
GButton_317["fg"] = "#000000"
GButton_317["text"] = "RECEIVER"
GButton_317.place(x=670,y=180,width=309,height=254)
GButton_317["command"] = receiver



root.mainloop()