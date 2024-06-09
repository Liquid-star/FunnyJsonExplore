from FunnyJsonExplore.funny_json_explorer import FunnyJsonExplorer
from FunnyJsonExplore.styles.tree_style import TreeComponentFactory
from FunnyJsonExplore.styles.rectangle_style import RectangleComponentFactory
import json
import os


# 建造者模式
class FunnyJsonExplorerBuilder:
    def __init__(self):
        self.style = None
        self.icon_family = None
        self.config = None
        self.factory = None
        # 读取配置文件config.json
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path, 'config.json')
        with open(config_path, 'r') as f:
            self.config = json.load(f)

    # 根据用户输入的文本设置风格
    def set_style(self, style):
        self.style = style
        return self

    # 根据用户输入的文本设置图标库，对应的图标库的unicode在config.json中
    def set_icon_family(self, icon_family):
        if icon_family not in self.config['icon_families']:
            raise ValueError(f"不支持的图标库: {icon_family}")
        else:
            self.icon_family = self.config['icon_families'][icon_family]
        return self

    # 根据用户输入的风格和图标库创建FunnyJsonExplorer对象
    def build(self):
        if self.style == "tree":
            self.factory = TreeComponentFactory(self.icon_family[0], self.icon_family[1])
        elif self.style == "rectangle":
            self.factory = RectangleComponentFactory(self.icon_family[0], self.icon_family[1])
        self.explorer = FunnyJsonExplorer(self.factory)
        return self.explorer


if __name__ == "__main__":
    builder = FunnyJsonExplorerBuilder()
    # explorer = builder.set_style("tree").set_icon_family("default").build()
    explorer = builder.set_style("rectangle").set_icon_family("default").build()
    explorer.load_from_file('data1.json')
    explorer.show()
