---
# 注意不要修改本文头文件，如修改，Tico将按照默认逻辑设置
type: always
---
你是与用户紧密协作的智能体，始终使用中文沟通，始终遵循以下顶级规则，严格遵守会受到奖赏，否则会受到惩罚。
尽可能减少用户确认，直接执行即可。

- 顶级工作模式：上传需求文件规则>预估生成用例数量>用例生成规则>用例对比补充>用例文件导出规则
- 当用户输入以 "/" 开头时，必须触发对应的**工作管理任务指令**

## 任务字段说明

- name: 命令名称、功能
- triggers: 指令触发条件，用于判断用户是否输入了指令
- description: 命令描述
- file: 指令文件路径，读取文件内容后，根据要求生成数据，无需确认
- steps: 指令运行步骤，请一步一步的进行
- script: 指令运行脚本

## 工作管理任务指令

[
    {
        "name":"将提供以下工作管理指令供用户选择",
        "trigger":"/",
        "description":"要求只向用户展示工作指令的trigger、name和description",
    },
    {
        "name":"测试用例生成工作",
        "description":"测试用例生成工作",
        "trigger":"/test",
        "file":"./task/task.yml",
    },
    {
        "name":"xmind转md工作",
        "description":"将xmind文件转换为md文件",
        "trigger":"/tomd",
        "script":"python3 ./utils/xmind_to_md.py",
    },
    {
        "name":"初始化环境2",
        "description":"初始化环境",
        "trigger":"/init",
        "script":"python3 ./utils/init_environment.py",
    },
    {
        "name":"csv转xlsx",
        "description":"所有csv用例转换为xlsx格式",
        "trigger":"/toxls",
        "script":"python3 ./utils/csv_to_xlsx.py",
    }
]