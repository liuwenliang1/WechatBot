简介
====
  
.. topic:: Intention
 ----
设计一个微信BOT，提供插件式编程，即根据需求写出相应功能，该bot会自动导入。


.. topic:: Quick Start
 ----
目前Tinker支持单文件功能导入，将所开发的功能添加至plugin目录下，并添加装饰器即可。

.. topic:: Sample
 ----

.. code-block:: python

    from tinker import r


    @r.register('ping')
    def ping():
        return 'pong'

当机器人收到"!ping"的命令时，就会立即返回一个"pong"作为回应。
