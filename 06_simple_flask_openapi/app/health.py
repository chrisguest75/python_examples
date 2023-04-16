from connexion import NoContent
import logging

def dependency_check():
    logger = logging.getLogger()
    logger.info("Checking dependencies")
    return True

def health():
    if dependency_check():
        return "Healthy", 200        
    else:
        return "Unhealthy", 503            
