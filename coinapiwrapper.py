import json
from typing import List
import requests
from pprint import pprint
from json import JSONDecoder
import time, getpass
import pathlib
import webbrowser

# COINAPI key
key = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"

def timer():
    local_time = time.localtime()
    parsed_time = f'{local_time.tm_mday}/{local_time.tm_mon}/{local_time.tm_year} {local_time.tm_hour}:{local_time.tm_min}:{local_time.tm_sec} >'
    return parsed_time

def command_list () :
    commands = f'''
    | {timer()} Ecco la lista dei comandi:
    | > cmd - Mostra la lista dei comandi.
    | > all - Richiedi la lista delle criptovalute a disposizione.
    | > fetch <COIN-ID> - Richiedi le informazioni sulla criptovaluta indicata.
    | > write <COIN-ID> <PATH=cwd> - Scrivi le info della crito indicata su file (default current working dir)
    | > apikey - Mostra la api key verso COINAPI
    | > webme - Apri COINAPI sul default browser
    | > exit - Esci dall'applicazione
    '''
    print(commands)

def all ():
    r = requests.get(f"https://rest.coinapi.io/v1/exchanges",params={"apikey":key})
    query = r.content.decode("utf-8")
    p = JSONDecoder().decode(query)

    print(f'''
    | {timer()} Cripto disponibili per la query: 
    | COIN-ID\tNOME\tWEBSITE
    ''')
    for n in p:
        print(f'    | > {n["exchange_id"]}\t\t{n["name"]}\t\t{n["website"]}')
    print("")
    r.close()

def exitfunc ():
    print(f'| {timer()} Sto chiudendo la connessione.')
    print(f"| {timer()} Arrivederci.")
    quit()

def apikey () :
    print(f'''
    | La chiave di connessione è: {key}
    | Per sostituire la chiave prova apikey -c <NEW_API_KEY>
    ''')

def apikey_change():
    global key
    old_key = key
    key = stdin.strip("apikey -c ")
    if requests.get("https://rest.coinapi.io/v1/exchanges",params={"apikey":key}).status_code != 200:
        print(f'''
    | Qualcosa è andato storto. Controlla la chiave o procurati una chiave valida!''')
        key = old_key
    else:
        print(f'''
    !!! 200. Chiave cambiata per la sessione corrente! !!!
    ''')

def fetch (coin_id):
    global key
    try:
        query = requests.get(f"https://rest.coinapi.io/v1/assets?filter_asset_id={coin_id}",params={"apikey":key})
        q = query.content.decode("utf-8")
        a = JSONDecoder().decode(q)
        for f in a[0]:
            print(f'    | - {f}:  {a[0][f]}')
        print("")
        query.close()
    except IndexError as indexerror:
        print(f'''
    | Non ho trovato niente per l'ID {coin_id}!
    ''')
    except Exception as error:
        print(f'''
    |Ops, qualcosa nella richiesta è andato storto! Erore: {error}
        ''')

def write (coin_id):
    path = pathlib.Path().home()
    print(f'''
    | Scrivo in: {path}
    ''')
    query = requests.get(f"https://rest.coinapi.io/v1/assets?filter_asset_id={coin_id}",params={"apikey":key})
    q = query.content.decode("utf-8")
    a = JSONDecoder().decode(q)
    with open(f'{coin_id}.json','w') as file:
        json.dump(a,file,indent=4)

def webme (coin_id):
    r = requests.get(f"https://rest.coinapi.io/v1/exchanges",params={"apikey":key})
    query = r.content.decode("utf-8")
    p = JSONDecoder().decode(query)

    for coin in p:
        if coin_id == coin["exchange_id"]:
            print(f'''
    | Apro il sito: {coin["website"]}
            ''')
            webbrowser.open(coin["website"])
            break

if __name__ == "__main__":
    print("\n")
    print("    | ----------------------------------------------------------------------------------------------- |")
    print(f'''    | {timer()} Benvenuto {getpass.getuser()}.
    |
    | {timer()} Ecco la lista dei comandi:
    | > cmd - Mostra la lista dei comandi.
    | > all - Richiedi la lista delle criptovalute a disposizione.
    | > fetch <COIN-ID> - Richiedi le informazioni sulla criptovaluta indicata.
    | > write <COIN-ID> - Scrivi le info della crito indicata su file (default current working dir)
    | > apikey - Mostra la api key verso COINAPI
    | > webme <COIN-ID> - Apri il sito della moneta sul default browser
    | > exit - Esci dall'applicazione
    ''')

    while True:

        stdin = input(" > ")

        if stdin == "exit":
            exitfunc()
        elif stdin == "cmd":
            command_list()
        elif stdin == "all":
            all()
        elif stdin == "apikey":
            apikey()
        elif "apikey -c " in stdin:
            apikey_change()
        elif "fetch" in stdin:
            fetch(stdin.strip("fetch "))
        elif "write" in stdin:
            write(stdin.strip("write "))
        elif "webme" in stdin:
            webme(stdin.strip("webme "))
        else:
            print(f'''
    | Il comando {stdin} non è disponibile.
    | Scrivi 'cmd' per vedere la lista dei comandi disponibili.
    ''')
