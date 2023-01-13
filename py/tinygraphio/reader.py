from typing import Optional

from google.protobuf.internal.decoder import _DecodeVarint

from tinygraphio.graph import Tinygraph, Node, Edge
from tinygraphio.errors import DataLossError
from tinygraphio.utils import delta_decode

from tinygraphio.proto.tinygraphio_pb2 import FileHeader, GraphHeader, GraphChunk


class TinygraphioReader:
    def __init__(self, io):
        self.io = io

    def read(self) -> Tinygraph:
        return self._read_graph()

    def close(self) -> None:
        self.io.close()

    def _read_file_header(self) -> FileHeader:
        # 2x fixed64 plus their tag
        buf = self.io.read(2 * 8 + 2)

        if not buf:
            raise DataLossError("Could not read all file header bytes")

        obj = FileHeader()
        obj.ParseFromString(buf)

        return obj

    def _read_graph_header(self) -> GraphHeader:
        # 2x fixed64 plus their tag
        buf = self.io.read(2 * 8 + 2)

        if not buf:
            raise DataLossError("Could not read all graph header bytes")

        obj = GraphHeader()
        obj.ParseFromString(buf)

        return obj

    def _read_graph_chunk(self) -> Optional[GraphChunk]:
        # TODO: this will fail if we write out e.g. an
        # empty graph chunk and a prefix size of 0. We
        # should in addition store number of graph chunks
        # e.g. in the graph header or use a fixed size
        # prefix here instead of a variable sized varint.
        szbuf = self.io.peek(4)

        if not szbuf:
            return None

        size, pos = _DecodeVarint(szbuf, pos=0)
        self.io.seek(pos, 1)

        buf = self.io.read(size)

        if not buf:
            raise DataLossError("Could not read all graph chunk bytes")

        obj = GraphChunk()
        obj.ParseFromString(buf)

        return obj

    def _read_graph(self) -> Tinygraph:
        file_header = self._read_file_header()
        graph_header = self._read_graph_header()

        offsets = []
        targets = []

        while True:
            chunk = self._read_graph_chunk()

            if not chunk:
                break

            offsets += chunk.offsets
            targets += chunk.targets

        return Tinygraph(offsets=[Edge(e) for e in delta_decode(offsets)],
                         targets=[Node(n) for n in targets])

    def __repr__(self) -> str:
        return f"<TinygraphioReader {self.io}>"
