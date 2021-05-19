# Vaccine Slot Tracker

This script aims at providing automatic email notifications when vaccine slots are available for a given vaccine center.

## Requirements
- Python 3.6+
- A gmail account
- Windows computer (could be adapted for Mac and Linux though)

Launch cmd and install the following librairies:

```python
pip install beautifulsoup4
pip install requests
```

## Starting

1. Go to the url of your target vaccine center and display network traces with a developer tool. Select the target "Motif de consultation", and retrieve the associated url starting with https://www.doctolib.fr/availabilities.json

![image](https://github.com/labbeth/vaccine_slot/blob/fba129ab02d0395d2f86fa8659073b48861c9aef/media/availabilites.png)

2. Copy the vaccine_slot.py script in a given folder and edit the values retrieved from the previous step:

```python
toAddress = ['your_email@gmail.com'] # Could be a non-gmail adress
urlSite = 'public url of your vaccine center'
visitMotiveId = 'value of visit_motive_ids' 
agendaId = 'value of agenda_ids' 
practiceId = 'value of practice_ids'
daysLimit = 20 # choose the period you want to cover in [1;20]
```

2. Update the following lines with your personal data:

```python
conn.login('your_email@gmail.com', 'your app key')
conn.sendmail('your_email@gmail.com', toAddress, 'Subject: Slots disponibles !\n\n%s\n\n%s' % (urlSite, slot_dispo))
```

Your mail app key could be retrieve at https://myaccount.google.com/security by selecting "applications password" menu

4. Edit the slot_notifier.bat file and replace the script path C:\your_path\vaccine_slot.py

5. Open Windows "Task Scheduler" (Planificateur de tâches) and add the task associated to the .bat file
6. Open 
7. 
