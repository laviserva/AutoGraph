from lib import AutoGraph

auto_graph = AutoGraph()
node_epsilon = r"$\epsilon$"  # "\u03B5" # epsilon
node_a = r"$a$"
node_ab = r"$ab$"
node_b = r"$b$"
node_aa = r"$aa$"

auto_graph.create_nodes(node_epsilon, (-2, 1), input=True)
auto_graph.create_nodes(node_a, (2, 1))
auto_graph.create_nodes(node_ab, (2, -1), accept=True)
auto_graph.create_nodes(node_b, (-2, -1))
auto_graph.create_nodes(node_aa, (0, 0))

auto_graph.create_edges(node_epsilon, node_a, "a")
auto_graph.create_edges(node_epsilon, node_b, "b")
auto_graph.create_edges(node_a, node_aa, "a")
auto_graph.create_edges(node_a, node_ab, "b")
auto_graph.create_edges(node_b, node_ab, "a")
auto_graph.create_edges(node_b, node_aa, "b")
auto_graph.create_edges(node_ab, node_ab, "a,b")
auto_graph.create_edges(node_aa, node_aa, "a,b")

auto_graph.draw_graph()