from abc import ABC, abstractmethod

# 一个抽象组件类，定义了一个抽象方法 draw
class Component(ABC):
    # 绘制组件
    @abstractmethod
    def draw(self):
        pass
