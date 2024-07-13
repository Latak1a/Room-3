import logging
import os

def percorso_log(name, log_file='app.log', level=logging.INFO):
    """
    Imposta un logger personalizzato.

    Args:
    - name (str): Il nome del logger.
    - log_file (str): Il file in cui scrivere i log.
    - level (int): Il livello di logging.
        
    Returns:
    - logger (logging.Logger): Il logger configurato.
    """
    log_directory = "Log"
    
    # Verifica se la cartella esiste, altrimenti la crea
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        
    log_path = os.path.join(log_directory, log_file)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    file_handler=logging.FileHandler(log_path)
    file_handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    console_handler=logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
          
    return logger
        