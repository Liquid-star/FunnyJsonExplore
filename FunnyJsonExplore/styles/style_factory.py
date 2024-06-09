from abc import ABC, abstractmethod


# 一个抽象工厂类，定义了两个抽象方法，分别用于创建容器和叶子组件
class ComponentFactory(ABC):
    # 创建容器组件
    @abstractmethod
    def create_container(self, name, is_root=False):
        pass

    # 创建叶子组件
    @abstractmethod
    def create_leaf(self, name, value=None):
        pass
