import pandas as pd
import yagmail
import yaml
import time

interval = 10
last_sent = 0
check = 0
subject = ""
contents = ""
while True:
    try:
        print("lecture du fichier configuration...\n")
        with open("options.yaml","r") as file:
            options = yaml.safe_load(file)
        print("lecture complet.\n")
        print("accès aux données...\n")
        data = pd.read_csv('measurements.csv', parse_dates=['date'])
        print("données enregistrés.\n")

        if options["choiceTemp"] == ">":

            if data.loc[data.index[-1],options["tempVar"]] >= options["thresholdTemp"]:
                now = time.time()
                if now - last_sent > options["cooldown"]:
                    print("Seuil température dépassé, envoi de notification en cours...\n")
                    check = 1
                    subject += options["tempVar"] + " "
                    contents += f"<b>Attention! La température est supérieure au seuil de {options['thresholdTemp']}°C ! Température actuelle : {data.loc[data.index[-1],options['tempVar']]}°C</b>" + f"\nMessage sur la température:\n{options['msgTemp']}\n\n"
        elif options["choiceTemp"] == "<":

            if data.loc[data.index[-1],options["tempVar"]] <= options["thresholdTemp"]:
                now = time.time()
                if now - last_sent > options["cooldown"]:
                    print("Seuil température dépassé, envoi de notification en cours...\n")
                    check = 1
                    subject += options["tempVar"] + " "
                    contents += f"<b>Attention! La température est inférieure au seuil de {options['thresholdTemp']}°C ! Température actuelle : {data.loc[data.index[-1],options['tempVar']]}°C</b>" + f"\nMessage sur la température:\n{options['msgTemp']}\n\n"
    
        if options["choiceHum"] == ">":

            if data.loc[data.index[-1],options["humVar"]] >= options["thresholdHum"]:
                now = time.time()
                if now - last_sent > options["cooldown"]:
                    print("Seuil humidité dépassé, envoi de notification en cours...\n")
                    check = 1
                    subject += options["humVar"] + " "
                    contents += f"<b>Attention! L'humidité est supérieure au seuil de {options['thresholdHum']}% ! Humidité actuelle : {data.loc[data.index[-1],options['humVar']]}%</b>" + f"\nMessage sur l'humidité :\n{options['msgHum']}\n\n"
        
        elif options["choiceHum"] == "<":

            if data.loc[data.index[-1],options["humVar"]] <= options["thresholdHum"]:
                now = time.time()
                if now - last_sent > options["cooldown"]:
                    print("Seuil humidité dépassé, envoi de notification en cours...\n")
                    check = 1
                    subject += options["humVar"] + " "
                    contents += f"<b>Attention! La température est inférieure au seuil de {options['thresholdHum']}% ! Humidité actuelle : {data.loc[data.index[-1],options['humVar']]}%</b>" + f"\nMessage sur l'humidité :\n{options['msgHum']}\n\n"

        if check == 1:
            yag = yagmail.SMTP('temp.squad101','euby kcfa ravt obyu')
            yag.send(options["email"],f"Seuil dépassé : {subject}", contents)
            print("Courriel envoyé!\n")
            contents = ""
            check = 0
            subject = ""
    except:
        print("erreur. nouvelle tentative...\n")
        contents = ""
        check = 0
        subject = ""

    time.sleep(interval)

