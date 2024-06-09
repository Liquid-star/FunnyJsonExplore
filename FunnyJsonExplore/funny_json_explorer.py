import json


class FunnyJsonExplorer:
    # 指定工厂即可完成初始化
    def __init__(self, fectory):
        self.fectory = fectory
        self.container = self.fectory.create_container("根容器", is_root=True)

    # 对结果进行展示
    def show(self):
        self.container.draw()

    # 加载数据
    def load(self, data):
        # 递归解析数据
        self._parse_data(data, self.container)

    # 从文件加载数据(对外接口)
    def load_from_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.load(data)

    # 递归解析数据
    def _parse_data(self, data, parent):
        if isinstance(data, dict):
            # 遍历字典
            for key, value in data.items():
                if isinstance(value, dict):  # dict才给container，否则给leaf
                    container = self.fectory.create_container(key)
                    parent.add(container)
                    self._parse_data(value, container)
                else:
                    leaf = self.fectory.create_leaf(key, value)
                    parent.add(leaf)
