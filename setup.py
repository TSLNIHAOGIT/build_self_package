'''
其中比较重要的几项是:name,version,packages
name:描述的是你打包的文件文件名。
version描述的是文件的版本号。
packages是所有要打包的包（package），这里需要打包的是test_package包以及test_package包下的test_package2。所以packages=[‘test_package’,‘test_package.test_package2’]。包与包之间用逗号“ ，”隔开

'''

from distutils.core import setup
setup(
    name='build_self_package',
    version='1.0',
    author='me',
    author_email='hh@qq.coom',
    url='www.baidu.com',
    packages=['test_package','test_package.test_package2']
)
