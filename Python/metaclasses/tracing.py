from typing import Tuple, Any, Mapping

class TracingMeta(type):
    @classmethod
    def __prepare__(metacls, __name: str, __bases: Tuple[type, ...], **kwds: Any) -> Mapping[str, Any]:
        print("TracingMeta.__prepare__(__name, __bases, **kwds)")
        print("   metacls = {}".format(metacls))
        print("   __name = {}".format(__name))
        print("   __bases = {}".format(__bases))
        print("   kwd = {}".format(kwds))
        namespace = super().__prepare__(__name, __bases)
        print("<-- namespace = {}".format(namespace))
        print()
        return namespace


    def __new__(metacls, __name, __bases, namespace, **kwargs):
        print("TracingMeta.__new__(metacls, __name, __bases, namespace, **kwargs)")
        print("    metacls =", metacls)
        print("    name =", __name)
        print("    bases =", __bases)
        print("    namespace=", namespace)
        print("    kwargs =", kwargs)
        cls = super().__new__(metacls, __name, __bases, namespace)
        print('<-- cls =', cls)
        print()
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        print('TracingMeta.__init__(cls, name, bases, namespace, **kwargs)')
        print('    cls=', cls)
        print('    name=',name)
        super().__init__(name, bases, namespace)


class Widget(metaclass=TracingMeta):
    def __init__(self) -> None:
        print('In widget')


if __name__ == '__main__':
    w = Widget()
    print(isinstance(w, type))
    if callable(w):
        print(True)
    else:
        print(False)