def modus_ponens(P, P_implica_Q):
    if P and P_implica_Q:
        return True
    return False

# Ejemplo
tiene_fiebre = True
fiebre_implica_enfermedad = True

if modus_ponens(tiene_fiebre, fiebre_implica_enfermedad):
    print("Conclusión: La persona está enferma.")
else:
    print("No se puede concluir nada.")