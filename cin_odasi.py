
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

nodes = {
    "Girdi": "Çince soru",
    "Analiz": "Sembolleri ayır",
    "Kural1": "Kural 1",
    "Kural2": "Kural 2",
    "Cevap": "Cevabı oluştur",
    "Cikti": "Çince cevap"
}

for node, label in nodes.items():
    G.add_node(node, label=label)

edges = [
    ("Girdi", "Analiz"),
    ("Analiz", "Kural1"),
    ("Analiz", "Kural2"),
    ("Kural1", "Cevap"),
    ("Kural2", "Cevap"),
    ("Cevap", "Cikti")
]

G.add_edges_from(edges)

pos = {
    "Girdi": (0, 2),
    "Analiz": (0, 1),
    "Kural1": (-1, 0),
    "Kural2": (1, 0),
    "Cevap": (0, -1),
    "Cikti": (0, -2)
}

labels = nx.get_node_attributes(G, "label")

nx.draw_networkx(
    G,
    pos,
    labels=labels,
    node_color="lightblue",
    node_size=3000,
    font_size=9,
    arrows=True,
    arrowsize=20
)

plt.title("Çin Odası - Yönlü Graf Modeli")
plt.axis("off")
plt.tight_layout()
plt.show()

print("Düğüm sayısı:", G.number_of_nodes())
print("Kenar sayısı:", G.number_of_edges())
print("Girdi-çıktı yolu:",
      nx.shortest_path(G, "Girdi", "Cikti"))
