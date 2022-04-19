import json

from netdiff.parsers.base import BaseParser


class ZeroTierParser(BaseParser):
    def to_python(self, data):
        return data

    def parse(self, data):
        graph = self._init_graph()
        leaf_nodes = []
        planet_nodes = []
        for network in data:
            graph.add_node(
                network['address'],
                **network,
            )
            if network.get('role') == 'PLANET':
                planet_nodes.append(network['address'])
            else:
                leaf_nodes.append(network['address'])
        self._parse_edge(graph, leaf_nodes)
        self._parse_edge(graph, planet_nodes)
        return graph

    def _parse_edge(self, graph, nodes):
        for node in nodes:
            node_data = graph.nodes.get(node)
            for path in node_data['paths']:
                graph.add_edge(
                    node, path.get('address'), weight=node_data.get('latency'), **path
                )
