#!/bin/bash
# 强制开启错误检测，确保每一步都正确
set -euo pipefail

# 1. 定义核心路径（避免硬编码出错）
VENV_PATH="/home/guohurui/LibreLog/.venv"
PROJECT_ROOT="/home/guohurui/LibreLog"
PYTHON_BIN="${VENV_PATH}/bin/python"

# 2. 激活uv虚拟环境（确保环境正确）
if [ -f "${VENV_PATH}/bin/activate" ]; then
    source "${VENV_PATH}/bin/activate"
else
    echo "错误：uv虚拟环境不存在！路径：${VENV_PATH}/bin/activate"
    exit 1
fi

# 3. 切换到项目根目录（模块运行的前提）
cd "${PROJECT_ROOT}" || { echo "错误：项目根目录不存在！路径：${PROJECT_ROOT}"; exit 1; }

# 4. 关键：用 -m 以模块方式运行evaluator.py（必选！）
#    格式：python -m 包名.模块名 （parser是包，evaluator是模块）
"${PYTHON_BIN}" -m parser.evaluator \
  --project "Apache,HPC,OpenSSH,Zookeeper,OpenStack,Linux,Proxifier,HealthApp,HDFS,Hadoop,Spark,BGL,Mac,Thunderbird" \
  --sample "3" \
  --use_dashscope_api true

# 5. 退出环境（可选）
deactivate