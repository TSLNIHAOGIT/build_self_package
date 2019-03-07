一.参考链接
1.https://blog.csdn.net/ITBriceWu/article/details/82774939
2.https://blog.csdn.net/Julialove102123/article/details/80009971

二.打包说明
在原来文件的根目录下新建setup.py文件
1.只需要修改setup.py文件
  其中比较重要的几项是:name,version,packages
   name:描述的是你打包的文件文件名。
   version描述的是文件的版本号。
   packages是所有要打包的包（package），这里需要打包的是test_package包以及test_package包下的test_package2。所以packages=[‘test_package’,‘test_package.test_package2’]。包与包之间用逗号“ ，”隔开
2.打包命令
linux下的命令:python setup.py sdist 为模块创建一个源码包
     生成一个MANIFEST文件以及文件夹dist，而我们的源码包就在dist文件夹下面，解压该源码包
     执行sudo python setup.py install安装库，安装后即可正常使用
window下命令：python setup.py bdist_wininst 
     生成build、dist文件，dist文件下生成exe文件。双击该exe文件，就会弹出python库的安装界面（就是经典的蓝色界面），
     可以自己选择要安装的位置（特别是电脑中有多个版本的python的时候，需要指定这个库装到哪个python库目录下），一路下一步，就安装成功了。
     此时去指定的python库目录下，就会发现多出了一些我们自己安装的文件以及文件夹。此时试着import一下，就会发现已经可以导入我们自己的模块了
