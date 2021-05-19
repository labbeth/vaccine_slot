#! python3
import bs4, requests, smtplib, json
from datetime import date

toAddress = ['your_email@gmail.com']
urlSite = 'https://www.doctolib.fr/centre-de-vaccinations-internationales/rennes/centre-de-vaccination-covid-19-rennes-liberte?pid=practice-164684'
startDate = date.today()
visitMotiveId = '2548527' # type d'injection (par défaut 1ère injection Pfizer)
agendaId = '429575-449554-417726-473602-473601-473600-417731-473604-471900-410821-436811-436809-410820-410823-417727-417728-417725-436265-429639-436810-472886' # id de l'agenda (à récupérer depuis les traces réseaux)
practiceId = '164684' # id du centre de vaccination
daysLimit = 10

getPage = requests.get('https://www.doctolib.fr/availabilities.json?start_date=%s&visit_motive_ids=%s&agenda_ids=%s&insurance_sector=public&practice_ids=%s&destroy_temporary=true&limit=%s' % (startDate, visitMotiveId, agendaId, practiceId, daysLimit))
getPage.raise_for_status()

calendar = bs4.BeautifulSoup(getPage.text, 'html.parser')
calendar_json=json.loads(calendar.text)
slot_dispo = [d.get('slots') for d in calendar_json['availabilities'] if d.get('slots')]

if slot_dispo:
    conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('your_email@gmail.com', 'your app key')
    conn.sendmail('your_email@gmail.com', toAddress, 'Subject: Slots disponibles !\n\n%s\n\n%s' % (urlSite, slot_dispo))
    conn.quit()
    print('Sent notificaton e-mails for the following recipients:\n')
    for i in range(len(toAddress)):
        print(toAddress[i])
    print('')
else:
    print('Pas de slots actuellement')