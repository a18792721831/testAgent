#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import xmindparser
import datetime

# 设置默认编码为utf-8
if sys.version_info[0] == 3:
    sys.stdout.reconfigure(encoding='utf-8')

class XMindToMarkdown:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.xmind_dir = os.path.join(self.current_dir, 'xmind')
        self.markdown_dir = os.path.join(self.current_dir, 'markdown')
        
    def convert_to_markdown(self, xmind_file):
        """
        将XMind文件转换为Markdown格式
        :param xmind_file: XMind文件名
        :return: 转换后的Markdown内容
        """
        xmind_path = os.path.join(self.xmind_dir, xmind_file)
        if not os.path.exists(xmind_path):
            raise FileNotFoundError(f"XMind文件不存在: {xmind_path}")

        # 解析XMind文件
        xmind_content = xmindparser.xmind_to_dict(xmind_path)
        if not xmind_content or not xmind_content[0].get('topic'):
            raise ValueError("XMind文件格式错误或内容为空")

        markdown_content = []
        root_topic = xmind_content[0]['topic']
        
        # 添加标题
        markdown_content.append(f"# {root_topic.get('title', '需求文档')}\n")
        
        # 添加生成时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        markdown_content.append(f"生成时间：{current_time}\n")

        # 处理子主题
        if 'topics' in root_topic:
            self._process_topics(root_topic['topics'], markdown_content, level=1)

        return '\n'.join(markdown_content)

    def _process_topics(self, topics, markdown_content, level):
        """
        递归处理XMind主题
        :param topics: 主题列表
        :param markdown_content: Markdown内容列表
        :param level: 当前层级
        """
        for topic in topics:
            # 添加标题
            title = topic.get('title', '')
            markdown_content.append(f"{'#' * (level + 1)} {title}\n")

            # 处理备注
            if 'note' in topic:
                note = topic['note'].strip()
                if note:
                    markdown_content.append(f"{note}\n")

            # 处理子主题
            if 'topics' in topic:
                self._process_topics(topic['topics'], markdown_content, level + 1)

    def convert_all_xminds(self):
        """
        转换xmind目录下的所有XMind文件为Markdown格式，并保存到markdown目录
        """
        # 确保xmind目录存在
        if not os.path.exists(self.xmind_dir):
            os.makedirs(self.xmind_dir)
            print(f"创建目录: {self.xmind_dir}")
            return

        # 确保markdown目录存在
        if not os.path.exists(self.markdown_dir):
            os.makedirs(self.markdown_dir)
            print(f"创建目录: {self.markdown_dir}")

        xmind_files = [f for f in os.listdir(self.xmind_dir) if f.endswith('.xmind')]
        if not xmind_files:
            print("没有找到XMind文件")
            return

        for xmind_file in xmind_files:
            try:
                markdown_content = self.convert_to_markdown(xmind_file)
                md_filename = os.path.splitext(xmind_file)[0] + '.md'
                md_path = os.path.join(self.markdown_dir, md_filename)
                
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                print(f"成功转换: {xmind_file} -> {md_filename}")
            except Exception as e:
                print(f"转换 {xmind_file} 失败: {str(e)}")

if __name__ == '__main__':
    print("开始转换")
    converter = XMindToMarkdown()
    print("转换完成")
    converter.convert_all_xminds()
    print('done')