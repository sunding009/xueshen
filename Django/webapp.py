#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
所有来自Web服务器的HTTP请求都会由WSGI服务转化为对该函数的调用。
该示例的application函数中没有复杂的处理，只是通过start_response返回了状态码，并通过return返回了一个固定的HTTP请求。
"""


# WSGI python Web Server
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<b>Hello world!</b>'
