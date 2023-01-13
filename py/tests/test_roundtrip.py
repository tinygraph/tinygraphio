import io
import tempfile
import unittest
from pathlib import Path

from tinygraphio.graph import Tinygraph
from tinygraphio.reader import TinygraphioReader
from tinygraphio.writer import TinygraphioWriter


class RoundtripTestCase(unittest.TestCase):
    def test_roundtrip_bytesio(self):
        b1 = io.BytesIO()

        g1 = Tinygraph(offsets=[0, 2, 4, 5], targets=[1, 2, 0, 2, 1])

        writer = TinygraphioWriter(b1)
        writer.write(g1)

        b1.seek(0)

        reader = TinygraphioReader(io.BufferedReader(b1))
        g2 = reader.read()

        self.assertEqual(list(g1.offsets), list(g2.offsets))
        self.assertEqual(list(g1.targets), list(g2.targets))

    def test_roundtrip_file(self):
        g1 = Tinygraph(offsets=[0, 2, 4, 5], targets=[1, 2, 0, 2, 1])

        with tempfile.TemporaryDirectory() as workdir:
            workdir = Path(workdir)

            with open(workdir / "g1.tinygraph", "wb") as f:
                writer = TinygraphioWriter(f)
                writer.write(g1)

            with open(workdir / "g1.tinygraph", "rb") as f:
                reader = TinygraphioReader(f)
                g2 = reader.read()

        self.assertEqual(list(g1.offsets), list(g2.offsets))
        self.assertEqual(list(g1.targets), list(g2.targets))


if __name__ == "__main__":
    unittest.main()
