import folium
import webbrowser
import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
from tkinter import filedialog
import exifread
#read_map = geoip2.database.Reader('.\\GeoLite2-City.mmdb')
def open_html(pos):
    m = folium.Map(location=pos[0],zoom_start=10,control_scale=True,max_zoom=35)
    for apos in pos:
        WE = round(apos[0],14)
        NS = round(apos[1],13)
        folium.Marker([WE,NS],popup='Some Other Location',icon=folium.Icon(icon='cloud')).add_to(m)
        folium.Circle(radius=150,location=[WE,NS],color='crimson',fill=True,fill_color='#fdbebe',fill_opacity=0.1).add_to(m)
    m.add_child(folium.LatLngPopup())
    m.add_child(folium.ClickForMarker())
    
    m.save("pos.html")
    webbrowser.open("pos.html") #重新打开HTML网页
def run():
    dirs = []
    for dir in list(msgw.get(0,msgw.size()-1)):
        f = open(dir, 'rb')
        tags = exifread.process_file(f)
        #print(tags['GPS GPSLatitude'],tags['GPS GPSLongitude'])
        try:
            ns = str(tags['GPS GPSLatitude']).replace('[','').replace(']','').split(', ')
            we = str(tags['GPS GPSLongitude']).replace('[','').replace(']','').split(', ')
            print(ns,we)
            ns[2] = eval(ns[2])
            we[2] = eval(we[2])
            NS = int(ns[0]) + int(ns[1])/60 + ns[2]/3600
            WE = int(we[0]) + int(we[1])/60 + we[2]/3600
            dirs.append([NS,WE])
        except:messagebox.showerror('Error','[ERROR]:There is no position in "' + dir+'".')
    #NS,WE = check.Transform(NS,WE)
    if dirs != []:open_html(dirs)
def delete():
    index = msgw.curselection()
    if len(index) == 1:msgw.delete(index)
    elif len(index) == 0:pass
    else:
        for a,b in zip(list(index),range(len(index))):msgw.delete(int(a-b))
def opfile():
    pth = filedialog.askopenfilenames()#['jpg','jpeg','JPG','JPEG']
    for apath in pth:
        if apath != '':
            if apath.split('.')[-1] in ['jpg','jpeg','JPG','JPEG']:
                if apath in list(msgw.get(0,msgw.size()-1)):messagebox.showwarning('Warning','[WARN]:"' + apath+'" has been imported.')
                else:msgw.insert(tk.END,str(apath))
            else:messagebox.showwarning('Warning','[WARN]:"' + apath+'" is not JPEG file.')
window = tk.Tk()
window.title("File Packager")
window.geometry("840x630")
ph_open = tk.PhotoImage(file='./icon/open.png')
ph_del = tk.PhotoImage(file='./icon/del.png')
ph_pac = tk.PhotoImage(file='./icon/run.png')
ph_opt = tk.PhotoImage(file='./icon/opt.png')
tk.Label(window, text="File Packager",bd=10,font=('consolas',30)).pack()
scy = tk.Scrollbar(window)
scy.pack(side=tk.RIGHT,fill=tk.Y)
msgw = tk.Listbox(window,width=80,height=10,font=('consolas',20),relief='sunken',yscrollcommand=scy.set,selectmode=tk.EXTENDED)
msgw.pack()
scx = tk.Scrollbar(window,orient='horizontal')
scx.pack(fill=tk.X)
msgw.config(xscrollcommand=scx.set)
scy.config(command=msgw.yview)
scx.config(command=msgw.xview)
tk.Button(window,width=200,height=124,image=ph_open,relief='ridge',command=opfile).pack(side=tk.LEFT)
tk.Button(window,width=200,height=124,image=ph_del,relief='ridge',command=delete).pack(side=tk.LEFT)
tk.Button(window,width=200,height=124,image=ph_pac,relief='ridge',command=run).pack(side=tk.LEFT)
window.mainloop()