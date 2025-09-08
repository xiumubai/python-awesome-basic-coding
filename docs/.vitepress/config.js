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