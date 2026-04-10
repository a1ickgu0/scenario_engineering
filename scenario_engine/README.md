# Scenario Engineering SKILL

这是一个通用的 INCOSE 需求工程 SKILL，专注于从厂商 customer story PDF 或文本中提取需求和利益相关者信息。它可以在 Claude 中使用，也可以应用于其他 LLM 或手工分析流程。

## 📋 目的

本 SKILL 的目标是引导分析人员从 customer story 文本中提取：

1. 文章名、国家、行业、公司名、文档年份
2. 关键利益相关者及其角色
3. 购买要素和业务价值，并基于业务重要性进行评估与排序
4. 各方期望/需求、影响与利益、优先级/冲突、承诺与参与
5. 运行使用构想（operational concept / usage concept）
6. 引用的产品、服务与解决方案

## 🔍 核心能力

### 1. Stakeholder Extraction
- 识别用户、客户、运营方、维护方、支持方、监管机构、社群／公众、供应商等
- 区分角色、期望、价值、风险、优先级和冲突
- 关联生命周期中的参与与验收

### 2. Purchase Element Analysis
- 提取 customer story 中的 3-5 个业务购买要素
- 基于客户业务的重要性对这些购买要素进行评估与排序
- 从客户视角描述“为什么要买”“需要解决什么问题”

### 3. Operational Concept
- 描述系统运行/使用构想
- 提取关键使用场景、环境、交互和成功标准

### 4. Product & Solution Identification
- 抽取 story 中的产品、服务、解决方案、技术或交付形式
- 映射到利益相关者需求

### 5. Traceability
- 所有分析要点须基于原文内容
- 提供原文引用、段落或关键句回溯信息

### 6. PDF Processing Support
- 支持PDF文档的文本提取和分析
- 提供工具集成指南和命令示例
- 保持页面和段落引用以支持追溯

## 🛠️ PDF 处理工具集成

### 推荐工具
- **pdftotext**: Linux/Mac 原生工具，保持布局
- **pdf2txt.py**: Python PDFMiner 工具
- **在线转换器**: 浏览器-based PDF转文本工具
- **OCR工具**: tesseract 用于扫描PDF

### 使用示例
```bash
# 基本文本提取
pdftotext input.pdf output.txt

# 保持布局结构
pdftotext -layout input.pdf output.txt

# 指定页面范围
pdftotext -f 1 -l 5 input.pdf output.txt

# Python 方式
python -c "import pdfminer; pdfminer.high_level.extract_text('input.pdf')"
```

### 处理步骤
1. **提取文本**: 将PDF转换为纯文本格式
2. **添加引用**: 标记页码、章节位置
3. **清理内容**: 移除页眉页脚和格式噪音
4. **验证完整性**: 确保文本可读且内容完整

### 追溯标记
- 页面引用: "Page 3, paragraph 2"
- 章节标记: "Section 2.1: Customer Challenges"
- 直接引用原文内容

```
scenario_engine/
├── SKILL.md                # SKILL 元数据定义
├── README.md               # 当前说明文档
├── tests/                  # 文档验证和测试样例存放目录
└── assets/
    ├── prompts/            # 核心提示词
    │   └── customer-story-analysis.prompt.md
    └── references/         # 分析指南
        └── analysis-guidelines.md
```

## 🚀 开始使用

1. 将厂商 customer story 的 PDF 文本内容复制或转换为可供分析的可读文本
2. 启动本 SKILL，说明你需要提取下面这些维度：
   - 购买要素
   - 利益相关者及期望
   - 影响力与利益
   - 优先级与冲突
   - 承诺与参与
   - 运行使用构想
   - 产品与解决方案
3. 输出应以结构化表格为主，并附上补充说明和原文回溯标记

本 SKILL 适用于 Claude、其他 LLM 平台或手工分析流程。

## 🧭 你现在的第一步

请把第一份厂商 customer story 的文本内容贴给我，或至少给出第一段关键句。我们从这份真实内容开始进行 stakeholder extraction 和需求分析。

