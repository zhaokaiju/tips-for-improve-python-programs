"""
单例的三个要求：
    1.只能有一个实例。
    2.它必须自行创建这个实例。
    3.它必须自行向整个系统提供这个实例。
"""


class Singleton(object):
    """
    单例（基于__new__实现）
    存在的问题：并发问题
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def use_singleton():
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), id(s2))
    assert id(s1) == id(s2)
    # 输出结果：
    """
    4502234056 4502234056
    """


if __name__ == '__main__':
    use_singleton()
