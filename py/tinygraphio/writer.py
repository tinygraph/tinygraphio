from google.protobuf.internal.encoder import _VarintBytes, _VarintSize

from tinygraphio.graph import Tinygraph
from tinygraphio.errors import DataLossError
from tinygraphio.utils import delta_encode

from tinygraphio.proto.tinygraphio_pb2 import FileHeader, GraphHeader, GraphChunk


class TinygraphioWriter:
    def __init__(self, io):
        self.io = io

    def write(self, graph: Tinygraph) -> int:
        return self._write_graph(graph)

    def flush(self) -> None:
        self.io.flush()

    def close(self) -> None:
        self.io.close()

    def _write_file_header(self, file_header: FileHeader) -> int:
        assert file_header.IsInitialized()

        buf = file_header.SerializeToString()
        assert len(buf) == (2 * 8 + 2)

        if self.io.write(buf) != len(buf):
            raise DataLossError("Could not write all file header bytes")

        return len(buf)

    def _write_graph_header(self, graph_header: GraphHeader) -> int:
        assert graph_header.IsInitialized()

        buf = graph_header.SerializeToString()
        assert len(buf) == (2 * 8 + 2)

        if self.io.write(buf) != len(buf):
            raise DataLossError("Could not write all graph header bytes")

        return len(buf)

    def _write_graph_chunk(self, graph_chunk: GraphChunk) -> int:
        assert graph_chunk.IsInitialized()

        buf = graph_chunk.SerializeToString()

        n = self.io.write(_VarintBytes(len(buf)) + buf)

        if n != _VarintSize(len(buf)) + len(buf):
            raise DataLossError("Could not write all graph chunk bytes")

        return n

    def _write_graph(self, graph: Tinygraph) -> int:
        file_header = FileHeader(version=1, checksum=0)

        graph_header = GraphHeader(nodes=graph.num_nodes(),
                                   edges=graph.num_edges())

        written = 0
        written += self._write_file_header(file_header)
        written += self._write_graph_header(graph_header)

        # The chunk size is a trade-off between having to decode
        # one chunk in memory at a time vs the overhead of chunks.
        # With a size ~20k we will get chunks of ~40k-160k bytes,
        # depending on how small varints will be encoded.
        chunk_size = 20000

        n = max(len(graph.offsets), len(graph.targets))

        for i in range(0, n, chunk_size):
            offsets = delta_encode(graph.offsets[i : i + n])
            targets = graph.targets[i : i + n]

            graph_chunk = GraphChunk(offsets=offsets, targets=targets)

            written += self._write_graph_chunk(graph_chunk)

        return written

    def __repr__(self) -> str:
        return f"<TinygraphioWriter {self.io}>"
