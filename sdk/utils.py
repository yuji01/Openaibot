# -*- coding: utf-8 -*-

"""
bilibili_api.utils.sync

同步执行异步函数
"""
import asyncio
import hashlib
from typing import Coroutine

import nest_asyncio

nest_asyncio.apply()


def __ensure_event_loop():
    try:
        asyncio.get_event_loop()
    except Exception as e:
        asyncio.set_event_loop(asyncio.new_event_loop())


def sync(coroutine: Coroutine):
    """
    同步执行异步函数，使用可参考 [同步执行异步代码](https://nemo2011.github.io/bilibili-api/#/sync-executor)

    Args:
        coroutine (Coroutine): 异步函数

    Returns:
        该异步函数的返回值
    """
    __ensure_event_loop()
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coroutine)


def sha1_encrypt(string):
    """
    sha1加密算法
    """

    sha = hashlib.sha1(string.encode('utf-8'))
    encrypts = sha.hexdigest()
    return encrypts[:8]
