def modus_tollens(Q, P_implica_Q):
    if not Q and P_implica_Q:
        return False  # Se niega P
    return True  # No se puede concluir nada

# Ejemplo
suelo_mojado = False
lluvia_implica_suelo_mojado = True

if not modus_tollens(suelo_mojado, lluvia_implica_suelo_mojado):
    print("Conclusión: No ha llovido.")
else:
    print("No se puede concluir nada.")