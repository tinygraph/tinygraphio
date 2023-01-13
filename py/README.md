# tinygraphio

Python implementation of the tinygraphio graph data interchange file format.


## Installation

Install with `poetry`

    poetry add tinygraphio

Install with `pip`

    pip install tinygraphio


## Usage

- The `Tinygraph` class implements a compressed sparse row graph
- The `TinygraphioReader` implements reading a graph from a binary file-like object
- The `TinygraphioWriter` implements writing a graph to a binary file-like object

```python3
from tinygraphio.graph import Tinygraph, Node, Edge
from tinygraphio.reader import TinygraphioReader
from tinygraphio.writer import TinygraphioWriter
```

Writing

```
graph = Tinygraph(offsets=[0, 2, 4, 5], targets=[1, 2, 0, 2, 1])

with open("berlin.tinygraph", "wb") as f:
    writer = TinygraphioWriter(f)
    writer.write(graph)
```

Reading

```
with open("berlin.tinygraph", "rb") as f:
    reader = TinygraphioReader(f)
    graph = reader.read()
```

Note: this library implements reading and writing a compressed sparse row graph in a 
The use case tinygraphio covers is storing large graphs effectively and efficiently and sharing graphs in a portable way.
We do not provide a full-blown graph computation toolkit on purpose.

## Development


## License

Copyright © 2023 tinygraph

Distributed under the MIT License (MIT).
