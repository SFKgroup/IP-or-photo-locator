#IP地址定位
import folium
import webbrowser
import geoip2.database
import tkinter as tk
import tkinter.ttk
read_map = geoip2.database.Reader('.\\GeoLite2-City.mmdb')
def open_html(WE,NS):
    print(NS)
    print(WE)
    #m = folium.Map(location=[WE, NS],zoom_start=13)
    m = folium.Map(location=[WE,NS],zoom_start=10,control_scale=True,max_zoom=35)
    #--------------------------------------------------------------------------------------------------------------------
    folium.Marker([WE,NS],popup='Some Other Location',icon=folium.Icon(icon='cloud')).add_to(m)
    folium.Circle(radius=15000,location=[WE,NS],color='crimson',fill=True,fill_color='#fdbebe',fill_opacity=0.05).add_to(m)
    folium.Circle(radius=10000,location=[WE,NS],color='crimson',fill=True,fill_color='#fdbebe',fill_opacity=0.1).add_to(m)
    folium.Circle(radius=5000 ,location=[WE,NS],color='crimson',fill=True,fill_color='#fdbebe',fill_opacity=0.15).add_to(m)
    m.add_child(folium.LatLngPopup())
    m.add_child(folium.ClickForMarker())
    #--------------------------------------------------------------------------------------------------------------------
    m.save("IP.html")
    webbrowser.open("IP.html") #重新打开HTML网页
def find(ip):
    # 载入指定IP相关数据
    response = read_map.city(ip)
    #读取国家代码
    Country_IsoCode = response.country.iso_code
    #读取国家名称
    Country_Name = response.country.name
    #读取国家名称(中文显示)
    Country_NameCN = response.country.names['zh-CN']
    #读取州(国外)/省(国内)名称
    Country_SpecificName = response.subdivisions.most_specific.name
    #读取州(国外)/省(国内)代码
    Country_SpecificIsoCode = response.subdivisions.most_specific.iso_code
    #读取城市名称
    City_Name = response.city.name
    #读取邮政编码
    City_PostalCode = response.postal.code
    #获取纬度
    Location_Latitude = response.location.latitude
    #获取经度
    Location_Longitude = response.location.longitude

    open_html(Location_Latitude,Location_Longitude)

    if Country_IsoCode != None:
        print('Country_IsoCode        : ' + Country_IsoCode)
    if Country_Name != None:
        print('Country_Name           : ' + Country_Name)
    if Country_NameCN != None:
        print('Country_NameCN         : ' + Country_NameCN)
    if Country_SpecificName != None:
        print('Country_SpecificName   : ' + Country_SpecificName)
    if Country_SpecificIsoCode != None:
        print('Country_SpecificIsoCode: ' + Country_SpecificIsoCode)
    if City_Name != None:
        print('City_Name              : ' + City_Name)
    if City_PostalCode != None:
        print('City_PostalCode        : ' + City_PostalCode)
    #print('Location_Latitude      : ' + str(Location_Latitude))
    #print('Location_Longitude     : ' + str(Location_Longitude))
    
def run():
    try:ip = str(ip1.get()) + '.' + str(ip2.get()) + '.' + str(ip3.get()) + '.' + str(ip4.get())
    except:
        ttitle.set('IP Find:Input error.')
        tt.config(fg='#ff0000')
        root.update()
    if ip != '':
        try:
            find(ip)
            ttitle.set('IP Find:Done.')
            tt.config(fg='#00ff00')
            root.update()
        except:
            ttitle.set('IP Find:IP not found.')
            tt.config(fg='#ff0000')
            root.update()
        ip1.set(0)
        ip2.set(0)
        ip3.set(0)
        ip4.set(0)

root = tk.Tk()
root.title('IP Find')
root.geometry('400x100')
root.iconbitmap('./icon/favicon.ico')
ttitle = tk.StringVar()
ttitle.set('IP Find')
tt = tk.Label(root, textvariable=ttitle,bd=5,font=('consolas',30))
tt.pack(side=tk.TOP)
ip1 = tk.IntVar()
tk.Label(root, text="IP:",bd=5,font=('consolas',20)).pack(side=tk.LEFT)
ipentry1=tk.Entry(root,textvariable=ip1,font=('consolas',20), width = 3)
ipentry1.pack(side=tk.LEFT)
ip2 = tk.IntVar()
tk.Label(root, text=".",bd=5,font=('consolas',20)).pack(side=tk.LEFT)
ipentry2=tk.Entry(root,textvariable=ip2,font=('consolas',20), width = 3)
ipentry2.pack(side=tk.LEFT)
ip3 = tk.IntVar()
tk.Label(root, text=".",bd=5,font=('consolas',20)).pack(side=tk.LEFT)
ipentry3=tk.Entry(root,textvariable=ip3,font=('consolas',20), width = 3)
ipentry3.pack(side=tk.LEFT)
ip4 = tk.IntVar()
tk.Label(root, text=".",bd=5,font=('consolas',20)).pack(side=tk.LEFT)
ipentry4=tk.Entry(root,textvariable=ip4,font=('consolas',20), width = 3)
ipentry4.pack(side=tk.LEFT)
tk.Button(root,text='Find',command=run,width=14).pack(side=tk.LEFT)
root.mainloop()