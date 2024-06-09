from FunnyJsonExplore.styles.style_factory import ComponentFactory
from FunnyJsonExplore.styles.components.tree_container_leaf import TreeContainer, TreeLeaf
# ┌──🌳oranges  ────────────────────────────────────────┐
# │   ├──🌳mandarin  ───────────────────────────────────┤
# │   │   ├──🍃clementine youknow ──────────────────────┤
# │   │   ├──🍃tangerine cheap & juicy! ────────────────┤
# ├──🌳apples  ─────────────────────────────────────────┤
# │   ├──🍃gala  ───────────────────────────────────────┤
# └───┴──🍃pink lady  ──────────────────────────────────┘


# 树形风格组件工厂
class TreeComponentFactory(ComponentFactory):
    # 构造函数，初始化容器图标和叶子图标
    def __init__(self, container_icon="", leaf_icon=""):
        self.leaf_icon = leaf_icon
        self.container_icon = container_icon

    # 创建容器
    def create_container(self, name, is_root=False):
        return TreeContainer(name, self.container_icon, is_root)

    # 创建叶子
    def create_leaf(self, name, value=None):
        return TreeLeaf(name, self.leaf_icon, value)
