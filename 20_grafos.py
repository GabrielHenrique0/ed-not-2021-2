# Usando a estrurura dict nativa do Python
# para representar um grafo não direccionado
# refletindo sua matriz de adjacência
grafo_naodir = {
    'A': ['A', 'B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}