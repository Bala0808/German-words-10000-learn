


a_dic = {
    #row 1
    'Hallo' : 'Hello',
    'Guten Morgen':'Good morning',
    'Guten tag' : 'wishes',
    'Guten Abend':'Good evening',
    'Guten Nacht':'Good night ',
    #row 2
    'Danke':'Thank you',
    'Nein':'No',
    'Lecker':'Delicious',
    'Auf Wiedersehen':'Goodbye',
    'Ja':'Yes',
    #row 3
    'Woche':'week',
    'Jahr':'year',
    'Heute':'today',
    'Morgen':'tomorrow',
    'Gestern':'yesterday',
    #row 4
    'Kaleder':'calender',
    'Sekunde':'second',
    'Stunde':'hour',
    'Minute':'minute',
    'Uhr':'o'"'"'clock, clock',
    #row 4
    '':'',
    '':'',
    '':'',
    '':'',
    '':''

}

for key, value in a_dic.items():
    print("<td><button id="+'"'+key+'"'+">"+key+"</button> <div id="'"'"word"+value+'"'"> </div> <script>document.getElementById("+'"'+value+'"'+").onclick = function (){document.getElementById("'"'"word"+value+'"'").innerHTML = "+'"'+value+'"'+"}</script></td>") 


    