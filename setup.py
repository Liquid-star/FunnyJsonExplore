from setuptools import setup, find_packages

# setup(
#     name='funnyjsonexplorer',
#     version='1.0',
#     py_modules=['fje'],
#     install_requires=[
#         'matplotlib',  # 在这里添加所有其他需要的库
#     ],
#     entry_points='''
#         [console_scripts]
#         fje=fje:main
#     ''',
# )

# setup(
#     name='funnyjsonexplorer',
#     version='1.0',
#     packages=find_packages(),  # 自动发现并包含所有包
#     install_requires=[
#     ],
#     entry_points='''
#         [console_scripts]
#         fje=FunnyJsonExplore.main:main
#     ''',
# )

setup(
    name='funnyjsonexplorer',
    version='1.0',
    packages=find_packages(),  # 自动发现并包含所有包
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
        fje=FunnyJsonExplore.fje:main
    ''',
    package_data={
        'FunnyJsonExplore': ['config.json']
    }
)
