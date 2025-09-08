import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Python基础编程学习',
  description: 'Python基础编程完整学习教程',
  base: '/',
  ignoreDeadLinks: true,
  
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
          text: '基础语法',
          items: [
            { text: '变量和类型', link: '/guide/01-variables-and-types/' },
            { text: '运算符', link: '/guide/02-operators/' },
            { text: '输入输出', link: '/guide/03-input-output/' },
            { text: '注释', link: '/guide/04-comments/' }
          ]
        },
        {
          text: '控制结构',
          items: [
            { text: '条件语句', link: '/guide/05-conditions/' },
            { text: '循环', link: '/guide/06-loops/' },
            { text: '循环控制', link: '/guide/07-loop-control/' }
          ]
        },
        {
          text: '数据结构',
          items: [
            { text: '列表', link: '/guide/08-lists/' },
            { text: '元组', link: '/guide/09-tuples/' },
            { text: '字典', link: '/guide/10-dictionaries/' },
            { text: '集合', link: '/guide/11-sets/' },
            { text: '字符串', link: '/guide/12-strings/' }
          ]
        }
      ],
      '/guide/01-variables-and-types/': [
        {
          text: '变量和数据类型',
          items: [
            { text: '模块概述', link: '/guide/01-variables-and-types/' },
            { text: '基础变量', link: '/guide/01-variables-and-types/basic-variables' },
            { text: '数据类型', link: '/guide/01-variables-and-types/data-types' },
            { text: '动态类型', link: '/guide/01-variables-and-types/dynamic-typing' },
            { text: '类型转换', link: '/guide/01-variables-and-types/type-conversion' },
            { text: '变量命名', link: '/guide/01-variables-and-types/variable-naming' },
            { text: '综合练习', link: '/guide/01-variables-and-types/exercises' }
          ]
        }
      ],
      '/guide/02-operators/': [
        {
          text: '运算符',
          items: [
            { text: '模块概述', link: '/guide/02-operators/' },
            { text: '算术运算符', link: '/guide/02-operators/arithmetic-operators' },
            { text: '比较运算符', link: '/guide/02-operators/comparison-operators' },
            { text: '逻辑运算符', link: '/guide/02-operators/logical-operators' },
            { text: '赋值运算符', link: '/guide/02-operators/assignment-operators' },
            { text: '位运算符', link: '/guide/02-operators/bitwise-operators' },
            { text: '成员运算符', link: '/guide/02-operators/membership-operators' },
            { text: '运算符优先级', link: '/guide/02-operators/operator-precedence' },
            { text: '综合练习', link: '/guide/02-operators/exercises' }
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