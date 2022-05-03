import ccxt


access = 'Fofo123nKyvG7b1vHS4dxExFHsszf0ZEDgG5mFhGfGp37MpvvNe5qc6IOMyHAozJ'
secret = 'lt4qHHwGHb2sJhfYe84u6F8DzjWfnPv8KP4z4nBYW1mgB7adTmDD8trpB2Su59Zo'

binance = ccxt.binance(config={
    'apiKey' : access,
    'secret' : secret,
    'enableRateLimit' : True,
    'options' : {
        'defaultType' : 'future'
    }
})