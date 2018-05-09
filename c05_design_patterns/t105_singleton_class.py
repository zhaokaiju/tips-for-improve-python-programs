"""
单例的三个要求：
    1.只能有一个实例。
    2.它必须自行创建这个实例。
    3.它必须自行向整个系统提供这个实例。
"""


class Singleton(object):
    """
    单例（使用类实现）
    存在的问题：并发问题
    """

    def __init__(self):
        pass

    @classmethod
    def singleton(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(*args, **kwargs)
        return cls._instance


def use_singleton():
    s1 = Singleton().singleton()
    s2 = Singleton().singleton()
    print(id(s1), id(s2))
    assert id(s1) == id(s2)
    # 输出结果：
    """
    4502848512 4502848512
    """


if __name__ == '__main__':
    use_singleton()
