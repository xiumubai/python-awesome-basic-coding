import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Python基础编程学习',
  description: 'Python基础编程完整学习教程',
  base: process.env.NODE_ENV === 'production' ? '/python-awesome-basic-coding/' : '/',
  outDir: '../dist',
  ignoreDeadLinks: true,
  cleanUrls: true,
  
  themeConfig: {
    logo: '/logo.svg',
    
    nav: [
      { text: '首页', link: '/' },
      { text: '教程', link: '/guide/' },
      { text: '练习', link: '/exercises/' },
      { text: '项目', link: '/projects/' }
    ],
    
    sidebar: {
      '/guide/': [
        {
          text: '🏠 教程导航',
          link: '/guide/',
        },
        {
          text: '1. 基础语法',
          items: [
            { text: '📝 变量和类型', link: '/guide/01-variables-and-types/' },
            { text: '🔢 运算符', link: '/guide/02-operators/' },
            { text: '💬 输入输出', link: '/guide/03-input-output/' },
            { text: '📋 注释', link: '/guide/04-comments/' }
          ]
        },
        {
          text: '2. 控制结构',
          items: [
            { text: '❓ 条件语句', link: '/guide/05-conditions/' },
            { text: '🔄 循环', link: '/guide/06-loops/' },
            { text: '⏹️ 循环控制', link: '/guide/07-loop-control/' }
          ]
        },
        {
          text: '3. 数据结构',
          items: [
            { text: '📋 列表', link: '/guide/08-lists/' },
            { text: '📦 元组', link: '/guide/09-tuples/' },
            { text: '🗂️ 字典', link: '/guide/10-dictionaries/' },
            { text: '🎯 集合', link: '/guide/11-sets/' },
            { text: '🔤 字符串', link: '/guide/12-strings/' }
          ]
        },
        {
          text: '4. 函数',
          items: [
            { text: '🔧 函数基础', link: '/guide/13-functions/' },
            { text: '📊 函数参数', link: '/guide/14-function-parameters/' },
            { text: '🔄 函数返回值', link: '/guide/15-function-returns/' },
            { text: '🌐 作用域', link: '/guide/16-scope/' }
          ]
        },
        {
          text: '5. 文件操作',
          items: [
            { text: '📁 文件操作', link: '/guide/17-file-operations/' }
          ]
        },
        {
          text: '6. 异常处理',
          items: [
            { text: '⚠️ 异常处理', link: '/guide/18-exception-handling/' }
          ]
        },
        {
          text: '7. 面向对象',
          items: [
            { text: '🏗️ 类和对象', link: '/guide/19-classes-objects/' },
            { text: '🔒 封装', link: '/guide/20-encapsulation/' },
            { text: '🧬 继承', link: '/guide/21-inheritance/' },
            { text: '🎭 多态', link: '/guide/22-polymorphism/' }
          ]
        },
        {
          text: '8. 高级特性',
          items: [
            { text: '🎯 装饰器', link: '/guide/23-decorators/' },
            { text: '⚡ 生成器', link: '/guide/24-generators/' },
            { text: '🔄 迭代器', link: '/guide/25-iterators/' },
            { text: '🎪 上下文管理器', link: '/guide/26-context-managers/' }
          ]
        },
        {
          text: '9. 模块和包',
          items: [
            { text: '📦 模块', link: '/guide/27-modules/' },
            { text: '📚 包', link: '/guide/28-packages/' }
          ]
        },
        {
          text: '10. 标准库',
          items: [
            { text: '📚 标准库', link: '/guide/29-standard-library/' }
          ]
        },
        {
          text: '11. 实践项目',
          items: [
            { text: '🎮 游戏项目', link: '/guide/30-games/' },
            { text: '🌐 网络项目', link: '/guide/31-web-projects/' },
            { text: '🏆 挑战项目', link: '/guide/32-challenges/' }
          ]
        }
      ],
      '/guide/01-variables-and-types/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 无', link: '#', class: 'disabled' },
            { text: '➡️ 下一模块: 运算符', link: '/guide/02-operators/' }
          ]
        },
        {
          text: '📝 变量和数据类型',
          items: [
            { text: '📖 模块概述', link: '/guide/01-variables-and-types/' },
            { text: '🔤 基础变量', link: '/guide/01-variables-and-types/01_basic_variables' },
            { text: '🏷️ 数据类型', link: '/guide/01-variables-and-types/02_data_types' },
            { text: '🔄 动态类型', link: '/guide/01-variables-and-types/03_dynamic_typing' },
            { text: '🔀 类型转换', link: '/guide/01-variables-and-types/04_type_conversion' },
            { text: '📝 变量命名', link: '/guide/01-variables-and-types/05_variable_naming' },
            { text: '💪 综合练习', link: '/guide/01-variables-and-types/06_exercises' }
          ]
        }
      ],
      '/guide/02-operators/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 变量和类型', link: '/guide/01-variables-and-types/' },
            { text: '➡️ 下一模块: 输入输出', link: '/guide/03-input-output/' }
          ]
        },
        {
          text: '🔢 运算符',
          items: [
            { text: '📖 模块概述', link: '/guide/02-operators/' },
            { text: '➕ 算术运算符', link: '/guide/02-operators/01_arithmetic_operators' },
            { text: '⚖️ 比较运算符', link: '/guide/02-operators/02_comparison_operators' },
            { text: '🔗 逻辑运算符', link: '/guide/02-operators/03_logical_operators' },
            { text: '📝 赋值运算符', link: '/guide/02-operators/04_assignment_operators' },
            { text: '🔢 位运算符', link: '/guide/02-operators/05_bitwise_operators' },
            { text: '🔍 成员运算符', link: '/guide/02-operators/06_membership_operators' },
            { text: '📊 运算符优先级', link: '/guide/02-operators/07_operator_precedence' },
            { text: '💪 综合练习', link: '/guide/02-operators/08_exercises' }
          ]
        }
      ],
      '/guide/03-input-output/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 运算符', link: '/guide/02-operators/' },
            { text: '➡️ 下一模块: 注释', link: '/guide/04-comments/' }
          ]
        },
        {
          text: '💬 输入输出',
          items: [
            { text: '📖 模块概述', link: '/guide/03-input-output/' },
            { text: '⌨️ 基础输入', link: '/guide/03-input-output/01_basic_input' },
            { text: '✅ 输入验证', link: '/guide/03-input-output/02_input_validation' },
            { text: '📺 基础输出', link: '/guide/03-input-output/03_basic_output' },
            { text: '🎨 格式化输出', link: '/guide/03-input-output/04_formatted_output' },
            { text: '📁 文件输入', link: '/guide/03-input-output/05_file_input' },
            { text: '💾 文件输出', link: '/guide/03-input-output/06_file_output' },
            { text: '🚀 高级IO', link: '/guide/03-input-output/07_advanced_io' },
            { text: '💪 综合练习', link: '/guide/03-input-output/08_exercises' }
          ]
        }
      ],
      '/guide/04-comments/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 输入输出', link: '/guide/03-input-output/' },
            { text: '➡️ 下一模块: 条件语句', link: '/guide/05-conditions/' }
          ]
        },
        {
          text: '📋 注释',
          items: [
            { text: '📖 模块概述', link: '/guide/04-comments/' },
            { text: '📝 单行注释', link: '/guide/04-comments/01_single_line_comments' },
            { text: '📄 多行注释', link: '/guide/04-comments/02_multi_line_comments' },
            { text: '📚 文档字符串', link: '/guide/04-comments/03_docstrings' },
            { text: '📍 行内注释', link: '/guide/04-comments/04_inline_comments' },
            { text: '✨ 注释最佳实践', link: '/guide/04-comments/05_comment_best_practices' },
            { text: '💪 综合练习', link: '/guide/04-comments/06_exercises' }
          ]
        }
      ],
      '/guide/05-conditions/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 注释', link: '/guide/04-comments/' },
            { text: '➡️ 下一模块: 循环', link: '/guide/06-loops/' }
          ]
        },
        {
          text: '❓ 条件语句',
          items: [
            { text: '📖 模块概述', link: '/guide/05-conditions/' },
            { text: '🔰 基础if语句', link: '/guide/05-conditions/02_basic_if_statements' },
            { text: '⚖️ if-else语句', link: '/guide/05-conditions/03_if_else_statements' },
            { text: '🔀 elif多分支', link: '/guide/05-conditions/04_elif_statements' },
            { text: '🏗️ 嵌套条件', link: '/guide/05-conditions/05_nested_conditions' },
            { text: '🔗 逻辑运算符', link: '/guide/05-conditions/06_logical_operators_in_conditions' },
            { text: '⚖️ 比较运算符', link: '/guide/05-conditions/07_comparison_operators' },
            { text: '❓ 条件表达式', link: '/guide/05-conditions/08_conditional_expressions' }
          ]
        }
      ],
      '/guide/06-loops/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 条件语句', link: '/guide/05-conditions/' },
            { text: '➡️ 下一模块: 循环控制', link: '/guide/07-loop-control/' }
          ]
        },
        {
          text: '🔄 循环',
          items: [
            { text: '📖 模块概述', link: '/guide/06-loops/' },
            { text: '🔄 for循环', link: '/guide/06-loops/02_for_loops' },
            { text: '⏳ while循环', link: '/guide/06-loops/03_while_loops' },
            { text: '📊 range函数', link: '/guide/06-loops/04_range_function' },
            { text: '📋 循环遍历列表', link: '/guide/06-loops/05_loop_with_lists' },
            { text: '🔤 循环遍历字符串', link: '/guide/06-loops/06_loop_with_strings' },
            { text: '🏗️ 嵌套循环', link: '/guide/06-loops/07_nested_loops' },
            { text: '🎯 循环模式', link: '/guide/06-loops/08_loop_patterns' },
            { text: '💪 综合练习', link: '/guide/06-loops/09_exercises' }
          ]
        }
      ],
      '/guide/07-loop-control/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 循环', link: '/guide/06-loops/' },
            { text: '➡️ 下一模块: 列表', link: '/guide/08-lists/' }
          ]
        },
        {
          text: '⏹️ 循环控制',
          items: [
            { text: '📖 模块概述', link: '/guide/07-loop-control/01_index' },
            { text: '🛑 break语句', link: '/guide/07-loop-control/02_break_statement' },
            { text: '⏭️ continue语句', link: '/guide/07-loop-control/03_continue_statement' },
            { text: '🔄 else子句', link: '/guide/07-loop-control/04_else_clause' },
            { text: '🎯 循环控制技巧', link: '/guide/07-loop-control/05_loop_control_tips' },
            { text: '💪 综合练习', link: '/guide/07-loop-control/06_exercises' }
          ]
        }
      ],
      '/guide/08-lists/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 循环控制', link: '/guide/07-loop-control/' },
            { text: '➡️ 下一模块: 元组', link: '/guide/09-tuples/' }
          ]
        },
        {
          text: '📋 列表',
          items: [
            { text: '📖 模块概述', link: '/guide/08-lists/' },
            { text: '📝 创建列表', link: '/guide/08-lists/02_creating_lists' },
            { text: '🔍 访问元素', link: '/guide/08-lists/03_accessing_elements' },
            { text: '✏️ 修改列表', link: '/guide/08-lists/04_modifying_lists' },
            { text: '🔧 列表方法', link: '/guide/08-lists/05_list_methods' },
            { text: '🔄 列表遍历', link: '/guide/08-lists/06_list_iteration' },
            { text: '📊 列表推导式', link: '/guide/08-lists/07_list_comprehensions' },
            { text: '🏗️ 嵌套列表', link: '/guide/08-lists/08_nested_lists' },
            { text: '💪 综合练习', link: '/guide/08-lists/09_exercises' }
          ]
        }
      ],
      '/guide/09-tuples/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 列表', link: '/guide/08-lists/' },
            { text: '➡️ 下一模块: 字典', link: '/guide/10-dictionaries/' }
          ]
        },
        {
          text: '📦 元组',
          items: [
            { text: '📖 模块概述', link: '/guide/09-tuples/' },
            { text: '📝 创建元组', link: '/guide/09-tuples/02_creating_tuples' },
            { text: '🔍 访问元素', link: '/guide/09-tuples/03_accessing_elements' },
            { text: '🔧 元组操作', link: '/guide/09-tuples/04_tuple_operations' },
            { text: '📦 元组解包', link: '/guide/09-tuples/05_tuple_unpacking' },
            { text: '⚖️ 元组vs列表', link: '/guide/09-tuples/06_tuple_vs_list' },
            { text: '💪 综合练习', link: '/guide/09-tuples/07_exercises' }
          ]
        }
      ],
      '/guide/10-dictionaries/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 元组', link: '/guide/09-tuples/' },
            { text: '➡️ 下一模块: 集合', link: '/guide/11-sets/' }
          ]
        },
        {
          text: '🗂️ 字典',
          items: [
            { text: '📖 模块概述', link: '/guide/10-dictionaries/index' },
            { text: '📝 创建字典', link: '/guide/10-dictionaries/02_creating_dictionaries' },
            { text: '🔍 访问值', link: '/guide/10-dictionaries/03_accessing_values' },
            { text: '✏️ 修改字典', link: '/guide/10-dictionaries/04_modifying_dictionaries' },
            { text: '🔧 字典方法', link: '/guide/10-dictionaries/05_dictionary_methods' },
            { text: '🔄 字典遍历', link: '/guide/10-dictionaries/06_dictionary_iteration' },
            { text: '🏗️ 嵌套字典', link: '/guide/10-dictionaries/07_nested_dictionaries' },
            { text: '📊 字典推导式', link: '/guide/10-dictionaries/08_dictionary_comprehensions' },
            { text: '💪 综合练习', link: '/guide/10-dictionaries/09_exercises' }
          ]
        }
      ],
      '/guide/11-sets/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 字典', link: '/guide/10-dictionaries/' },
            { text: '➡️ 下一模块: 字符串', link: '/guide/12-strings/' }
          ]
        },
        {
          text: '🎯 集合',
          items: [
            { text: '📖 模块概述', link: '/guide/11-sets/' },
            { text: '📝 创建集合', link: '/guide/11-sets/01_creating_sets' },
            { text: '✏️ 修改集合', link: '/guide/11-sets/02_modifying_sets' },
            { text: '🔧 集合方法', link: '/guide/11-sets/03_set_methods' },
            { text: '🔄 集合运算', link: '/guide/11-sets/04_set_operations' },
            { text: '📊 集合推导式', link: '/guide/11-sets/05_set_comprehensions' },
            { text: '💪 综合练习', link: '/guide/11-sets/06_exercises' }
          ]
        }
      ],
      '/guide/12-strings/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 集合', link: '/guide/11-sets/' },
            { text: '➡️ 下一模块: 函数基础', link: '/guide/13-functions/' }
          ]
        },
        {
          text: '🔤 字符串',
          items: [
            { text: '📖 模块概述', link: '/guide/12-strings/' },
            { text: '📝 创建字符串', link: '/guide/12-strings/01_creating_strings' },
            { text: '🔍 访问字符', link: '/guide/12-strings/02_accessing_characters' },
            { text: '🔧 字符串方法', link: '/guide/12-strings/03_string_methods' },
            { text: '🎨 格式化字符串', link: '/guide/12-strings/04_string_formatting' },
            { text: '✂️ 字符串切片', link: '/guide/12-strings/05_string_slicing' },
            { text: '🔄 字符串遍历', link: '/guide/12-strings/06_string_iteration' },
            { text: '🔍 正则表达式', link: '/guide/12-strings/07_regular_expressions' },
            { text: '💪 综合练习', link: '/guide/12-strings/08_exercises' }
          ]
        }
      ],
      '/guide/13-functions/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 字符串', link: '/guide/12-strings/' },
            { text: '➡️ 下一模块: 函数参数', link: '/guide/14-function-parameters/' }
          ]
        },
        {
          text: '🔧 函数基础',
          items: [
            { text: '📖 模块概述', link: '/guide/13-functions/' },
            { text: '🔧 定义函数', link: '/guide/13-functions/01_defining_functions' },
            { text: '📞 调用函数', link: '/guide/13-functions/02_calling_functions' },
            { text: '📊 函数参数', link: '/guide/13-functions/03_function_parameters' },
            { text: '🔄 返回值', link: '/guide/13-functions/04_return_values' },
            { text: '📚 文档字符串', link: '/guide/13-functions/05_docstrings' },
            { text: '🌐 局部变量', link: '/guide/13-functions/06_local_variables' },
            { text: '💪 综合练习', link: '/guide/13-functions/07_exercises' }
          ]
        }
      ],
      '/guide/14-function-parameters/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 函数基础', link: '/guide/13-functions/' },
            { text: '➡️ 下一模块: 函数返回值', link: '/guide/15-function-returns/' }
          ]
        },
        {
          text: '📊 函数参数',
          items: [
            { text: '📖 模块概述', link: '/guide/14-function-parameters/' },
            { text: '📝 位置参数', link: '/guide/14-function-parameters/01_positional_parameters' },
            { text: '🏷️ 关键字参数', link: '/guide/14-function-parameters/02_keyword_parameters' },
            { text: '⭐ 默认参数', link: '/guide/14-function-parameters/03_default_parameters' },
            { text: '📦 可变参数', link: '/guide/14-function-parameters/04_variable_parameters' },
            { text: '🗂️ 关键字可变参数', link: '/guide/14-function-parameters/05_keyword_variable_parameters' },
            { text: '🔀 参数解包', link: '/guide/14-function-parameters/06_parameter_unpacking' },
            { text: '💪 综合练习', link: '/guide/14-function-parameters/07_exercises' }
          ]
        }
      ],
      '/guide/15-function-returns/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 函数参数', link: '/guide/14-function-parameters/' },
            { text: '➡️ 下一模块: 作用域', link: '/guide/16-scope/' }
          ]
        },
        {
          text: '🔄 函数返回值',
          items: [
            { text: '📖 模块概述', link: '/guide/15-function-returns/' },
            { text: '🔄 基础返回值', link: '/guide/15-function-returns/01_basic_returns' },
            { text: '📦 多个返回值', link: '/guide/15-function-returns/02_multiple_returns' },
            { text: '❓ 条件返回', link: '/guide/15-function-returns/03_conditional_returns' },
            { text: '🔧 返回函数', link: '/guide/15-function-returns/04_returning_functions' },
            { text: '📊 返回数据结构', link: '/guide/15-function-returns/05_returning_data_structures' },
            { text: '💪 综合练习', link: '/guide/15-function-returns/06_exercises' }
          ]
        }
      ],
      '/guide/16-scope/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 函数返回值', link: '/guide/15-function-returns/' },
            { text: '➡️ 下一模块: 文件操作', link: '/guide/17-file-operations/' }
          ]
        },
        {
          text: '🌐 作用域',
          items: [
            { text: '📖 模块概述', link: '/guide/16-scope/' },
            { text: '🏠 局部作用域', link: '/guide/16-scope/01_local_scope' },
            { text: '🌍 全局作用域', link: '/guide/16-scope/02_global_scope' },
            { text: '🔗 global关键字', link: '/guide/16-scope/03_global_keyword' },
            { text: '🏗️ 嵌套作用域', link: '/guide/16-scope/04_nested_scope' },
            { text: '🔒 nonlocal关键字', link: '/guide/16-scope/05_nonlocal_keyword' },
            { text: '🔍 LEGB规则', link: '/guide/16-scope/06_legb_rule' },
            { text: '💪 综合练习', link: '/guide/16-scope/07_exercises' }
          ]
        }
      ],
      '/guide/17-file-operations/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 作用域', link: '/guide/16-scope/' },
            { text: '➡️ 下一模块: 异常处理', link: '/guide/18-exception-handling/' }
          ]
        },
        {
          text: '📁 文件操作',
          items: [
            { text: '📖 模块概述', link: '/guide/17-file-operations/' },
            { text: '📖 打开文件', link: '/guide/17-file-operations/01_opening_files' },
            { text: '📝 读取文件', link: '/guide/17-file-operations/02_reading_files' },
            { text: '✏️ 写入文件', link: '/guide/17-file-operations/03_writing_files' },
            { text: '📂 文件路径', link: '/guide/17-file-operations/04_file_paths' },
            { text: '🗂️ 目录操作', link: '/guide/17-file-operations/05_directory_operations' },
            { text: '📊 CSV文件', link: '/guide/17-file-operations/06_csv_files' },
            { text: '📄 JSON文件', link: '/guide/17-file-operations/07_json_files' },
            { text: '💪 综合练习', link: '/guide/17-file-operations/08_exercises' }
          ]
        }
      ],
      '/guide/18-exception-handling/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 文件操作', link: '/guide/17-file-operations/' },
            { text: '➡️ 下一模块: 类和对象', link: '/guide/19-classes-objects/' }
          ]
        },
        {
          text: '⚠️ 异常处理',
          items: [
            { text: '📖 模块概述', link: '/guide/18-exception-handling/' },
            { text: '🚨 异常基础', link: '/guide/18-exception-handling/01_exception_basics' },
            { text: '🛡️ try-except', link: '/guide/18-exception-handling/02_try_except' },
            { text: '🔄 多重异常', link: '/guide/18-exception-handling/03_multiple_exceptions' },
            { text: '🧹 finally子句', link: '/guide/18-exception-handling/04_finally_clause' },
            { text: '🚀 抛出异常', link: '/guide/18-exception-handling/05_raising_exceptions' },
            { text: '🎯 自定义异常', link: '/guide/18-exception-handling/06_custom_exceptions' },
            { text: '💪 综合练习', link: '/guide/18-exception-handling/07_exercises' }
          ]
        }
      ],
      '/guide/19-classes-objects/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 异常处理', link: '/guide/18-exception-handling/' },
            { text: '➡️ 下一模块: 继承', link: '/guide/20-inheritance/' }
          ]
        },
        {
          text: '🏗️ 类和对象',
          items: [
            { text: '📖 模块概述', link: '/guide/19-classes-objects/' },
            { text: '🏗️ 定义类', link: '/guide/19-classes-objects/01_defining_classes' },
            { text: '🎯 创建对象', link: '/guide/19-classes-objects/02_creating_objects' },
            { text: '🔧 实例方法', link: '/guide/19-classes-objects/03_instance_methods' },
            { text: '📊 实例属性', link: '/guide/19-classes-objects/04_instance_attributes' },
            { text: '🏗️ 构造方法', link: '/guide/19-classes-objects/05_constructor_method' },
            { text: '🔒 私有属性', link: '/guide/19-classes-objects/06_private_attributes' },
            { text: '📚 类属性', link: '/guide/19-classes-objects/07_class_attributes' },
            { text: '💪 综合练习', link: '/guide/19-classes-objects/08_exercises' }
          ]
        }
      ],
      '/guide/20-inheritance/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 类和对象', link: '/guide/19-classes-objects/' },
            { text: '➡️ 下一模块: 多态', link: '/guide/21-polymorphism/' }
          ]
        },
        {
          text: '🧬 继承',
          items: [
            { text: '📖 模块概述', link: '/guide/20-inheritance/' },
            { text: '🧬 基础继承', link: '/guide/20-inheritance/01_basic_inheritance' },
            { text: '🔄 方法重写', link: '/guide/20-inheritance/02_method_overriding' },
            { text: '🆙 super函数', link: '/guide/20-inheritance/03_super_function' },
            { text: '🏗️ 多级继承', link: '/guide/20-inheritance/04_multilevel_inheritance' },
            { text: '🔀 多重继承', link: '/guide/20-inheritance/05_multiple_inheritance' },
            { text: '🔍 MRO方法解析', link: '/guide/20-inheritance/06_mro' },
            { text: '💪 综合练习', link: '/guide/20-inheritance/07_exercises' }
          ]
        }
      ],
      '/guide/21-polymorphism/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 继承', link: '/guide/20-inheritance/' },
            { text: '➡️ 下一模块: 封装', link: '/guide/22-encapsulation/' }
          ]
        },
        {
          text: '🎭 多态',
          items: [
            { text: '📖 模块概述', link: '/guide/21-polymorphism/' },
            { text: '🎭 多态基础', link: '/guide/21-polymorphism/01_polymorphism_basics' },
            { text: '🔄 方法重载', link: '/guide/21-polymorphism/02_method_overloading' },
            { text: '🎯 鸭子类型', link: '/guide/21-polymorphism/03_duck_typing' },
            { text: '🔧 抽象基类', link: '/guide/21-polymorphism/04_abstract_base_classes' },
            { text: '🎨 接口设计', link: '/guide/21-polymorphism/05_interface_design' },
            { text: '💪 综合练习', link: '/guide/21-polymorphism/06_exercises' }
          ]
        }
      ],
      '/guide/22-encapsulation/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 多态', link: '/guide/21-polymorphism/' },
            { text: '➡️ 下一模块: 装饰器', link: '/guide/23-decorators/' }
          ]
        },
        {
          text: '🔒 封装',
          items: [
            { text: '📖 模块概述', link: '/guide/22-encapsulation/' },
            { text: '🔒 访问控制', link: '/guide/22-encapsulation/01_access_control' },
            { text: '🏷️ 属性装饰器', link: '/guide/22-encapsulation/02_property_decorator' },
            { text: '🔧 getter和setter', link: '/guide/22-encapsulation/03_getter_setter' },
            { text: '🛡️ 数据保护', link: '/guide/22-encapsulation/04_data_protection' },
            { text: '🎯 接口设计', link: '/guide/22-encapsulation/05_interface_design' },
            { text: '💪 综合练习', link: '/guide/22-encapsulation/06_exercises' }
          ]
        }
      ],
      '/guide/23-decorators/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 封装', link: '/guide/22-encapsulation/' },
            { text: '➡️ 下一模块: 生成器', link: '/guide/24-generators/' }
          ]
        },
        {
          text: '🎨 装饰器',
          items: [
            { text: '📖 模块概述', link: '/guide/23-decorators/' },
            { text: '🎨 装饰器基础', link: '/guide/23-decorators/01_decorator_basics' },
            { text: '🔧 函数装饰器', link: '/guide/23-decorators/02_function_decorators' },
            { text: '🏗️ 类装饰器', link: '/guide/23-decorators/03_class_decorators' },
            { text: '📊 带参数装饰器', link: '/guide/23-decorators/04_parameterized_decorators' },
            { text: '🔄 装饰器链', link: '/guide/23-decorators/05_decorator_chains' },
            { text: '🛠️ 内置装饰器', link: '/guide/23-decorators/06_built_in_decorators' },
            { text: '💪 综合练习', link: '/guide/23-decorators/07_exercises' }
          ]
        }
      ],
      '/guide/24-generators/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 装饰器', link: '/guide/23-decorators/' },
            { text: '➡️ 下一模块: 迭代器', link: '/guide/25-iterators/' }
          ]
        },
        {
          text: '⚡ 生成器',
          items: [
            { text: '📖 模块概述', link: '/guide/24-generators/' },
            { text: '⚡ 生成器基础', link: '/guide/24-generators/01_generator_basics' },
            { text: '🔄 yield关键字', link: '/guide/24-generators/02_yield_keyword' },
            { text: '📊 生成器表达式', link: '/guide/24-generators/03_generator_expressions' },
            { text: '🔧 生成器方法', link: '/guide/24-generators/04_generator_methods' },
            { text: '🎯 生成器应用', link: '/guide/24-generators/05_generator_applications' },
            { text: '💪 综合练习', link: '/guide/24-generators/06_exercises' }
          ]
        }
      ],
      '/guide/25-iterators/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 生成器', link: '/guide/24-generators/' },
            { text: '➡️ 下一模块: 上下文管理器', link: '/guide/26-context-managers/' }
          ]
        },
        {
          text: '🔄 迭代器',
          items: [
            { text: '📖 模块概述', link: '/guide/25-iterators/' },
            { text: '🔄 迭代器基础', link: '/guide/25-iterators/01_iterator_basics' },
            { text: '🏗️ 自定义迭代器', link: '/guide/25-iterators/02_custom_iterators' },
            { text: '🔧 迭代器协议', link: '/guide/25-iterators/03_iterator_protocol' },
            { text: '📊 内置迭代器', link: '/guide/25-iterators/04_built_in_iterators' },
            { text: '🎯 迭代器应用', link: '/guide/25-iterators/05_iterator_applications' },
            { text: '💪 综合练习', link: '/guide/25-iterators/06_exercises' }
          ]
        }
      ],
      '/guide/26-context-managers/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 迭代器', link: '/guide/25-iterators/' },
            { text: '➡️ 下一模块: 模块', link: '/guide/27-modules/' }
          ]
        },
        {
          text: '🎯 上下文管理器',
          items: [
            { text: '📖 模块概述', link: '/guide/26-context-managers/' },
            { text: '🎯 with语句', link: '/guide/26-context-managers/01_with_statement' },
            { text: '🏗️ 自定义上下文管理器', link: '/guide/26-context-managers/02_custom_context_managers' },
            { text: '🔧 contextlib模块', link: '/guide/26-context-managers/03_contextlib_module' },
            { text: '📊 上下文管理器应用', link: '/guide/26-context-managers/04_context_manager_applications' },
            { text: '💪 综合练习', link: '/guide/26-context-managers/05_exercises' }
          ]
        }
      ],
      '/guide/27-modules/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 上下文管理器', link: '/guide/26-context-managers/' },
            { text: '➡️ 下一模块: 包', link: '/guide/28-packages/' }
          ]
        },
        {
          text: '📦 模块',
          items: [
            { text: '📖 模块概述', link: '/guide/27-modules/' },
            { text: '📦 模块基础', link: '/guide/27-modules/01_module_basics' },
            { text: '📥 导入模块', link: '/guide/27-modules/02_importing_modules' },
            { text: '🏗️ 创建模块', link: '/guide/27-modules/03_creating_modules' },
            { text: '🔍 模块搜索路径', link: '/guide/27-modules/04_module_search_path' },
            { text: '🎯 模块属性', link: '/guide/27-modules/05_module_attributes' },
            { text: '🔄 重新加载模块', link: '/guide/27-modules/06_reloading_modules' },
            { text: '💪 综合练习', link: '/guide/27-modules/07_exercises' }
          ]
        }
      ],
      '/guide/28-packages/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 模块', link: '/guide/27-modules/' },
            { text: '➡️ 下一模块: 标准库', link: '/guide/29-standard-library/' }
          ]
        },
        {
          text: '📚 包',
          items: [
            { text: '📖 模块概述', link: '/guide/28-packages/' },
            { text: '📚 包基础', link: '/guide/28-packages/01_package_basics' },
            { text: '🏗️ 创建包', link: '/guide/28-packages/02_creating_packages' },
            { text: '📥 导入包', link: '/guide/28-packages/03_importing_packages' },
            { text: '🔧 __init__.py文件', link: '/guide/28-packages/04_init_file' },
            { text: '📦 子包', link: '/guide/28-packages/05_subpackages' },
            { text: '🎯 相对导入', link: '/guide/28-packages/06_relative_imports' },
            { text: '💪 综合练习', link: '/guide/28-packages/07_exercises' }
          ]
        }
      ],
      '/guide/29-standard-library/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 包', link: '/guide/28-packages/' },
            { text: '➡️ 下一模块: 项目实战', link: '/guide/30-project-practice/' }
          ]
        },
        {
          text: '📚 标准库',
          items: [
            { text: '📖 模块概述', link: '/guide/29-standard-library/' },
            { text: '🕒 时间和日期', link: '/guide/29-standard-library/01_datetime' },
            { text: '🔢 数学运算', link: '/guide/29-standard-library/02_math' },
            { text: '🎲 随机数', link: '/guide/29-standard-library/03_random' },
            { text: '💻 操作系统', link: '/guide/29-standard-library/04_os' },
            { text: '🌐 网络请求', link: '/guide/29-standard-library/05_urllib' },
            { text: '📊 数据处理', link: '/guide/29-standard-library/06_collections' },
            { text: '🔍 正则表达式', link: '/guide/29-standard-library/07_re' },
            { text: '💪 综合练习', link: '/guide/29-standard-library/08_exercises' }
          ]
        }
      ],
      '/guide/30-project-practice/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 标准库', link: '/guide/29-standard-library/' },
            { text: '➡️ 下一模块: 算法练习', link: '/guide/31-algorithms/' }
          ]
        },
        {
          text: '🚀 项目实战',
          items: [
            { text: '📖 模块概述', link: '/guide/30-project-practice/' },
            { text: '📝 待办事项管理', link: '/guide/30-project-practice/01_todo_manager' },
            { text: '📊 学生成绩管理', link: '/guide/30-project-practice/02_grade_manager' },
            { text: '📚 图书管理系统', link: '/guide/30-project-practice/03_library_system' },
            { text: '🎮 猜数字游戏', link: '/guide/30-project-practice/04_number_game' },
            { text: '📈 数据分析工具', link: '/guide/30-project-practice/05_data_analyzer' },
            { text: '🌐 网页爬虫', link: '/guide/30-project-practice/06_web_scraper' },
            { text: '💪 综合项目', link: '/guide/30-project-practice/07_comprehensive_project' }
          ]
        }
      ],
      '/guide/31-algorithms/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 项目实战', link: '/guide/30-project-practice/' },
            { text: '➡️ 下一模块: 编程挑战', link: '/guide/32-challenges/' }
          ]
        },
        {
          text: '🧮 算法练习',
          items: [
            { text: '📖 模块概述', link: '/guide/31-algorithms/' },
            { text: '🔍 搜索算法', link: '/guide/31-algorithms/01_search_algorithms' },
            { text: '📊 排序算法', link: '/guide/31-algorithms/02_sorting_algorithms' },
            { text: '🔄 递归算法', link: '/guide/31-algorithms/03_recursive_algorithms' },
            { text: '🌳 数据结构', link: '/guide/31-algorithms/04_data_structures' },
            { text: '🎯 动态规划', link: '/guide/31-algorithms/05_dynamic_programming' },
            { text: '📈 贪心算法', link: '/guide/31-algorithms/06_greedy_algorithms' },
            { text: '💪 综合练习', link: '/guide/31-algorithms/07_exercises' }
          ]
        }
      ],
      '/guide/32-challenges/': [
        {
          text: '🧭 快速导航',
          items: [
            { text: '🏠 返回教程首页', link: '/guide/' },
            { text: '⬅️ 上一模块: 算法练习', link: '/guide/31-algorithms/' }
          ]
        },
        {
          text: '🏆 编程挑战',
          items: [
            { text: '📖 模块概述', link: '/guide/32-challenges/' },
            { text: '🥉 初级挑战', link: '/guide/32-challenges/01_beginner_challenges' },
            { text: '🥈 中级挑战', link: '/guide/32-challenges/02_intermediate_challenges' },
            { text: '🥇 高级挑战', link: '/guide/32-challenges/03_advanced_challenges' },
            { text: '🎯 专题挑战', link: '/guide/32-challenges/04_special_challenges' },
            { text: '🏆 竞赛题目', link: '/guide/32-challenges/05_contest_problems' },
            { text: '💪 终极挑战', link: '/guide/32-challenges/06_ultimate_challenges' }
          ]
        }
      ]
    },
    
    socialLinks: [
      { icon: 'github', link: 'https://github.com/your-repo/python-awesome-basic-coding' }
    ],
    
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2024 Python Learning Team'
    },
    
    search: {
      provider: 'local'
    }
  },
  
  markdown: {
    lineNumbers: true,
    config: (md) => {
      // 可以在这里添加markdown插件
    }
  }
})