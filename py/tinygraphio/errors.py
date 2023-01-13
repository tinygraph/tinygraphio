class TinygraphioError(Exception):
    code: int

class UnknownError(TinygraphioError):
    code = 1

class InternalError(TinygraphioError):
    code = 2

class DataLossError(TinygraphioError):
    code = 3

class InvalidArgumentError(TinygraphioError):
    code = 4
