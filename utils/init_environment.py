#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import platform
from pathlib import Path
import subprocess

def ensure_directories():
    """
    确保必要的目录存在，如果markdown目录存在则清空
    """
    try:
        # 获取当前脚本所在目录的上级目录（项目根目录）
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 需要确保存在的目录
        required_dirs = ['markdown', 'testcase', 'xmind']
        
        for dir_name in required_dirs:
            # 使用绝对路径
            dir_path = Path(os.path.join(root_dir, dir_name))
            
            # 如果是markdown目录且存在，清空它
            if dir_name in ['markdown','testcase'] and dir_path.exists():
                shutil.rmtree(dir_path)
                dir_path.mkdir()
                print(f"已清空并重新创建目录: {dir_path}")
            # 如果目录不存在，创建它
            elif not dir_path.exists():
                dir_path.mkdir()
                print(f"已创建目录: {dir_path}")
            
        return True
        
    except Exception as e:
        print(f"初始化目录时出错: {str(e)}")
        return False

def install_dependencies():
    try:
        req_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'requirements.txt')
        if os.path.exists(req_file):
            print("正在安装Python依赖...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', req_file, '--break-system-packages'])
            return True
        print("未找到requirements.txt文件")
        return False
    except Exception as e:
        print(f"依赖安装失败: {str(e)}")
        return False


# 在 initialize_environment() 函数中添加文件存在性检查
def initialize_environment():
    """
    初始化环境：创建必要目录并清理markdown目录
    """
    try:
        # 确保必要的目录存在
        if not ensure_directories():
            return False
            
        # 安装依赖
        if not install_dependencies():
            return False
            
        print("环境初始化完成")
        return True
        
    except Exception as e:
        print(f"初始化环境时出错: {str(e)}")
        return False

if __name__ == "__main__":
    # 设置控制台输出编码为UTF-8
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')
    success = initialize_environment()
    sys.exit(0 if success else 1)