import folium
import exifread
import os
#read_map = geoip2.database.Reader('.\\GeoLite2-City.mmdb')
def open_html(pos,nm):
    m = folium.Map(location=pos[0],zoom_start=10,control_scale=True,max_zoom=35)
    for apos in pos:
        WE = round(apos[0],14)
        NS = round(apos[1],13)
        folium.Marker([WE,NS],popup='Some Other Location',icon=folium.Icon(icon='cloud')).add_to(m)
        folium.Circle(radius=150,location=[WE,NS],color='crimson',fill=True,fill_color='#fdbebe',fill_opacity=0.1).add_to(m)
    m.add_child(folium.LatLngPopup())
    m.add_child(folium.ClickForMarker())
    
    m.save('./pos/'+ nm + ".html")
def run(inp,nm):
    dirs = []
    for dir in inp:
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
        except:print('Error','[ERROR]:There is no position in "' + dir+'".')
    #NS,WE = check.Transform(NS,WE)
    if dirs != []:open_html(dirs,nm)
bgdir = './dir/'#这里路径一定要以'/'结尾
for apath in os.listdir(bgdir):
    if not('.' in apath):
        pthl = []
        for apth in os.listdir(bgdir + apath):
            if '.' in apth:
                if apth.split('.')[-1] in ['jpg','jpeg','JPG','JPEG']:
                    pthl.append(bgdir + apath + '/' + apth)
                else:print('Warning','[WARN]:"' + apth+'" is not JPEG file.')
        run(pthl,apath)
    else:
        if apath.split('.')[-1] in ['jpg','jpeg','JPG','JPEG']:
            run(bgdir + apath,apath.split('.')[0])
        else:print('Warning','[WARN]:"' + apath+'" is not JPEG file.')

