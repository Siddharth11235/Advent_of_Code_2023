from collections import deque
from math import gcd


with open("day20/input.txt", mode="r") as input_stream:
    signal_list = input_stream.read().splitlines()


def split_graph_row(graph_row):
    input_node = graph_row.split(" -> ")[0]

    if input_node != "broadcaster":
        input_node_name = input_node[1:]
        input_node_type = input_node[0]

    else:
        input_node_name = input_node
        input_node_type = input_node

    return input_node_name, input_node_type


class Node:
    def __init__(self, name, node_type, parents=None):
        self.name = name
        self.node_type = node_type

        self.state = False  # Initially off

        if parents:
            self.prev_signal = {x: "LOW" for x in parents}

        self.input_num = 0

    def propagate_signal(self, signal, sender):
        if self.node_type == "broadcaster":
            return signal
        elif self.node_type == "button":
            return "LOW"
        elif self.node_type == "%":
            signal = signal
            if signal == "HIGH":
                return
            elif signal == "LOW":
                if self.state == False:
                    self.state = True
                    return "HIGH"
                else:
                    self.state = False
                    return "LOW"
        elif self.node_type == "&":
            self.prev_signal[sender] = signal

            if all(s == "HIGH" for s in self.prev_signal.values()):
                return "LOW"
            else:
                return "HIGH"

    def get_node_state(self):
        if self.node_type == "&":
            return self.prev_signal
        else:
            return self.state


class Graph:
    def __init__(self):
        self.nodes = {"button": Node("button", "button", 0)}
        self.edges = {"button": ["broadcaster"]}
        self.initial_states = {"button": self.nodes["button"].state}
        self.node_states = self.initial_states
        self.pulse_counter = {"LOW": 0, "HIGH": 0}

    def add_node(self, node):
        self.nodes[node.name] = node
        self.initial_states[node.name] = node.get_node_state()

    def add_edge(self, from_node, to_node):
        if from_node in self.edges.keys():
            self.edges[from_node].append(to_node)
        else:
            self.edges[from_node] = [to_node]

    def propagate_signal(self):
        incoming_signals = {name: deque([]) for name in self.nodes.keys()}
        current_states = {}
        cycle_count = 0
        signal_none = False
        while cycle_count < 1000:
            next_steps = deque([("button", ["broadcaster"])])
            incoming_signals["button"].append(("LOW", None))
            while len(next_steps) > 0:
                from_node, to_nodes = next_steps.popleft()
                incoming_signal, parent = incoming_signals[from_node].popleft()
                signal = self.nodes[from_node].propagate_signal(incoming_signal, parent)

                for to_node in to_nodes:
                    if signal == None:
                        signal_none = True
                        break
                    self.pulse_counter[signal] += 1
                    if to_node in self.edges.keys():
                        next_steps.append((to_node, self.edges[to_node]))
                        incoming_signals[to_node].append((signal, from_node))

            current_states = {
                name: node.get_node_state() for name, node in self.nodes.items()
            }
            cycle_count += 1
        return (cycle_count, self.pulse_counter)

    def get_rx_out(self):
        incoming_signals = {name: deque([]) for name in self.nodes.keys()}
        current_states = {}
        cycle_count = 0
        signal_none = False

        list_of_rx_input_high = {}
        output_found = False
        while not output_found:
            next_steps = deque([("button", ["broadcaster"])])
            incoming_signals["button"].append(("LOW", None))
            while len(next_steps) > 0:
                from_node, to_nodes = next_steps.popleft()
                incoming_signal, parent = incoming_signals[from_node].popleft()
                signal = self.nodes[from_node].propagate_signal(incoming_signal, parent)

                for to_node in to_nodes:
                    if to_node == "zr":
                        if signal == "HIGH":
                            if from_node not in list_of_rx_input_high.keys():
                                list_of_rx_input_high[from_node] = cycle_count
                        if list_of_rx_input_high.keys() == 4:
                            output_found = True
                            break
                    if signal == None:
                        signal_none = True
                        break
                    self.pulse_counter[signal] += 1
                    if to_node in self.edges.keys():
                        next_steps.append((to_node, self.edges[to_node]))
                        incoming_signals[to_node].append((signal, from_node))
                if output_found:
                    break
            if len(list_of_rx_input_high) == 4:
                return list_of_rx_input_high
            current_states = {
                name: node.get_node_state() for name, node in self.nodes.items()
            }
            cycle_count += 1


graph = Graph()
node_inputs = {"broadcaster": ["button"]}
for graph_row in signal_list:
    input_node_name, input_node_type = split_graph_row(graph_row)
    to_nodes = graph_row.split(" -> ")[1].split(",")
    for to_node in to_nodes:
        if to_node[0] == " ":
            to_node = to_node[1:]
        if to_node in node_inputs.keys():
            node_inputs[to_node].append(input_node_name)
        else:
            node_inputs[to_node] = [input_node_name]
        graph.add_edge(input_node_name, to_node)

for graph_row in signal_list:
    input_node_name, input_node_type = split_graph_row(graph_row)
    current_node = Node(input_node_name, input_node_type, node_inputs[input_node_name])
    graph.add_node(current_node)

cycle_count, output = graph.propagate_signal()
print(cycle_count, output)
total_soln = 1
for count in output.values():
    total_soln = total_soln * count

print(f"Solution to Part 1: {total_soln}")


# Part 2
graph2 = Graph()
node_inputs = {"broadcaster": ["button"]}
for graph_row in signal_list:
    input_node_name, input_node_type = split_graph_row(graph_row)
    to_nodes = graph_row.split(" -> ")[1].split(",")
    for to_node in to_nodes:
        if to_node[0] == " ":
            to_node = to_node[1:]
        if to_node in node_inputs.keys():
            node_inputs[to_node].append(input_node_name)
        else:
            node_inputs[to_node] = [input_node_name]
        graph2.add_edge(input_node_name, to_node)

for graph_row in signal_list:
    input_node_name, input_node_type = split_graph_row(graph_row)
    current_node = Node(input_node_name, input_node_type, node_inputs[input_node_name])
    graph2.add_node(current_node)


def calculate_lcm(list_of_ints):
    lcm = 1

    for i in list_of_ints:
        num = i + 1
        lcm = lcm * num // gcd(lcm, num)
    return lcm


list_of_rx_input_high = graph2.get_rx_out()
list_of_vals = list(list_of_rx_input_high.values())

print(f"Solution to Part 2: {calculate_lcm(list_of_vals)}")
