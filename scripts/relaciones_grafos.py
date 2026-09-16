import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NODE_R = 0.18
FS = 13


def nodo(ax, pos, nombre):
    circ = plt.Circle(pos, NODE_R, facecolor="#dbeafe", edgecolor="#2563eb",
                       linewidth=1.6, zorder=3)
    ax.add_patch(circ)
    ax.text(pos[0], pos[1], nombre, ha="center", va="center",
            fontsize=FS, zorder=4)


def arista(ax, p, q, color="#334155", estilo="-"):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, linewidth=1.8,
            linestyle=estilo, zorder=2)


def panel(ax, titulo):
    ax.set_xlim(-0.6, 3.6)
    ax.set_ylim(-0.6, 2.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(titulo, fontsize=13)


# --- complemento -------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(6, 3.2))
pos = {"1": (0, 2), "2": (1.5, 2), "3": (1.5, 0), "4": (0, 0)}

panel(axs[0], "G")
for a, b in [("1", "2"), ("2", "3"), ("3", "4")]:
    arista(axs[0], pos[a], pos[b])
for n, p in pos.items():
    nodo(axs[0], p, n)

panel(axs[1], "complemento de G")
for a, b in [("1", "3"), ("1", "4"), ("2", "4")]:
    arista(axs[1], pos[a], pos[b], color="#dc2626")
for n, p in pos.items():
    nodo(axs[1], p, n)

fig.tight_layout()
fig.savefig("imagenes/complemento.png", dpi=100)
plt.close(fig)

# --- union disjunta ------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 2.6))
panel(ax, "G ∪ H  (unión disjunta)")
posU = {"a": (0.3, 1.6), "b": (0.3, 0.4), "c": (2.6, 1.6), "d": (2.6, 0.4)}
arista(ax, posU["a"], posU["b"])
arista(ax, posU["c"], posU["d"])
for n, p in posU.items():
    nodo(ax, p, n)
ax.text(0.3, 2.15, "G", ha="center", fontsize=12, color="#475569")
ax.text(2.6, 2.15, "H", ha="center", fontsize=12, color="#475569")
fig.tight_layout()
fig.savefig("imagenes/union_disjunta.png", dpi=100)
plt.close(fig)

# --- junta -----------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 2.6))
panel(ax, "G + H  (junta)")
for a, b in [("a", "c"), ("a", "d"), ("b", "c"), ("b", "d")]:
    arista(ax, posU[a], posU[b], color="#dc2626", estilo="--")
arista(ax, posU["a"], posU["b"])
arista(ax, posU["c"], posU["d"])
for n, p in posU.items():
    nodo(ax, p, n)
ax.text(0.3, 2.15, "G", ha="center", fontsize=12, color="#475569")
ax.text(2.6, 2.15, "H", ha="center", fontsize=12, color="#475569")
fig.tight_layout()
fig.savefig("imagenes/junta.png", dpi=100)
plt.close(fig)

print("OK")
