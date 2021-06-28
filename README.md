# CoinAPI - Wrapper

![Screenshot_20210628_003131](https://user-images.githubusercontent.com/51529905/123561372-4bbbab80-d7a8-11eb-97f7-fa0957944982.png)

Un semplice tool per scaricare dati da [CoinAPI](https://www.coinapi.io/), con una semplice interfaccia CLI a comandi preimpostati.
Hai bisogno di una chiave da connessione ottenibile da Coin API per utilizzare questo strumento.

## Manuale
Questo wrapper si basa sulla seguente serie di comandi preimpostati:

### > cmd
```
> cmd
    | 28/6/2021 0:49:17 > Ecco la lista dei comandi:
    | > cmd - Mostra la lista dei comandi.
    | > all - Richiedi la lista delle criptovalute a disposizione.
    | > fetch <COIN-ID> - Richiedi le informazioni sulla criptovaluta indicata.
    | > write <COIN-ID> <PATH=cwd> - Scrivi le info della crito indicata su file (default current working dir)
    | > apikey - Mostra la api key verso COINAPI
    | > webme - Apri COINAPI sul default browser
    | > exit - Esci dall'applicazione
```
Mostra la lista dei comandi disponibili.

### > all
```
> all
| 28/6/2021 0:49:37 > Cripto disponibili per la query: 
    | COIN-ID   NOME    WEBSITE
    
    | > ECB             European Central Bank           https://www.ecb.europa.eu/
    | > BINANCE         Binance         https://www.binance.com/
    | > KRAKEN          Kraken          https://www.kraken.com/
    | > COINBASE                Coinbase Pro (GDAX)             https://pro.coinbase.com/
    | > BITSTAMP                Bitstamp Ltd.           https://www.bitstamp.net/
    | > GEMINI          Gemini          https://gemini.com/
    | > LMAXDIGITAL             LMAX Digital            https://www.lmaxdigital.com/
    | > OKCOINCNY               OKCoin CNY              https://www.okcoin.cn/
    | > HUOBI           Huobi (HBUS)            https://www.huobi.us/
    | > BITTREX         Bittrex         https://bittrex.com/
    | > POLONIEX                POLONIEX                https://poloniex.com/
    | > BITFINEX                Bitfinex    ...
    ...
```
Mostra la lista delle coin disponibili presso l'API di CoinAPI.

### > fetch [COIN-ID]
```
> fetch BTC
    | - asset_id:  BTC
    | - name:  Bitcoin
    | - type_is_crypto:  1
    | - data_start:  2010-07-17
    | - data_end:  2021-06-27
    | - data_quote_start:  2014-02-24T17:43:05.0000000Z
    | - data_quote_end:  2021-06-27T22:31:04.4713816Z
    | - data_orderbook_start:  2014-02-24T17:43:05.0000000Z
    | - data_orderbook_end:  2020-08-05T14:38:38.3413202Z
    | - data_trade_start:  2010-07-17T23:09:17.0000000Z
    | - data_trade_end:  2021-06-27T22:32:41.1860000Z
    | - data_symbols_count:  57781
    | - volume_1hrs_usd:  16252752683443.84
    | - volume_1day_usd:  849766029184906.2
    | - volume_1mth_usd:  5.681640538966346e+16
    | - price_usd:  34202.08664405485
    | - id_icon:  4caf2b16-a017-4e26-a348-2cea69c34cba
```
Richiede a CoinAPI le informazioni disponibili sulla coin indicata.

### > write [COIN-ID]
```
> write BTC
```
Crea un file json con i dati raccolti nella cartella attuale.

### > apikey
```
> apikey
| La chiave di connessione è: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
| Per sostituire la chiave prova apikey -c <NEW_API_KEY>
```
Mostra la chiave per la connnessione a CoinAPi. Per sostituire la chiave per la sessione corrente, utilizzare il comando:
```
> apikey -c YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYYYYY
!!! 200. Chiave cambiata per la sessione corrente! !!!
```

### > webme [COIN-ID]
```
> webme BTC
| Apro il sito: www.bitcoint.org
```
Apre il browser verso il sito web della criptovaluta.

### > exit
```
> exit
| Sto chiudendo la connessione.
| Arrivederci.
```
Chiude l'applicazione.
