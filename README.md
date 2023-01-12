# tinygraphio specification

tinygraphio is a graph data interchange file format.
The use case tinygraphio covers is storing large graphs effectively and efficiently and sharing graphs in a portable way.


## Versioning

The GraphIO interchange file format is versioned following [Semantic Versioning 2.0.0](https://semver.org).

| Version | Release | Changelog |
| ------: | ------- | --------- |
| [1.0.0](./v1) | 2023-01-29 | First release |


## Format

The tinygraphio file stores a directed (or bidirectional) graph in a compressed sparse row format for a compact representation.
The compressed sparse row format minimizes storage use to O(n + m) where n and m are the number of vertices and edges, respectively.

The on-disk representation of the compressed sparse row graph is based on Protocol Buffers.

The recommended file extension for a tinygraphio file is `.tinygraph`.


## Implementations

* [Python](./py)


## Authors

* Daniel J. Hofmann


## License

The text of this specification is licensed under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).
