# CoinAPI - Wrapper

![Screenshot_20210628_003131](https://user-images.githubusercontent.com/51529905/123561372-4bbbab80-d7a8-11eb-97f7-fa0957944982.png)

Un semplice tool per scaricare dati da [CoinAPI](https://www.coinapi.io/), con una semplice interfaccia CLI a comandi preimpostati.
Hai bisogno di una chiave da connessione ottenibile da Coin API per utilizzare questo strumento.

## Manuale
Questo wrapper si basa sulla seguente serie di comandi preimpostati:

### > cmd
```
> cmd
```
Mostra la lista dei comandi disponibili.

### > all
```
> all
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
