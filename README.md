# ConfigKit

ConfigKit 是一个用于 Python 字典、YAML 文件和 Tcl 文件/解释器之间进行配置转换的库。它提供了一套完整的工具，用于处理配置数据的转换、合并和管理。

ConfigKit is a library for configuration transformation between Python dictionaries, YAML files, and Tcl files/interpreters. It provides a complete set of tools for converting, merging, and managing configuration data.

## 特性 (Features)

- 在 Python 字典、YAML 文件和 Tcl 文件/解释器之间进行无缝转换
- 支持嵌套结构和复杂数据类型
- 保留类型信息，确保转换的准确性
- 跟踪配置源，提高可追溯性
- 处理混合文件类型（YAML 和 Tcl）
- 提供详细的中英文文档

## 安装 (Installation)

使用 pip 安装：

```bash
pip install configkit
```

## 使用示例 (Usage Examples)

### 基本转换 (Basic Conversion)

```python
from configkit import yamlfiles2tclfile, tclfiles2yamlfile

# 将 YAML 文件转换为 Tcl 文件
yamlfiles2tclfile('config.yaml', output_file='config.tcl')

# 将 Tcl 文件转换为 YAML 文件
tclfiles2yamlfile('config.tcl', output_file='config.yaml')
```

### 混合文件处理 (Mixed File Processing)

```python
from configkit import files2tclfile, files2yamlfile, files2dict

# 将混合的 YAML 和 Tcl 文件转换为 Tcl 文件
files2tclfile('config1.yaml', 'config2.tcl', 'config3.yaml', output_file='combined.tcl')

# 将混合的 YAML 和 Tcl 文件转换为 YAML 文件
files2yamlfile('config1.yaml', 'config2.tcl', 'config3.yaml', output_file='combined.yaml')

# 将混合的 YAML 和 Tcl 文件转换为 Python 字典
config_dict = files2dict('config1.yaml', 'config2.tcl', 'config3.yaml')
```

### Python 字典与 Tcl 解释器之间的转换 (Python Dict <-> Tcl Interpreter)

```python
from tkinter import Tcl
from configkit import dict2tclinterp, tclinterp2dict

# Python 字典
config = {
    'server': {
        'host': 'localhost',
        'port': 8080
    },
    'database': {
        'url': 'postgres://localhost/db'
    }
}

# 将 Python 字典转换为 Tcl 解释器
interp = dict2tclinterp(config)
print(interp.eval('set server(host)'))  # 输出: localhost

# 将 Tcl 解释器转换为 Python 字典
result = tclinterp2dict(interp)
print(result)  # 输出原始字典
```

### 字典合并 (Dictionary Merging)

```python
from configkit import merge_dict

dict1 = {'a': 1, 'b': {'c': 2}}
dict2 = {'b': {'d': 3}, 'e': 4}

# 合并两个字典，支持嵌套结构
result = merge_dict(dict1, dict2)
print(result)  # 输出: {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
```

## 主要功能 (Main Functions)

### 字典操作 (Dictionary Operations)
- `merge_dict`: 合并两个字典，支持嵌套结构
- `yamlfiles2dict`: 将一个或多个 YAML 文件加载到 Python 字典中
- `files2dict`: 将混合的 YAML 和 Tcl 文件转换为 Python 字典

### 值格式转换 (Value Format Conversion)
- `value_format_py2tcl`: 将 Python 值转换为 Tcl 格式
- `value_format_tcl2py`: 将 Tcl 值转换为 Python 格式

### Python <-> Tcl 转换 (Python <-> Tcl Conversion)
- `dict2tclinterp`: 将 Python 字典转换为 Tcl 解释器
- `tclinterp2dict`: 将 Tcl 解释器转换为 Python 字典

### 文件操作 (File Operations)
- `tclinterp2tclfile`: 将 Tcl 解释器写入 Tcl 文件
- `tclfiles2tclinterp`: 将一个或多个 Tcl 文件加载到 Tcl 解释器中
- `tclfiles2yamlfile`: 将一个或多个 Tcl 文件转换为 YAML 文件
- `yamlfiles2tclfile`: 将一个或多个 YAML 文件转换为 Tcl 文件
- `files2tclfile`: 将混合的 YAML 和 Tcl 文件转换为 Tcl 文件
- `files2yamlfile`: 将混合的 YAML 和 Tcl 文件转换为 YAML 文件

## 许可证 (License)

MIT

## 贡献 (Contributing)

欢迎贡献！请随时提交问题或拉取请求。

Contributions are welcome! Feel free to submit issues or pull requests.
