'use client'

import { useState, useEffect } from 'react'
import Link from 'next/link'
import { LayoutDashboard, Users, FileText, Activity, Search, Filter, RefreshCw, Loader2, TrendingUp, Clock, CheckCircle2 } from 'lucide-react'
import { projectApi } from '@/lib/api'
import { Project, ProjectProgress } from '@/types'
import { formatDate, getStatusColor, getStatusText } from '@/lib/utils'

export default function AdminPage() {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)
  const [refreshing, setRefreshing] = useState(false)
  const [searchTerm, setSearchTerm] = useState('')
  const [filterStatus, setFilterStatus] = useState('')
  const [activeTab, setActiveTab] = useState<'overview' | 'projects' | 'nodes'>('overview')

  useEffect(() => {
    loadProjects()
  }, [])

  const loadProjects = async () => {
    setLoading(true)
    const response = await projectApi.list({ limit: 100 })
    if (response.success && response.data) {
      setProjects(response.data)
    }
    setLoading(false)
  }

  const handleRefresh = async () => {
    setRefreshing(true)
    await loadProjects()
    setRefreshing(false)
  }

  const filteredProjects = projects.filter(project => {
    const matchesSearch =
      project.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      project.industry_keyword.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (project.final_topic && project.final_topic.toLowerCase().includes(searchTerm.toLowerCase()))

    const matchesFilter = !filterStatus || project.status === filterStatus

    return matchesSearch && matchesFilter
  })

  // 统计数据
  const stats = {
    total: projects.length,
    inProgress: projects.filter(p => p.status === 'stage1_in_progress' || p.status === 'stage2_in_progress').length,
    completed: projects.filter(p => p.status === 'stage2_completed').length,
    cancelled: projects.filter(p => p.status === 'cancelled').length,
  }

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
            <Link href="/projects" className="text-slate-600 hover:text-slate-900 transition-colors">
              我的项目
            </Link>
            <Link href="/admin" className="text-slate-900 font-medium">
              管理后台
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
              <h1 className="text-3xl font-bold text-slate-900 mb-2">管理后台</h1>
              <p className="text-slate-600">监控和管理所有研究项目</p>
            </div>
            <button
              onClick={handleRefresh}
              disabled={refreshing}
              className="flex items-center space-x-2 px-4 py-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-colors"
            >
              <RefreshCw className={`w-4 h-4 ${refreshing ? 'animate-spin' : ''}`} />
              <span>刷新数据</span>
            </button>
          </div>

          {/* Tab 切换 */}
          <div className="flex space-x-1 bg-slate-100 rounded-lg p-1 mb-6">
            <button
              onClick={() => setActiveTab('overview')}
              className={`flex items-center space-x-2 px-6 py-2 rounded-md font-medium transition-colors ${
                activeTab === 'overview'
                  ? 'bg-white text-slate-900 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <LayoutDashboard className="w-4 h-4" />
              <span>概览</span>
            </button>
            <button
              onClick={() => setActiveTab('projects')}
              className={`flex items-center space-x-2 px-6 py-2 rounded-md font-medium transition-colors ${
                activeTab === 'projects'
                  ? 'bg-white text-slate-900 shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              <FileText className="w-4 h-4" />
              <span>项目管理</span>
            </button>
          </div>

          {activeTab === 'overview' && (
            <>
              {/* 统计卡片 */}
              <div className="grid md:grid-cols-4 gap-6 mb-8">
                <div className="bg-white rounded-xl p-6 shadow-sm">
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-12 h-12 gradient-bg rounded-xl flex items-center justify-center">
                      <LayoutDashboard className="w-6 h-6 text-white" />
                    </div>
                  </div>
                  <div className="text-3xl font-bold text-slate-900 mb-1">{stats.total}</div>
                  <div className="text-sm text-slate-600">总项目数</div>
                </div>

                <div className="bg-white rounded-xl p-6 shadow-sm">
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-12 h-12 bg-blue-500 rounded-xl flex items-center justify-center">
                      <Activity className="w-6 h-6 text-white" />
                    </div>
                  </div>
                  <div className="text-3xl font-bold text-slate-900 mb-1">{stats.inProgress}</div>
                  <div className="text-sm text-slate-600">进行中</div>
                </div>

                <div className="bg-white rounded-xl p-6 shadow-sm">
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-12 h-12 bg-green-500 rounded-xl flex items-center justify-center">
                      <CheckCircle2 className="w-6 h-6 text-white" />
                    </div>
                  </div>
                  <div className="text-3xl font-bold text-slate-900 mb-1">{stats.completed}</div>
                  <div className="text-sm text-slate-600">已完成</div>
                </div>

                <div className="bg-white rounded-xl p-6 shadow-sm">
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-12 h-12 bg-red-500 rounded-xl flex items-center justify-center">
                      <Clock className="w-6 h-6 text-white" />
                    </div>
                  </div>
                  <div className="text-3xl font-bold text-slate-900 mb-1">{stats.cancelled}</div>
                  <div className="text-sm text-slate-600">已取消</div>
                </div>
              </div>

              {/* 最近项目 */}
              <div className="bg-white rounded-xl p-6 shadow-sm">
                <h2 className="text-xl font-semibold text-slate-900 mb-4">最近项目</h2>
                {loading ? (
                  <div className="flex items-center justify-center py-12">
                    <Loader2 className="w-8 h-8 animate-spin text-slate-400" />
                  </div>
                ) : (
                  <div className="space-y-4">
                    {projects.slice(0, 5).map(project => (
                      <Link
                        key={project.id}
                        href={`/projects/${project.id}`}
                        className="flex items-center justify-between p-4 bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors"
                      >
                        <div className="flex items-center space-x-4">
                          <div className="w-10 h-10 gradient-bg rounded-lg flex items-center justify-center text-white">
                            <FileText className="w-5 h-5" />
                          </div>
                          <div>
                            <div className="font-medium text-slate-900">{project.name}</div>
                            <div className="text-sm text-slate-600">{project.industry_keyword}</div>
                          </div>
                        </div>
                        <div className="flex items-center space-x-4">
                          <span className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(project.status)}`}>
                            {getStatusText(project.status)}
                          </span>
                          <span className="text-sm text-slate-600">{formatDate(project.created_at)}</span>
                        </div>
                      </Link>
                    ))}
                  </div>
                )}
              </div>
            </>
          )}

          {activeTab === 'projects' && (
            <>
              {/* 筛选和搜索 */}
              <div className="bg-white rounded-xl p-6 shadow-sm mb-6">
                <div className="flex flex-col md:flex-row gap-4">
                  {/* 搜索框 */}
                  <div className="flex-1 relative">
                    <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-slate-400" />
                    <input
                      type="text"
                      placeholder="搜索项目..."
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
                  <p className="text-slate-600">
                    {searchTerm || filterStatus ? '没有找到匹配的项目' : '暂无项目'}
                  </p>
                </div>
              ) : (
                <div className="bg-white rounded-xl shadow-sm overflow-hidden">
                  <table className="w-full">
                    <thead className="bg-slate-50 border-b border-slate-200">
                      <tr>
                        <th className="px-6 py-4 text-left text-sm font-medium text-slate-700">项目名称</th>
                        <th className="px-6 py-4 text-left text-sm font-medium text-slate-700">行业关键词</th>
                        <th className="px-6 py-4 text-left text-sm font-medium text-slate-700">状态</th>
                        <th className="px-6 py-4 text-left text-sm font-medium text-slate-700">创建时间</th>
                        <th className="px-6 py-4 text-right text-sm font-medium text-slate-700">操作</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-200">
                      {filteredProjects.map(project => (
                        <tr key={project.id} className="hover:bg-slate-50 transition-colors">
                          <td className="px-6 py-4">
                            <Link
                              href={`/projects/${project.id}`}
                              className="font-medium text-slate-900 hover:text-blue-600 transition-colors"
                            >
                              {project.name}
                            </Link>
                          </td>
                          <td className="px-6 py-4 text-slate-600">{project.industry_keyword}</td>
                          <td className="px-6 py-4">
                            <span className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(project.status)}`}>
                              {getStatusText(project.status)}
                            </span>
                          </td>
                          <td className="px-6 py-4 text-slate-600">{formatDate(project.created_at)}</td>
                          <td className="px-6 py-4 text-right">
                            <Link
                              href={`/projects/${project.id}`}
                              className="text-blue-600 hover:text-blue-700 text-sm font-medium transition-colors"
                            >
                              查看详情
                            </Link>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </>
          )}
        </div>
      </main>
    </div>
  )
}
