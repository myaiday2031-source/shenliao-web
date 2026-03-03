'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { ArrowLeft, Plus, Loader2, CheckCircle2 } from 'lucide-react'
import { projectApi } from '@/lib/api'

export default function CreateProjectPage() {
  const router = useRouter()
  const [loading, setLoading] = useState(false)
  const [formData, setFormData] = useState({
    name: '',
    industry_keyword: '',
    client_email: '',
  })
  const [errors, setErrors] = useState<Record<string, string>>({})

  const validateForm = () => {
    const newErrors: Record<string, string> = {}

    if (!formData.name.trim()) {
      newErrors.name = '请输入项目名称'
    }
    if (!formData.industry_keyword.trim()) {
      newErrors.industry_keyword = '请输入行业关键词'
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!validateForm()) {
      return
    }

    setLoading(true)
    const response = await projectApi.create(formData)

    if (response.success && response.data) {
      // 跳转到项目详情页
      router.push(`/projects/${response.data.id}`)
    } else {
      setErrors({
        submit: response.error || '创建项目失败，请稍后重试'
      })
      setLoading(false)
    }
  }

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
    // 清除该字段的错误
    if (errors[name]) {
      setErrors(prev => {
        const newErrors = { ...prev }
        delete newErrors[name]
        return newErrors
      })
    }
  }

  return (
    <div className="min-h-screen bg-slate-50">
      {/* 导航栏 */}
      <nav className="fixed top-0 w-full bg-white/80 backdrop-blur-md border-b border-slate-200 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <Link href="/" className="flex items-center space-x-2">
            <div className="w-8 h-8 gradient-bg rounded-lg flex items-center justify-center">
              <CheckCircle2 className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-bold text-slate-900">深聊</span>
          </Link>
          <div className="flex items-center space-x-6">
            <Link href="/" className="text-slate-600 hover:text-slate-900 transition-colors">
              首页
            </Link>
            <Link href="/projects" className="text-slate-900 font-medium">
              我的项目
            </Link>
            <Link href="/admin" className="text-slate-600 hover:text-slate-900 transition-colors">
              管理后台
            </Link>
          </div>
        </div>
      </nav>

      {/* 主内容 */}
      <main className="pt-24 pb-12 px-6">
        <div className="max-w-3xl mx-auto">
          {/* 返回按钮 */}
          <Link
            href="/projects"
            className="inline-flex items-center space-x-2 text-slate-600 hover:text-slate-900 mb-6 transition-colors"
          >
            <ArrowLeft className="w-5 h-5" />
            <span>返回项目列表</span>
          </Link>

          {/* 页面标题 */}
          <div className="mb-8">
            <h1 className="text-3xl font-bold text-slate-900 mb-2">创建新项目</h1>
            <p className="text-slate-600">填写以下信息创建新的研究项目</p>
          </div>

          {/* 表单 */}
          <form onSubmit={handleSubmit} className="bg-white rounded-xl p-8 shadow-sm">
            {/* 项目名称 */}
            <div className="mb-6">
              <label htmlFor="name" className="block text-sm font-medium text-slate-700 mb-2">
                项目名称 <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleInputChange}
                placeholder="例如：人工智能行业研究报告"
                className={`w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent ${
                  errors.name ? 'border-red-500' : 'border-slate-200'
                }`}
              />
              {errors.name && (
                <p className="mt-2 text-sm text-red-600">{errors.name}</p>
              )}
            </div>

            {/* 行业关键词 */}
            <div className="mb-6">
              <label htmlFor="industry_keyword" className="block text-sm font-medium text-slate-700 mb-2">
                行业关键词 <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                id="industry_keyword"
                name="industry_keyword"
                value={formData.industry_keyword}
                onChange={handleInputChange}
                placeholder="例如：人工智能、机器学习、深度学习"
                className={`w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent ${
                  errors.industry_keyword ? 'border-red-500' : 'border-slate-200'
                }`}
              />
              {errors.industry_keyword && (
                <p className="mt-2 text-sm text-red-600">{errors.industry_keyword}</p>
              )}
              <p className="mt-2 text-sm text-slate-500">
                系统将基于此关键词搜索行业热点并生成选题建议
              </p>
            </div>

            {/* 客户邮箱 */}
            <div className="mb-6">
              <label htmlFor="client_email" className="block text-sm font-medium text-slate-700 mb-2">
                客户邮箱（可选）
              </label>
              <input
                type="email"
                id="client_email"
                name="client_email"
                value={formData.client_email}
                onChange={handleInputChange}
                placeholder="例如：client@example.com"
                className={`w-full px-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent ${
                  errors.client_email ? 'border-red-500' : 'border-slate-200'
                }`}
              />
              {errors.client_email && (
                <p className="mt-2 text-sm text-red-600">{errors.client_email}</p>
              )}
              <p className="mt-2 text-sm text-slate-500">
                填写后，研究报告将通过加密邮件发送至该邮箱
              </p>
            </div>

            {/* 错误提示 */}
            {errors.submit && (
              <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg">
                <p className="text-sm text-red-700">{errors.submit}</p>
              </div>
            )}

            {/* 提交按钮 */}
            <div className="flex items-center justify-end space-x-4">
              <Link
                href="/projects"
                className="px-6 py-3 border border-slate-200 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors"
              >
                取消
              </Link>
              <button
                type="submit"
                disabled={loading}
                className="gradient-bg text-white px-6 py-3 rounded-lg font-medium hover:opacity-90 transition-opacity disabled:opacity-50 flex items-center space-x-2"
              >
                {loading ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    <span>创建中...</span>
                  </>
                ) : (
                  <>
                    <Plus className="w-5 h-5" />
                    <span>创建项目</span>
                  </>
                )}
              </button>
            </div>
          </form>
        </div>
      </main>
    </div>
  )
}
