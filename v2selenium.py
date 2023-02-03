from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
import json
import datetime

fichier="sallesbien.csv"

driver=webdriver.Chrome(ChromeDriverManager().install())

section = "2022-STPI1"

ajd = datetime.datetime.now()
ajd=str(ajd)
ajd=ajd[:10]
lajd=ajd.split('-')
annee=lajd[0]
mois=lajd[1]
jour=lajd[2]
link = "http://agendas.insa-rouen.fr/2022/day.php?cal="+section+"&getdate="+annee+mois+jour

driver.get(link)

newsalles=0
sallesdujour=[]
salleslibresdujour=[]
Du=[]
Ma=[]
Bo=[]
Lh=[]
Da=[]
autresSalles=[]

h8lOccupe=[]
h9_45lOccupe=[]
h11_30lOccupe=[]
h13_15lOccupe=[]
h15lOccupe=[]
h16_45lOccupe=[]
h18_30lOccupe=[]
autresHeureslOccupe=[]

h8lLibre=[]
h9_45lLibre=[]
h11_30lLibre=[]
h13_15lLibre=[]
h15lLibre=[]
h16_45lLibre=[]
h18_30lLibre=[]
autresHeureslLibre=[]

h8d={'Magellanh8':[],'Dumonth8':[],'Lhh8':[],'Bougainvilleh8':[],'Darwinh8':[],'AutresSallesh8':[]}
h9_45d={'Magellanh9_45':[],'Dumonth9_45':[],'Lhh9_45':[],'Bougainvilleh9_45':[],'Darwinh9_45':[],'AutresSallesh9_45':[]}
h11_30d={'Magellanh11_30':[],'Dumonth11_30':[],'Lhh11_30':[],'Bougainvilleh11_30':[],'Darwinh11_30':[],'AutresSallesh11_30':[]}
h13_15d={'Magellanh13_15':[],'Dumonth13_15':[],'Lhh13_15':[],'Bougainvilleh13_15':[],'Darwinh13_15':[],'AutresSallesh13_15':[]}
h15d={'Magellanh15':[],'Dumonth15':[],'Lhh15':[],'Bougainvilleh15':[],'Darwinh15':[],'AutresSallesh15':[]}
h16_45d={'Magellanh16_45':[],'Dumonth16_45':[],'Lhh16_45':[],'Bougainvilleh16_45':[],'Darwinh16_45':[],'AutresSallesh16_45':[]}
h18_30d={'Magellanh18_30':[],'Dumonth18_30':[],'Lhh18_30':[],'Bougainvilleh18_30':[],'Darwinh18_30':[],'AutresSallesh18_30':[]}
#autresHeuresd={'Magellan':[],'Dumont':[],'Lh':[],'Bougainville':[],'Darwin':[],'AutresSalles':[]}

searchclassps = driver.find_elements(By.XPATH, "//a[@class='ps']")


for el in searchclassps:
    if "Location" in el.get_attribute("nicetitle"):
        txtnicetitle1=el.get_attribute('nicetitle')
        txtnicetitle2=txtnicetitle1
        txtnicetitle1 = txtnicetitle1[txtnicetitle1.index('Location')+10:]
        salle = txtnicetitle1[:txtnicetitle1.index('\n')]
        indicetab=txtnicetitle2.index('\n')
        h = txtnicetitle2[indicetab+1:indicetab+6]
        #print(txt)
        if len(salle)>=21:
            txts=list(salle.split(","))
            for x in txts:
                if x not in sallesdujour:
                    newsalles+=1
                    sallesdujour.append(x)
                    match h:
                        case '08:00' : h8lOccupe.append(salle)
                        case '09:45' : h9_45lOccupe.append(salle)
                        case '11:30' : h11_30lOccupe.append(salle)
                        case '13:15' : h13_15lOccupe.append(salle)
                        case '15:00' : h15lOccupe.append(salle)
                        case '16:45' : h16_45lOccupe.append(salle)
                        case '18:30' : h18_30lOccupe.append(salle)
                        case _: autresHeureslOccupe.append(salle)
        if (salle not in sallesdujour) and (len(salle)<21):
            newsalles+=1
            sallesdujour.append(salle)
            match h:
                case '08:00' : h8lOccupe.append(salle)
                case '09:45' : h9_45lOccupe.append(salle)
                case '11:30' : h11_30lOccupe.append(salle)
                case '13:15' : h13_15lOccupe.append(salle)
                case '15:00' : h15lOccupe.append(salle)
                case '16:45' : h16_45lOccupe.append(salle)
                case '18:30' : h18_30lOccupe.append(salle)
                case _: autresHeureslOccupe.append(salle)
            

#print(newsalles,"salles occupees aujourd hui : ",sallesdujour)

"""a reprendre ici"""
with open(fichier, "r") as f:
    reader=csv.reader(f)
    for line in reader:
        print(line[0] in h8lOccupe)
        if line[0] not in sallesdujour:
            salleslibresdujour.append(line[0])
        if line[0] not in h8lOccupe:
            h8lLibre.append(line[0])
        if line[0] not in h9_45lOccupe:
            h9_45lLibre.append(line[0])
        if line[0] not in h11_30lOccupe:
            h11_30lLibre.append(line[0])
        if line[0] not in h13_15lOccupe:
            h13_15lLibre.append(line[0])
        if line[0] not in h15lOccupe:
            h15lLibre.append(line[0])
        if line[0] not in h16_45lOccupe:
            h16_45lLibre.append(line[0])
        if line[0] not in h18_30lOccupe:
            h18_30lLibre.append(line[0])

for x in salleslibresdujour:
    if x.startswith('MA'):
            Ma.append(x)
    elif x.startswith('DU'):
            Du.append(x)
    elif x.startswith('LH'):
            Lh.append(x)
    elif x.startswith('BO'):
            Bo.append(x)
    elif x.startswith('DA'):
            Da.append(x)
    else:
        autresSalles.append(x)

for x in h8lLibre:
    if x.startswith('MA'):
        h8d['Magellanh8'].append(x)
    elif x.startswith('DU'):
        h8d['Dumonth8'].append(x)
    elif x.startswith('LH'):
        h8d['Lhh8'].append(x)
    elif x.startswith('BO'):
        h8d['Bougainvilleh8'].append(x)
    elif x.startswith('DA'):
        h8d['Darwinh8'].append(x)
    else:
        h8d['AutresSallesh8'].append(x)

for x in h9_45lLibre:
    if x.startswith('MA'):
        h9_45d['Magellanh9_45'].append(x)
    elif x.startswith('DU'):
        h9_45d['Dumonth9_45'].append(x)
    elif x.startswith('LH'):
        h9_45d['Lhh9_45'].append(x)
    elif x.startswith('BO'):
        h9_45d['Bougainvilleh9_45'].append(x)
    elif x.startswith('DA'):
        h9_45d['Darwinh9_45'].append(x)
    else:
        h9_45d['AutresSallesh9_45'].append(x)

for x in h11_30lLibre:
    if x.startswith('MA'):
        h11_30d['Magellanh11_30'].append(x)
    elif x.startswith('DU'):
        h11_30d['Dumonth11_30'].append(x)
    elif x.startswith('LH'):
        h11_30d['Lhh11_30'].append(x)
    elif x.startswith('BO'):
        h11_30d['Bougainvilleh11_30'].append(x)
    elif x.startswith('DA'):
        h11_30d['Darwinh11_30'].append(x)
    else:
        h11_30d['AutresSallesh11_30'].append(x)

for x in h13_15lLibre:
    if x.startswith('MA'):
        h13_15d['Magellanh13_15'].append(x)
    elif x.startswith('DU'):
        h13_15d['Dumonth13_15'].append(x)
    elif x.startswith('LH'):
        h13_15d['Lhh13_15'].append(x)
    elif x.startswith('BO'):
        h13_15d['Bougainvilleh13_15'].append(x)
    elif x.startswith('DA'):
        h13_15d['Darwinh13_15'].append(x)
    else:
        h13_15d['AutresSallesh13_15'].append(x)

for x in h15lLibre:
    if x.startswith('MA'):
        h15d['Magellanh15'].append(x)
    elif x.startswith('DU'):
        h15d['Dumonth15'].append(x)
    elif x.startswith('LH'):
        h15d['Lhh15'].append(x)
    elif x.startswith('BO'):
        h15d['Bougainvilleh15'].append(x)
    elif x.startswith('DA'):
        h15d['Darwinh15'].append(x)
    else:
        h15d['AutresSallesh15'].append(x)

for x in h16_45lLibre:
    if x.startswith('MA'):
        h16_45d['Magellanh16_45'].append(x)
    elif x.startswith('DU'):
        h16_45d['Dumonth16_45'].append(x)
    elif x.startswith('LH'):
        h16_45d['Lhh16_45'].append(x)
    elif x.startswith('BO'):
        h16_45d['Bougainvilleh16_45'].append(x)
    elif x.startswith('DA'):
        h16_45d['Darwinh16_45'].append(x)
    else:
        h16_45d['AutresSallesh16_45'].append(x)

for x in h18_30lLibre:
    if x.startswith('MA'):
        h18_30d['Magellanh18_30'].append(x)
    elif x.startswith('DU'):
        h18_30d['Dumonth18_30'].append(x)
    elif x.startswith('LH'):
        h18_30d['Lhh18_30'].append(x)
    elif x.startswith('BO'):
        h18_30d['Bougainvilleh18_30'].append(x)
    elif x.startswith('DA'):
        h18_30d['Darwinh18_30'].append(x)
    else:
        h18_30d['AutresSallesh18_30'].append(x)

Ma = list(set(Ma))
Du = list(set(Du))
Lh = list(set(Lh))
Bo = list(set(Bo))
Da = list(set(Da))
autresSalles = list(set(autresSalles))

Ma.sort()
Du.sort()
Lh.sort()
Bo.sort()
Da.sort()
autresSalles.sort()

h8d['Magellanh8'].sort()
h8d['Dumonth8'].sort()
h8d['Lhh8'].sort()
h8d['Bougainvilleh8'].sort()
h8d['Darwinh8'].sort()
h8d['AutresSallesh8'].sort()

h9_45d['Magellanh9_45'].sort()
h9_45d['Dumonth9_45'].sort()
h9_45d['Lhh9_45'].sort()
h9_45d['Bougainvilleh9_45'].sort()
h9_45d['Darwinh9_45'].sort()
h9_45d['AutresSallesh9_45'].sort()

h11_30d['Magellanh11_30'].sort()
h11_30d['Dumonth11_30'].sort()
h11_30d['Lhh11_30'].sort()
h11_30d['Bougainvilleh11_30'].sort()
h11_30d['Darwinh11_30'].sort()
h11_30d['AutresSallesh11_30'].sort()

h13_15d['Magellanh13_15'].sort()
h13_15d['Dumonth13_15'].sort()
h13_15d['Lhh13_15'].sort()
h13_15d['Bougainvilleh13_15'].sort()
h13_15d['Darwinh13_15'].sort()
h13_15d['AutresSallesh13_15'].sort()

h15d['Magellanh15'].sort()
h15d['Dumonth15'].sort()
h15d['Lhh15'].sort()
h15d['Bougainvilleh15'].sort()
h15d['Darwinh15'].sort()
h15d['AutresSallesh15'].sort()

h16_45d['Magellanh16_45'].sort()
h16_45d['Dumonth16_45'].sort()
h16_45d['Lhh16_45'].sort()
h16_45d['Bougainvilleh16_45'].sort()
h16_45d['Darwinh16_45'].sort()
h16_45d['AutresSallesh16_45'].sort()

h18_30d['Magellanh18_30'].sort()
h18_30d['Dumonth18_30'].sort()
h18_30d['Lhh18_30'].sort()
h18_30d['Bougainvilleh18_30'].sort()
h18_30d['Darwinh18_30'].sort()
h18_30d['AutresSallesh18_30'].sort()

if len(h8d['AutresSallesh8'])==0:
    h8d['AutresSallesh8'].append('Pas d\'autres salles')
if len(h9_45d['AutresSallesh9_45'])==0:
    h9_45d['AutresSallesh9_45'].append('Pas d\'autres salles')
if len(h11_30d['AutresSallesh11_30'])==0:
    h11_30d['AutresSallesh11_30'].append('Pas d\'autres salles')
if len(h13_15d['AutresSallesh13_15'])==0:
    h13_15d['AutresSallesh13_15'].append('Pas d\'autres salles')
if len(h15d['AutresSallesh15'])==0:
    h15d['AutresSallesh15'].append('Pas d\'autres salles')
if len(h16_45d['AutresSallesh16_45'])==0:
    h16_45d['AutresSallesh16_45'].append('Pas d\'autres salles')
if len(h18_30d['AutresSallesh18_30'])==0:
    h18_30d['AutresSallesh18_30'].append('Pas d\'autres salles')

"""
print((len(Ma)+len(Du)+len(Lh)+len(Bo)+len(Da)+len(autresSalles)),'salles libres aujourd hui')

print(len(Ma),"salles libres a Magellan : ", Ma)
print(len(Du),"salles libres a Dumont Durville : ", Du)
print(len(Lh),"salles libres a LH : ", Lh)
print(len(Bo),"salles libres a Bougainville : ", Bo)
print(len(Da),"salles libres a Darwin : ", Da)
print(len(autresSalles),"autres salles libres : ", autresSalles)"""

print('8h : ',h8d)
print('\n')
print('\n')
print('9h45 : ',h9_45d)
print('\n')
print('\n')
print('11h30 : ',h11_30d)
print('\n')
print('\n')
print('13h15 : ',h13_15d)
print('\n')
print('\n')
print('15h : ',h15d)
print('\n')
print('\n')
print('16h45 : ',h16_45d)
print('\n')
print('\n')
print('18h30 : ',h18_30d)


json_h8d = json.dumps(h8d, indent = 4)
json_h9_45d = json.dumps(h9_45d, indent = 4)
json_h11_30d = json.dumps(h11_30d, indent = 4)
json_h13_15d = json.dumps(h13_15d, indent = 4)
json_h15d = json.dumps(h15d, indent = 4)
json_h16_45d = json.dumps(h16_45d, indent = 4)
json_h18_30d = json.dumps(h18_30d, indent = 4)


json_file=open('listesalles.json', 'w')
json_file.write('{')
json_file.write('\n')

json_file.write('\"h8\" : ')
json_file.write(json_h8d)
json_file.write(',')
json_file.write('\n')
json_file.write('\n')

json_file.write('\"h9_45\" : ')
json_file.write(json_h9_45d)
json_file.write(',')
json_file.write('\n')
json_file.write('\n')

json_file.write('\"h11_30\" : ')
json_file.write(json_h11_30d)
json_file.write(',')
json_file.write('\n')
json_file.write('\n')

json_file.write('\"h13_15\" : ')
json_file.write(json_h13_15d)
json_file.write(',')
json_file.write('\n')
json_file.write('\n')

json_file.write('\"h15\" : ')
json_file.write(json_h15d)
json_file.write(',')
json_file.write('\n')
json_file.write('\n')

json_file.write('\"h16_45\" : ')
json_file.write(json_h16_45d)
json_file.write(',')
json_file.write('\n')
json_file.write('\n')

json_file.write('\"h18_30\" : ')
json_file.write(json_h18_30d)
json_file.write('}')
json_file.close()


driver.close()