from typing import Any


class CallMe:
    def __init__(self, numero) -> None:
        self.numero = numero

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print('chamando', self.numero)


call1 = CallMe(1564189453189)

call1()