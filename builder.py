import requests
import time

# Fonction pour envoyer le message à un webhook Discord
def envoyer_message_discord(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("succes check discord!")
    else:
        print("not succes not check")

# Fonction principale
def main():
    # Demander à l'utilisateur de saisir son webhook Discord
    webhook_url = input("enter you webhook: ")

    # Envoyer le message de spam
    while True:
        message = "d̵͇̫̪̒̈́͝i̸̼͖͔̓̕͝s̴̞͍͚͐̽̒c̵̪͎̽̔̽͜o̵̙͚͕͌͊h̴͍͕͒̐͜͝ä̴͖͎̺́̒c̵̡͉̙͒̈́̀k̵͇͉͕͛͠ https://discord.gg/sDUFGzpbmR"
        envoyer_message_discord(webhook_url, message)
        time.sleep(0)  # Attendre 1 seconde entre chaque envoi

if __name__ == "__main__":
    main()
