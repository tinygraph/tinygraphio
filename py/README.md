# tinygraphio

Python implementation of the tinygraphio graph data interchange file format.


## Installation

Install with `poetry`

    poetry add tinygraphio

Install with `pip`

    pip install tinygraphio


## Usage

- `Tinygraph` implements a compressed sparse row graph
- `TinygraphioReader` implements reading a graph from a binary file-like object
- `TinygraphioWriter` implements writing a graph to a binary file-like object

```python3
from tinygraphio.graph import Tinygraph, Node, Edge
from tinygraphio.reader import TinygraphioReader
from tinygraphio.writer import TinygraphioWriter
```

Writing

```python3
graph = Tinygraph(offsets=[0, 2, 4, 5], targets=[1, 2, 0, 2, 1])

with open("berlin.tinygraph", "wb") as f:
    writer = TinygraphioWriter(f)
    writer.write(graph)
```

Reading

```python3
with open("berlin.tinygraph", "rb") as f:
    reader = TinygraphioReader(f)
    graph = reader.read()
```

Note: this library implements reading and writing a compressed sparse row graph effectively and efficiently and sharing it in a portable way.
We do not provide a full-blown graph computation toolkit on purpose.

## Development


## License

Copyright © 2023 tinygraph

Distributed under the MIT License (MIT).
