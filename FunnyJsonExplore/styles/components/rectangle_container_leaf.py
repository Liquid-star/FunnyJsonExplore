from FunnyJsonExplore.styles.components.component import Component

# ┌──📦oranges  ────────────────────────────────────────┐
# │   ├──📦mandarin  ───────────────────────────────────┤
# │   │   ├──📖clementine  ─────────────────────────────┤
# │   │   ├──📖tangerine cheap & juicy! ────────────────┤
# │   ├──📦mandarin1  ──────────────────────────────────┤
# │   │   ├──📖clementine  ─────────────────────────────┤
# │   │   ├──📖tangerine cheap & juicy! ────────────────┤
# ├──📦apples  ─────────────────────────────────────────┤
# │   ├──📖gala  ───────────────────────────────────────┤
# └───┴──📖pink lady  ──────────────────────────────────┘

# 判断每一行的最后一个字符
def judge_suffix(is_last, is_first):
    if is_first:
        suffix = f"{'-' if is_last else '┐'}"
    else:
        suffix = f"{'┘' if is_last else '┤'}"
    return suffix


# 渲染一行，包括缩进indent、是否是第一行is_first、是否是最后一行is_last、图标的unicode icon,、名称name、行的长度line_length、
# 后缀suffix、值value
# 如果pre_walk为True，则返回行的长度（用于确定合适的line_length）
def render_line(indent, is_first, is_last, icon, name, line_length, suffix, value=None, pre_walk=False):
    if value is None:
        line = "─" * (line_length - len(name) - len(indent) - 5) + suffix
    else:
        line = "─" * (line_length - len(name) - len(str(value)) - len(indent) - 5) + suffix
    # 判断是否是第一行
    if is_first:
        if pre_walk:
            return len(f"{indent}{'-' if is_last else '┌'}──{icon}{name} {value if value is not None else ''} {line}")
        # 如果是第一行但是不是最后一行打印┌──📦oranges  ──────────────┐
        # 如果是第一行且是最后一行打印───📦oranges  ────────────────
        print(f"{indent}{'-' if is_last else '┌'}──{icon}{name} {value if value is not None else ''} {line}")
    else:
        if is_last:
            # 修改indent 从"│   "到"└───"
            # 修改前：│   │   ├──📖clementine ───────────────────────────────────────────────────┤
            # 修改后：└───┴───┴──📖clementine ───────────────────────────────────────────────────┘
            for i in range(0, len(indent), 4):
                indent = indent[:i] + "└───" + indent[i + 4:]
        if pre_walk:
            return len(f"{indent}{'┴' if is_last else '├'}──{icon}{name} {value if value is not None else ''} {line}")
        # 如果不是第一行但是是最后一行打印└──📦oranges  ────────────────
        print(f"{indent}{'┴' if is_last else '├'}──{icon}{name} {value if value is not None else ''} {line}")


# 矩形风格容器
class RectangleContainer(Component):
    def __init__(self, name, container_icon, is_root=False):
        self.name = name
        self.children = []
        self.is_root = is_root
        self.container_icon = container_icon

    # 添加子组件，组合模式的核心方法
    def add(self, component):
        self.children.append(component)

    # 绘制当前容器，以及容器内的所有子组件
    def draw(self, indent="", is_last=False, is_first=False, line_length=50):
        # 判断是否是根容器，如果是根容器则不draw自身，直接draw子容器
        if not self.is_root:
            last_container = is_last and len(self.children) == 0
            # 判断最后一个字符：┤ ┐ ┘ -
            suffix = judge_suffix(last_container, is_first)
            # 绘制一行（当前容器）
            render_line(indent, is_first, last_container, self.container_icon, self.name, line_length, suffix)
            # 设置缩进
            indent += "│   "
            # 绘制子节点
            for i, child in enumerate(self.children):
                child.draw(indent, (i == len(self.children) - 1) and is_last, False, line_length)

        else:
            # walk方法用于计算每一行的长度，以确定line_length
            Num=self.walk(indent, is_last, is_first, line_length)
            # 绘制子节点
            for i, child in enumerate(self.children):
                child.draw(indent, i == len(self.children) - 1, i == 0, Num)

    # 计算每一行的长度，以确定line_length，模拟绘制过程
    def walk(self, indent="", is_last=False, is_first=False, line_length=10):
        MaxLineNum=0
        if not self.is_root:
            last_container = is_last and len(self.children) == 0
            # 后缀
            suffix = judge_suffix(last_container, is_first)
            MaxLineNum=render_line(indent, is_first, last_container, self.container_icon, self.name, line_length, suffix,None,True)
            indent += "│   "
            for i, child in enumerate(self.children):
                Num=child.walk(indent, (i == len(self.children) - 1) and is_last, False, line_length)
                MaxLineNum=max(MaxLineNum,Num)

        else:
            for i, child in enumerate(self.children):
                Num=child.walk(indent, i == len(self.children) - 1, i == 0, line_length)
                MaxLineNum=max(MaxLineNum,Num)

        return MaxLineNum


# 矩形风格叶子
class RectangleLeaf(Component):
    def __init__(self, name, leaf_icon, value=None):
        self.name = name
        self.value = value
        self.leaf_icon = leaf_icon

    # 绘制叶子
    def draw(self, indent="", is_last=False, is_first=False, line_length=50):

        # 后缀
        suffix = judge_suffix(is_last, is_first)

        render_line(indent, is_first, is_last, self.leaf_icon, self.name, line_length, suffix, self.value)

    # 返回当前行的长度
    def walk(self, indent="", is_last=False, is_first=False, line_length=50):
        # 后缀
        suffix = judge_suffix(is_last, is_first)

        return render_line(indent, is_first, is_last, self.leaf_icon, self.name, line_length, suffix, self.value, True)