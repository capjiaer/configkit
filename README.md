ConfigKit

ConfigKit 是一个强大的配置文件处理和转换工具包，专注于处理YAML、TCL格式转换以及字典合并操作。

主要功能：

- YAML和TCL格式转换
- 多配置文件合并
- 灵活的字典深度合并
- TCL解释器集成

安装：

pip install configkit

使用示例：

1. YAML处理

from configkit import yaml2dict, yaml2tclfile, yaml2tclinterp

# YAML转字典
yaml_str = """
server:
  host: localhost
  port: 8080
"""
data = yaml2dict(yaml_str)

# YAML直接转TCL文件
yaml2tclfile(yaml_str, "output.tcl")

# 合并多个YAML文件
yaml2tclfile(["base.yaml", "override.yaml"], "merged.tcl")

# YAML转TCL解释器（支持多YAML合并）
interp = yaml2tclinterp([yaml1, yaml2])
print(interp.getvar("server(host)"))

2. 字典处理

from configkit import dict2tcl, dict2tclfile, dict2tclinterp

config = {
    "server": {
        "host": "localhost",
        "port": 8080,
        "settings": {
            "timeout": 30
        }
    }
}

# 转换为TCL命令列表
commands = dict2tcl(config)

# 生成TCL文件
dict2tclfile(config, "config.tcl")

# 获取TCL解释器
interp = dict2tclinterp(config)
value = interp.getvar("server(settings,timeout)")

3. 配置合并

from configkit import deep_merge

# 合并多个配置
base_config = {
    "server": {
        "host": "localhost",
        "port": 8080
    }
}

override_config = {
    "server": {
        "port": 9090,
        "timeout": 30
    }
}

# 方式1：直接合并多个字典
result = deep_merge(base_config, override_config)

# 方式2：合并配置列表
configs = [base_config, override_config]
result = deep_merge(configs)

特性：

1. 灵活的格式转换：
   - YAML到TCL的无缝转换
   - 支持复杂的嵌套结构
   - 自动处理特殊字符和空格

2. 智能的配置合并：
   - 深度递归合并
   - 保留未覆盖的配置
   - 支持多种合并方式

3. 完整的错误处理：
   - YAML解析错误检测
   - 文件操作异常处理
   - 类型安全检查

许可证：
MIT