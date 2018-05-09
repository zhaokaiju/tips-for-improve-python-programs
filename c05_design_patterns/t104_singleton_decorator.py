"""
单例的三个要求：
    1.只能有一个实例。
    2.它必须自行创建这个实例。
    3.它必须自行向整个系统提供这个实例。
"""


def singleton(cls):
    """
    单例（使用装饰器实现）
    存在的问题：并发问题
    """

    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class UserManager(object):
    pass


def use_singleton():
    u1 = UserManager()
    u2 = UserManager()
    print(id(u1), id(u2))
    assert id(u1) == id(u2)
    # 输出结果：
    """
    4502234000 4502234000
    """


if __name__ == '__main__':
    use_singleton()
