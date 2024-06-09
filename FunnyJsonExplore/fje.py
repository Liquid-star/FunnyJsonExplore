import argparse
import json
import os
from FunnyJsonExplore.ExploreBuilder import FunnyJsonExplorerBuilder


# 使用argparse模块解析命令行参数
def main():
    parser = argparse.ArgumentParser(description="Funny JSON Explorer (FJE) - JSON 文件可视化命令行工具")
    parser.add_argument('-f', '--file', required=True, help="JSON 文件路径")
    parser.add_argument('-s', '--style', required=True, help="可视化风格")
    parser.add_argument('-i', '--icon', required=True, help="图标库")

    # 解析命令行参数
    args = parser.parse_args()

    # 检查路径是否为相对路径，如果是，则转换为绝对路径
    if not os.path.isabs(args.file):
        file_path = os.path.abspath(args.file)
    else:
        file_path = args.file

    with open(file_path, 'r') as f:
        json_data = json.load(f)

    # 创建FunnyJsonExplorer对象
    builder = FunnyJsonExplorerBuilder()
    explorer = builder.set_style(args.style).set_icon_family(args.icon).build()
    # 加载数据并展示
    explorer.load(json_data)
    explorer.show()


if __name__ == "__main__":
    main()
