## 项目文件说明

- `configkit.egg-info/`: Python包元数据目录，由setuptools在安装时自动生成
  - 包含包名称、版本、依赖等元信息
  - 通常应该添加到`.gitignore`中
  - 可以安全删除，会在下次安装时重新生成
# ConfigKit - Python配置转换工具包

ConfigKit 提供了强大的配置格式转换功能，支持YAML、TCL和Python字典之间的相互转换。

## 主要功能

- YAML ↔ TCL 双向转换
- Python字典 ↔ TCL 双向转换
- 多配置文件合并
- 嵌套结构支持
- 完整的错误处理

## 安装

## 安装方法

### 开发模式安装（推荐开发时使用）

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/configkit.git
cd configkit
```

2. 使用pip安装（可编辑模式）：
```bash
pip install -e .
```

### 正式安装

1. 直接从本地安装：
```bash
pip install .
```

2. 或者从GitHub安装最新版本：
```bash
pip install git+https://github.com/yourusername/configkit.git
```

### 验证安装

安装完成后可以运行测试验证：
```bash
python -m unittest discover tests
```

或者在Python中导入验证：
```python
import configkit
print(configkit.__version__)
```
```bash
pip install configkit
```

## 使用示例

### YAML处理

```python
from configkit.yaml_converter import (
    yaml2dict,
    yamlfiles2tclfile,
    yaml2tclinterp
)

# YAML字符串转字典
data = yaml2dict("""
server:
  host: localhost
  port: 8080
""")

# 多YAML文件转TCL文件
yamlfiles2tclfile(["base.yaml", "override.yaml"], "merged.tcl")

# YAML转TCL解释器
interp = yaml2tclinterp(yaml_str)
print(interp.getvar("server(host)"))  # 输出: "localhost"
```

### 字典处理

```python
from configkit.dict_converter import (
    dict2tclsetcmd,
    dict2tclfile,
    dict2tclinterp,
    tclinterp2dict
)

config = {
    "server": {
        "host": "localhost",
        "port": 8080,
        "nested": {"timeout": 30}
    }
}

# 字典转TCL命令
commands = dict2tclsetcmd(config)
# ['set server(host) "localhost"', 'set server(port) 8080', 'set server(nested,timeout) 30']

# 字典转TCL文件
dict2tclfile(config, "output.tcl")

# 字典转TCL解释器
interp = dict2tclinterp(config)
print(interp.getvar("server(nested,timeout)"))  # 输出: "30"

# TCL解释器转回字典
new_dict = tclinterp2dict(interp)
```

## 特性

1. **智能格式转换**
   - 自动处理嵌套结构
   - 字符串值自动加引号
   - 支持列表和字典值

2. **完整测试覆盖**
   - 单元测试覆盖所有主要功能
   - 边界条件测试
   - 错误处理测试

3. **错误处理**
   - YAML解析错误
   - 文件操作异常
   - TCL语法错误

## 运行测试

```bash
python -m unittest discover tests
```

## 许可证

MIT