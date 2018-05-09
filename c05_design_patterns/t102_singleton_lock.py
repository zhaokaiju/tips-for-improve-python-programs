"""
单例的三个要求：
    1.只能有一个实例。
    2.它必须自行创建这个实例。
    3.它必须自行向整个系统提供这个实例。
"""

import threading


class Singleton(object):
    """
    单例（基于__new__实现，推荐使用）
    """

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # try:
            #     # 获得锁
            #     cls._instance_lock.acquire()
            #     if not hasattr(cls, "_instance"):
            #         cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            # finally:
            #     # 释放锁
            #     cls._instance_lock.release()

            # 使用with简化锁操作
            with cls._instance_lock:
                # 双检查锁机制
                if not hasattr(cls, "_instance"):
                    cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def gen_singleton():
    s = Singleton()
    print("id -> ", id(s))
    return s


def use_singleton():
    thread_list = []
    for i in range(10000):
        t = threading.Thread(target=gen_singleton)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()


if __name__ == '__main__':
    use_singleton()
