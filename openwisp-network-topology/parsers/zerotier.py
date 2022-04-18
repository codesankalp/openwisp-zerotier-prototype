from .base import BaseParser


class ZeroTierParser(BaseParser):
    def parse(self, data):
        graph = self._init_graph()
        server = self._server_common_name
        graph.add_node(server)
        nodes = []
        for node in data['nodes']:
            graph.add_node(node['address'], **node)
            nodes.append(node['address'])
        self._parse_edge(graph, nodes)
        return graph

    def _parse_edge(self, graph, nodes):
        for node in nodes:
            for path in graph.get('node'):
                graph.add_edge(
                    node, path.get('address'), weight=node.get('latency'), **path
                )
