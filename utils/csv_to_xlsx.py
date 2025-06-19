import pandas as pd
import os
import sys

def convert_csv_to_xlsx():
    """将testcase目录下的所有CSV文件转换为XLSX格式，并删除原CSV文件"""
    # 设置控制台输出编码为utf-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    testcase_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testcase')
    
    # 确保testcase目录存在
    if not os.path.exists(testcase_dir):
        print(f"目录不存在: {testcase_dir}")
        return
    
    # 遍历testcase目录下的所有csv文件
    for filename in os.listdir(testcase_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(testcase_dir, filename)
            print(csv_path)
            xlsx_path = os.path.join(testcase_dir, filename.replace('.csv', '.xlsx'))
            print(xlsx_path)
            try:
                # 读取CSV文件
                df = pd.read_csv(csv_path, encoding='utf-8')
                
                # 保存为XLSX文件
                df.to_excel(xlsx_path, index=False)
                print(f"已将 {filename} 转换为XLSX格式")
                
                # 删除原CSV文件
                os.remove(csv_path)
                print(f"已删除原CSV文件: {filename}")
                
            except Exception as e:
                print(f"处理 {filename} 时出错: {str(e)}")

if __name__ == '__main__':
    convert_csv_to_xlsx()