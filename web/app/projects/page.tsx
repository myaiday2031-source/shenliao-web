'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import { Plus, Search, Filter, Clock, CheckCircle2, XCircle, Loader2 } from 'lucide-react'
import { projectApi } from '@/lib/api'
import { Project } from '@/types'
import { formatDate, getStatusColor, getStatusText } from '@/lib/utils'

export default function ProjectsPage() {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [filterStatus, setFilterStatus] = useState('')

  useEffect(() => {
    loadProjects()
  }, [])

  const loadProjects = async () => {
    setLoading(true)
    const response = await projectApi.list({ limit: 50 })
    if (response.success && response.data) {
      setProjects(response.data)
    }
    setLoading(false)
  }

  const filteredProjects = projects.filter(project => {
    const matchesSearch =
      project.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      project.industry_keyword.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (project.final_topic && project.final_topic.toLowerCase().includes(searchTerm.toLowerCase()))

    const matchesFilter = !filterStatus || project.status === filterStatus

    return matchesSearch && matchesFilter
  })

  const statusOptions = [
    { value: '', label: '全部状态' },
    { value: 'pending', label: '待启动' },
    { value: 'stage1_in_progress', label: '阶段1进行中' },
    { value: 'stage1_completed', label: '阶段1完成' },
    { value: 'stage2_in_progress', label: '阶段2进行中' },
    { value: 'stage2_completed', label: '已完成' },
    { value: 'cancelled', label: '已取消' },
  ]

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
            <Link
              href="/projects/create"
              className="gradient-bg text-white px-4 py-2 rounded-full font-medium text-sm hover:opacity-90 transition-opacity"
            >
              创建项目
            </Link>
          </div>
        </div>
      </nav>

      {/* 主内容 */}
      <main className="pt-24 pb-12 px-6">
        <div className="max-w-7xl mx-auto">
          {/* 页面标题 */}
          <div className="flex items-center justify-between mb-8">
            <div>
              <h1 className="text-3xl font-bold text-slate-900 mb-2">我的项目</h1>
              <p className="text-slate-600">管理和查看您的研究项目</p>
            </div>
            <Link
              href="/projects/create"
              className="gradient-bg text-white px-6 py-3 rounded-lg font-medium hover:opacity-90 transition-opacity flex items-center space-x-2"
            >
              <Plus className="w-5 h-5" />
              <span>创建项目</span>
            </Link>
          </div>

          {/* 筛选和搜索 */}
          <div className="bg-white rounded-xl p-6 shadow-sm mb-6">
            <div className="flex flex-col md:flex-row gap-4">
              {/* 搜索框 */}
              <div className="flex-1 relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-slate-400" />
                <input
                  type="text"
                  placeholder="搜索项目名称、行业关键词或选题..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-10 pr-4 py-2.5 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>

              {/* 状态筛选 */}
              <div className="relative">
                <Filter className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-slate-400" />
                <select
                  value={filterStatus}
                  onChange={(e) => setFilterStatus(e.target.value)}
                  className="pl-10 pr-10 py-2.5 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white appearance-none"
                >
                  {statusOptions.map(option => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
              </div>
            </div>
          </div>

          {/* 项目列表 */}
          {loading ? (
            <div className="flex items-center justify-center py-20">
              <Loader2 className="w-8 h-8 animate-spin text-slate-400" />
            </div>
          ) : filteredProjects.length === 0 ? (
            <div className="bg-white rounded-xl p-12 text-center shadow-sm">
              <XCircle className="w-16 h-16 text-slate-300 mx-auto mb-4" />
              <h3 className="text-xl font-semibold text-slate-900 mb-2">暂无项目</h3>
              <p className="text-slate-600 mb-6">
                {searchTerm || filterStatus ? '没有找到匹配的项目' : '开始创建您的第一个研究项目吧'}
              </p>
              <Link
                href="/projects/create"
                className="gradient-bg text-white px-6 py-3 rounded-lg font-medium hover:opacity-90 transition-opacity inline-flex items-center space-x-2"
              >
                <Plus className="w-5 h-5" />
                <span>创建项目</span>
              </Link>
            </div>
          ) : (
            <div className="grid gap-4">
              {filteredProjects.map(project => (
                <Link
                  key={project.id}
                  href={`/projects/${project.id}`}
                  className="bg-white rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow"
                >
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <div className="flex items-center space-x-3 mb-2">
                        <h3 className="text-xl font-semibold text-slate-900">{project.name}</h3>
                        <span className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(project.status)}`}>
                          {getStatusText(project.status)}
                        </span>
                      </div>
                      <p className="text-slate-600 mb-3">
                        <span className="font-medium">行业关键词：</span>{project.industry_keyword}
                      </p>
                      {project.final_topic && (
                        <p className="text-slate-600 mb-3">
                          <span className="font-medium">选题：</span>{project.final_topic}
                        </p>
                      )}
                      <div className="flex items-center space-x-4 text-sm text-slate-500">
                        <div className="flex items-center space-x-1">
                          <Clock className="w-4 h-4" />
                          <span>创建于 {formatDate(project.created_at)}</span>
                        </div>
                        {project.client_email && (
                          <div className="flex items-center space-x-1">
                            <span>客户邮箱：{project.client_email}</span>
                          </div>
                        )}
                      </div>
                    </div>
                    <div className="text-slate-400">
                      <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                      </svg>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          )}
        </div>
      </main>
    </div>
  )
}
