深度学习导包路径问题

### 1 添加系统路径

一般系统路径包括当前脚本下的目录，项目根目录，虚拟环境相关目录，pycharm的python环境目录（这个我也不是很清楚），要是想导其他路径的包，这个时候就要在适当位置添加系统路径了

以下为我所建项目的目录结构：

我使用以下命令实现

```shell
tree ./ /F > tree.txt
```

截取我需要的部分如下

```shell
E:\CODE\PYTHON_CODE\PACKAGIMPORT
│  tree.txt
│  __init__.py
│  
├─.idea
│      .gitignore
│      encodings.xml
│      workspace.xml
│      
├─p1
│  ├─m1_1
│  │      m1_1.py
│  │      
│  └─m1_2
│          m1_2.py
│          
├─p2
│  │  module_test.py
│  │  __init__.py
│  │  
│  ├─m2_1
│  │  │  m2_1.py
│  │  │  m2_1_test.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          m2_1.cpython-38.pyc
│  │          
│  ├─m2_2
│  │  │  m2_2_md.py
│  │  │  oprator.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          oprator.cpython-38.pyc
│  │          __init__.cpython-38.pyc
│  │          
│  └─__pycache__
│          __init__.cpython-38.pyc
│          
├─p3
│  │  m3.py
│  │  test.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          m3.cpython-38.pyc
│          __init__.cpython-38.pyc
│          
└─p4
    │  test.py
    │  __init__.py
    │  
    └─m4_1
            m4_1.py
```

```python
import os
import sys

import m2_1 as m21
# os.getcwd() 获取当前工作目录


sys.path.append("..")
# import m2_2 as m22
if __name__ == '__main__':
    m21.m2_1()
    print(sys.path)
    print(os.path.abspath(__file__))  # 当前绝对目录
    print(os.path.dirname(__file__))  # 当前脚本目录
    print(os.path)  # ntpath 模块
    print(os.pardir)  # ..
    # 获取上级目录一，因为..需要规范化normpath
    print(os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir)))
    # 获取上级目录二, 强烈推荐
    print('/'.join(os.path.dirname(__file__).split('\\')[:-1]))
    # 此时可以使用sys
    sys.path.append('/'.join(os.path.dirname(__file__).split('\\')[:-1]))
    print(sys.path)
```

### 2 模块相关属性

- `__file__`：指示当前文件的路径。

- `__name__`：指示当前模块的名字。在直接运行脚本时，`__name__` 会被设置为 `"__main__"`；在作为模块被导入时，`__name__` 会被设置为模块的名字。

- `__package__`：指示当前包的名字。如果当前文件是作为独立脚本运行的，`__package__` 会被设置为 `None`；如果当前文件是作为包中的模块导入的，`__package__` 会被设置为包的名字。

  以下以一个简单例子说明：

  ```python
  # p2/m2_1/m2_1.py
  print('__file__={0:<50} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))
  ```

  ```python
  # p2/module_test.py
  print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))
  
  # 以下打印的`__name__`属性和`__package__`会因导包方式而改变，即类似java的全类名
  from m2_1 import m2_1                # m2_1.m2_1      m2_1
  # from p2.m2_1 import m2_1           # p2.m2_1.m2_1   p2.m2_1
  # import p2.m2_1.m2_1                # p2.m2_1.m2_1   p2.m2_1
  # __file__=E:\code\python_code\packagImport\p2\module_test.py | __name__=__main__             | __package__=None
  # __file__=E:\code\python_code\packagImport\p2\m2_1\m2_1.py   | __name__=m2_1.m2_1            | __package__=m2_1
  ```

### 3 相对导入与绝对导入

- 绝对导入

  &emsp;绝对导入是要求在`sys.path`列表中存在导入路径才可以导入，如上目录结构，可以执行以下操作

  ```python
  # oprator.py
  import m2_2_md  # pass
  import p2.m2_2.m2_2_md  # pass
  import m2_2.m2_2_md  # ModuleNotFoundError: No module named 'm2_2', 该m2_2所在的目录没有在`sys.path`中
  ```

  ```python
  # module_test.py
  from p2.m2_2 import oprator as op  # pass
  import p2.m2_2.oprator as op  # pass
  ```

  但是运行脚本所在的目录下，必定在`sys.path`列表中，即可放心导入。

- 相对导入，本质上也是要求在`sys.path`列表中才可以成功导入，相对导入的模块一定不能是运行脚本

  ```python
  # oprator.py
  # 以下相对导入为该模块的`__name__`属性为当前脚本名字时不报错，当直接运行，即为`__name__`属性为`__main__`时报错
  from . import m2_2_md
  from .m2_2_md import m2_2
  from ..m2_2.m2_2_md import m2_2
  ```

### 4 相关导包报错

- 相对导入引起的异常报错：

  ```python
  # oprator.py
  #以下导包方式出现 ImportError: attempted relative import with no known parent package
  from .m2_2_md import *
  # from . import m2_2_md
  ```

  因为使用相对导入的模块不能作为顶级执行文件，此时`__package__`属性为None

- 相对导入误用于非顶级包内的模块

  ```python
  # oprator.py
  """
     具体看调用该模块形式
     如果为 import p2.m2_2.oprator as op
         module_test.py 调用该模块使用以下导包， 该模块的顶级包(top-level package)为m2_2， 而m2_2包下并没有子包m2_1  
     如果为 import m2_2.oprator as op
         p2包下存在子包m2_1
     因此报错： ValueError: attempted relative import beyond top-level package
  """
  from ..m2_1 import m2_1_test
  ```

  ```python
  # module_test.py
  # 正常，不会报错, p2存在子包m2_1
  import p2.m2_2.oprator as op
  # 报错，m2_2不存在子包m2_1
  import m2_2.oprator as op
  ```

- 方法内想导入模块的全部方法和属性

  ```python
  def main():
      # SyntaxError: import * only allowed at module level 方法内部不能import所有
      from m2_2_md import *
      pass
  
  ```

- 导入所有模块、方法、属性时并没有在`__init__`导入模块，或者属性方法

  ```python
  # p4/test.py
  # 如果`sys.path`没有p3所在的目录，需要添加，否则会报错
  # sys.path.append('\\'.join(os.path.dirname(__file__).split('\\')[:-1]))
  # print(sys.path)
  from p3 import *
  m3.m3()
  ```

  ```python
  # p3/__init__.py
  # 不执行以下导入，报错
  from . import m3
  ```

  