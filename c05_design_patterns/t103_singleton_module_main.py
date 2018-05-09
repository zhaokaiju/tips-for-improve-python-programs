"""
单例的三个要求：
    1.只能有一个实例。
    2.它必须自行创建这个实例。
    3.它必须自行向整个系统提供这个实例。

Python的模块（天然单例的实现）：
    1.所有的变量都会绑定到模块。
    2.模块只初始化一次。
    3.import机制是线程安全的（保证在并发状态下模块也只有一个实例）
"""

from t103_singleton_module import singleton
from t103_singleton_module import singleton as s

if __name__ == '__main__':
    print(id(singleton))
    print(id(s))
