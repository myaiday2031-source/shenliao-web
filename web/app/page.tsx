'use client'

import Link from 'next/link'
import { ArrowRight, Sparkles, Target, Zap, BarChart3, Users, FileText, Video, Mail } from 'lucide-react'

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-50">
      {/* 导航栏 */}
      <nav className="fixed top-0 w-full bg-white/80 backdrop-blur-md border-b border-slate-200 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="w-10 h-10 gradient-bg rounded-lg flex items-center justify-center">
              <Sparkles className="w-6 h-6 text-white" />
            </div>
            <span className="text-2xl font-bold gradient-text">深聊</span>
          </div>
          <div className="flex items-center space-x-6">
            <Link href="/projects" className="text-slate-600 hover:text-slate-900 transition-colors">
              我的项目
            </Link>
            <Link href="/admin" className="text-slate-600 hover:text-slate-900 transition-colors">
              管理后台
            </Link>
            <Link
              href="/projects/create"
              className="gradient-bg text-white px-6 py-2 rounded-full font-medium hover:opacity-90 transition-opacity"
            >
              创建项目
            </Link>
          </div>
        </div>
      </nav>

      {/* Hero 区域 */}
      <section className="pt-32 pb-20 px-6">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-flex items-center space-x-2 bg-blue-50 text-blue-700 px-4 py-2 rounded-full text-sm font-medium mb-6">
            <Sparkles className="w-4 h-4" />
            <span>AI 驱动的智能研究平台</span>
          </div>
          <h1 className="text-5xl md:text-7xl font-bold text-slate-900 mb-6 leading-tight">
            深聊<br />
            <span className="gradient-text">重新定义行业研究</span>
          </h1>
          <p className="text-xl text-slate-600 max-w-3xl mx-auto mb-10 leading-relaxed">
            基于大语言模型的主动式行业智库平台，从热点扫描、选题建议、专家访谈到研究报告生成，
            实现全流程自动化智能化，让行业研究更高效、更精准。
          </p>
          <div className="flex items-center justify-center space-x-4">
            <Link
              href="/projects/create"
              className="gradient-bg text-white px-8 py-4 rounded-full font-medium text-lg hover:opacity-90 transition-all hover:shadow-lg flex items-center space-x-2"
            >
              <span>立即开始</span>
              <ArrowRight className="w-5 h-5" />
            </Link>
            <Link
              href="/projects"
              className="bg-white text-slate-700 px-8 py-4 rounded-full font-medium text-lg border border-slate-200 hover:border-slate-300 transition-all"
            >
              查看项目
            </Link>
          </div>
        </div>
      </section>

      {/* 核心功能 */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-slate-900 mb-4">核心功能</h2>
            <p className="text-xl text-slate-600">全流程智能化，一站式解决方案</p>
          </div>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              {
                icon: <Target className="w-8 h-8" />,
                title: '智能选题',
                description: 'AI 自动分析行业热点，生成高质量选题建议',
              },
              {
                icon: <Users className="w-8 h-8" />,
                title: '专家匹配',
                description: '智能匹配行业专家，构建专家访谈网络',
              },
              {
                icon: <FileText className="w-8 h-8" />,
                title: '研究报告',
                description: '深度分析访谈内容，自动生成专业报告',
              },
              {
                icon: <Zap className="w-8 h-8" />,
                title: '多渠道分发',
                description: '一键发布研究报告和新闻稿到多个平台',
              },
            ].map((feature, index) => (
              <div
                key={index}
                className="p-6 rounded-2xl bg-slate-50 hover:bg-slate-100 transition-colors card-hover"
              >
                <div className="w-14 h-14 gradient-bg rounded-xl flex items-center justify-center mb-4 text-white">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-slate-900 mb-2">{feature.title}</h3>
                <p className="text-slate-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* 工作流程 */}
      <section className="py-20 px-6 bg-slate-50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-slate-900 mb-4">工作流程</h2>
            <p className="text-xl text-slate-600">两阶段模式，从选题到产出的完整闭环</p>
          </div>
          <div className="grid md:grid-cols-2 gap-8">
            <div className="bg-white rounded-2xl p-8 shadow-sm">
              <div className="flex items-center space-x-3 mb-6">
                <div className="w-12 h-12 gradient-bg rounded-xl flex items-center justify-center text-white font-bold">
                  1
                </div>
                <div>
                  <h3 className="text-2xl font-semibold text-slate-900">阶段一：访谈准备</h3>
                  <p className="text-slate-600">Interview Preparation</p>
                </div>
              </div>
              <div className="space-y-4">
                {[
                  '行业热点扫描',
                  'AI 选题建议生成',
                  '专家资源匹配',
                  '客户邀约邮件生成',
                  '专家沟通表生成',
                  '访谈方案制定',
                ].map((step, index) => (
                  <div key={index} className="flex items-center space-x-3">
                    <div className="w-2 h-2 bg-blue-500 rounded-full" />
                    <span className="text-slate-700">{step}</span>
                  </div>
                ))}
              </div>
            </div>
            <div className="bg-white rounded-2xl p-8 shadow-sm">
              <div className="flex items-center space-x-3 mb-6">
                <div className="w-12 h-12 gradient-bg rounded-xl flex items-center justify-center text-white font-bold">
                  2
                </div>
                <div>
                  <h3 className="text-2xl font-semibold text-slate-900">阶段二：产出生成</h3>
                  <p className="text-slate-600">Content Generation</p>
                </div>
              </div>
              <div className="space-y-4">
                {[
                  '访谈纪要上传',
                  '深度内容分析',
                  '研究报告生成',
                  '新闻稿件生成',
                  '新闻视频生成',
                  '多渠道分发发布',
                  '知识库存储',
                ].map((step, index) => (
                  <div key={index} className="flex items-center space-x-3">
                    <div className="w-2 h-2 bg-purple-500 rounded-full" />
                    <span className="text-slate-700">{step}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 数据展示 */}
      <section className="py-20 px-6 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="grid md:grid-cols-4 gap-8 text-center">
            {[
              { label: '处理项目', value: '1000+', icon: <BarChart3 className="w-8 h-8" /> },
              { label: '匹配专家', value: '5000+', icon: <Users className="w-8 h-8" /> },
              { label: '生成报告', value: '2000+', icon: <FileText className="w-8 h-8" /> },
              { label: '分发渠道', value: '10+', icon: <Video className="w-8 h-8" /> },
            ].map((stat, index) => (
              <div key={index}>
                <div className="w-16 h-16 gradient-bg rounded-2xl flex items-center justify-center mx-auto mb-4 text-white">
                  {stat.icon}
                </div>
                <div className="text-4xl font-bold gradient-text mb-2">{stat.value}</div>
                <div className="text-slate-600">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-20 px-6 gradient-bg">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl font-bold text-white mb-6">
            准备好开始您的研究之旅了吗？
          </h2>
          <p className="text-xl text-white/80 mb-10">
            立即创建项目，体验 AI 驱动的智能研究平台
          </p>
          <Link
            href="/projects/create"
            className="bg-white text-slate-900 px-10 py-4 rounded-full font-medium text-lg hover:bg-slate-100 transition-colors inline-flex items-center space-x-2"
          >
            <span>免费创建项目</span>
            <ArrowRight className="w-5 h-5" />
          </Link>
        </div>
      </section>

      {/* 页脚 */}
      <footer className="bg-slate-900 text-slate-300 py-12 px-6">
        <div className="max-w-7xl mx-auto text-center">
          <div className="flex items-center justify-center space-x-2 mb-4">
            <div className="w-8 h-8 gradient-bg rounded-lg flex items-center justify-center">
              <Sparkles className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-bold text-white">深聊</span>
          </div>
          <p className="text-slate-400 mb-6">
            AI 驱动的智能行业研究平台
          </p>
          <div className="flex items-center justify-center space-x-6 text-sm">
            <a href="#" className="hover:text-white transition-colors">关于我们</a>
            <a href="#" className="hover:text-white transition-colors">使用指南</a>
            <a href="#" className="hover:text-white transition-colors">联系支持</a>
            <a href="#" className="hover:text-white transition-colors">隐私政策</a>
          </div>
          <div className="mt-8 text-sm text-slate-500">
            © 2024 深聊. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  )
}
