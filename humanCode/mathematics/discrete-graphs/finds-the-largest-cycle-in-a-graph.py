import networkx
import matplotlib

# generate a random graph
g = networkx.fast_gnp_random_graph(10, .5)
cycles = networkx.simple_cycles(g)

length = 0
the_cycle = []
for cycle in cycles:
    if len(cycle) > length:
        the_cycle = cycle
        length = len(cycle)

networkx.draw_networkx(g)

# the_cycle represents the longest cycle in the graph now.
print(len(the_cycle))
matplotlib.pyplot.show()
