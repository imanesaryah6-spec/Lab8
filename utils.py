def moyenne(liste):
    if not liste:
        return 0
    return sum(liste) / len(liste)

VERSION = "1.0.0"
__all__ = ['moyenne', 'VERSION']
