from .component import Component

# ┌──🌳oranges  ────────────────────────────────────────┐
# │   ├──🌳mandarin  ───────────────────────────────────┤
# │   │   ├──🍃clementine youknow ──────────────────────┤
# │   │   ├──🍃tangerine cheap & juicy! ────────────────┤
# ├──🌳apples  ─────────────────────────────────────────┤
# │   ├──🍃gala  ───────────────────────────────────────┤
# └───┴──🍃pink lady  ──────────────────────────────────┘


# 绘制一行，包括缩进、是否是最后一个、图标、名字、值
def render_line(indent, is_last, icon, name, value=None):
    if value is not None:
        print(f"{indent}{'└──' if is_last else '├──'}{icon}{name}: {value}")
    else:
        print(f"{indent}{'└──' if is_last else '├──'}{icon}{name}")


# 容器
class TreeContainer(Component):
    def __init__(self, name, container_icon, is_root=False):
        self.name = name
        self.children = []
        self.is_root = is_root
        self.container_icon = container_icon

    # 添加子组件，组合模式的核心方法
    def add(self, component):
        self.children.append(component)

    # 绘制当前容器，以及容器内的所有子组件
    def draw(self, indent="", is_last=False):
        if not self.is_root:
            render_line(indent, is_last, self.container_icon, self.name)
            indent += "    " if is_last else "│   "
        for i, child in enumerate(self.children):
            child.draw(indent, i == len(self.children) - 1)


# 叶子
class TreeLeaf(Component):
    def __init__(self, name, leaf_icon, value):
        self.name = name
        self.value = value
        self.leaf_icon = leaf_icon

    # 绘制叶子
    def draw(self, indent="", is_last=False):  # indent是缩进
        render_line(indent, is_last, self.leaf_icon, self.name, self.value)
