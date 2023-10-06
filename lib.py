import networkx as nx
import matplotlib.pyplot as plt

SIZE = 1300

class AutoGraph(nx.DiGraph):
    def __init__(self) -> None:
        super().__init__()
        self.labels = {}
        self.labels_loop = {}
        self.accept_nodes = []
        self.normal_nodes = []
        self.node_position = {}
        self.label_position = {}
        self.input_node = []

    def create_nodes(self, node_name: str, pos: tuple, input:bool = False, accept:bool = False):
        self.add_node(node_name, input=input, accept= accept)
        
        if accept: self.accept_nodes.append(node_name)
        elif input: self.input_node.append(node_name)
        else: self.normal_nodes.append(node_name)
        self.node_position[node_name] = pos

    def create_edges(self, node_1: str, node_2: str, label: str = ""):
        self.add_edge(node_1, node_2, label=label)

        node1_pos = self.node_position[node_1]
        node2_pos = self.node_position[node_2]

        vert = node1_pos[0] == node2_pos[0]
        horz = node1_pos[1] == node2_pos[1]

        if node_1 == node_2:
            self.label_position[node_1] = (node1_pos[0] - 0.25, node1_pos[1] + 0.15)
        elif vert:
            self.label_position[node_1] = (node1_pos[0], node1_pos[1] + 0.12)
        elif horz:
            self.label_position[node_1] = (node1_pos[0] - 0.2, node1_pos[1])
        else:
            self.label_position[node_1] = (node1_pos[0], node1_pos[1])

    def draw_graph(self):
        labels = {edge: self.edges[edge]["label"] for edge in self.edges}

        nx.draw(self, self.node_position, with_labels=True, nodelist=self.normal_nodes, node_size=SIZE, node_color="lightblue", font_size=10)
        nx.draw_networkx_nodes(self, self.node_position, nodelist=self.input_node, node_shape=">", node_color="yellow", node_size=SIZE)
        nx.draw_networkx_nodes(self, self.node_position, nodelist=self.accept_nodes, node_color="red", node_size=SIZE)
        nx.draw_networkx_edge_labels(self, self.label_position, edge_labels=labels)

        plt.title("AFN Inicial")
        plt.show()