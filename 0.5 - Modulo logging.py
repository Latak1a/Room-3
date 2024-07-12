import logging

# 1. configura il logger (le impostazioni del logger)
logging.basicConfig(level = logging.ERROR, format = '%(asctime)s - %(levelname)s - %(message)s')
# i livelli di severità (dal meno al più severo) sono:
# - DEBUG: per tutti i messaggi da visualizzare SOLO in fase di test/debug
# - INFO: per tutti i messaggi da visualizzare in fase di normale funzionamento del codice
# - WARNING: per tutti i messaggi da visualizzare in caso di un warning
# - ERROR: per tutti i messaggi da visualizzare in caso di errore (non fatale)
# - CRITICAL: per tutti i messaggi da visualizzare in caso di errore fatale

# debug: Registra un messaggio di debug
logging.debug('Questo è un messaggio di debug.')

# info: Registra un messaggio informativo
logging.info('Questo è un messaggio di info.')

# warning: Registra un avvertimento
logging.warning('Questo è un avvertimento.')
# Registra un messaggio con livello di gravità WARNING. Utilizzato per indicare che qualcosa di inaspettato è successo o potrebbe succedere.

# error: Registra un errore
logging.error('Questo è un errore.')
# Registra un messaggio con livello di gravità ERROR. Utilizzato per errori gravi che hanno causato problemi nel programma.

# critical: Registra un messaggio critico
logging.critical('Questo è un messaggio critico.')
# Registra un messaggio con livello di gravità CRITICAL. Utilizzato per errori molto gravi che potrebbero impedire l'esecuzione del programma.


# Costruisco un logger personalizzato
logger_personalizzato = logging.getLogger('logger personalizzato')
logger_personalizzato.setLevel(logging.WARNING)


# Specifico dove verranno salvati i messaggi di log del mio logger personalizzato
file_handler = logging.FileHandler('app.log')

# Specifico il formato dei messaggi
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Specifico che tutti i messaggi che verranno registrati dal Logger 'logger_personalizzato' saranno scritti sul file 'app.log'
logger_personalizzato.addHandler(file_handler)

# Registro un messaggio di warning sul logger personalizzato
logger_personalizzato.warning("Questo è uno specifico messaggio di warning registrato dal Logger 'logger_personalizzato'")

