'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { ArrowLeft, RefreshCw, Play, Pause, Loader2, CheckCircle2, Clock, AlertCircle } from 'lucide-react'
import { projectApi } from '@/lib/api'
import { ProjectProgress } from '@/types'
import { formatDate, getStatusColor, getStatusText, getNodeStatusColor, getNodeStatusText } from '@/lib/utils'

export default function ProjectDetailPage({ params }: { params: { id: string } }) {
  const router = useRouter()
  const [loading, setLoading] = useState(true)
  const [refreshing, setRefreshing] = useState(false)
  const [progress, setProgress] = useState<ProjectProgress | null>(null)

  const loadProjectProgress = async () => {
    const response = await projectApi.getProgress(Number(params.id))
    if (response.success && response.data) {
      setProgress(response.data)
    }
    setLoading(false)
  }

  useEffect(() => {
    loadProjectProgress()
  }, [params.id])

  const handleRefresh = async () => {
    setRefreshing(true)
    await loadProjectProgress()
    setRefreshing(false)
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <Loader2 className="w-12 h-12 animate-spin text-slate-400" />
      </div>
    )
  }

  if (!progress) {
    return (
      <div className="min-h-screen bg-slate-50 flex items-center justify-center">
        <div className="text-center">
          <AlertCircle className="w-16 h-16 text-slate-300 mx-auto mb-4" />
          <h2 className="text-xl font-semibold text-slate-900 mb-2">项目不存在</h2>
          <Link
            href="/projects"
            className="gradient-bg text-white px-6 py-3 rounded-lg font-medium hover:opacity-90 transition-opacity"
          >
            返回项目列表
          </Link>
        </div>
      </div>
    )
  }

  const project = progress.project
  const nodes = progress.nodes

  // 计算各阶段的节点
  const stage1Nodes = nodes.filter(n =>
    ['hotspot_scan', 'topic_suggestion_generation', 'topic_confirmation',
     'expert_matching', 'manual_expert_import', 'expert_list_merge',
     'client_invitation', 'communication_table', 'interview_plan',
     'project_update_status'].includes(n.node_name)
  )

  const stage2Nodes = nodes.filter(n =>
    ['interview_minutes_upload', 'deep_analysis', 'research_report',
     'encrypted_email_send', 'news_article', 'news_article_publish',
     'news_video_generation', 'news_video_publish', 'knowledge_storage'].includes(n.node_name)
  )

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
        <div className="max-w-7xl mx-auto">
          {/* 返回按钮 */}
          <div className="flex items-center justify-between mb-6">
            <Link
              href="/projects"
              className="inline-flex items-center space-x-2 text-slate-600 hover:text-slate-900 transition-colors"
            >
              <ArrowLeft className="w-5 h-5" />
              <span>返回项目列表</span>
            </Link>
            <button
              onClick={handleRefresh}
              disabled={refreshing}
              className="flex items-center space-x-2 px-4 py-2 text-slate-600 hover:text-slate-900 hover:bg-slate-100 rounded-lg transition-colors"
            >
              <RefreshCw className={`w-4 h-4 ${refreshing ? 'animate-spin' : ''}`} />
              <span>刷新</span>
            </button>
          </div>

          {/* 项目信息卡片 */}
          <div className="bg-white rounded-xl p-8 shadow-sm mb-6">
            <div className="flex items-start justify-between mb-6">
              <div>
                <h1 className="text-3xl font-bold text-slate-900 mb-2">{project.name}</h1>
                <div className="flex items-center space-x-3 mb-4">
                  <span className={`px-4 py-1.5 rounded-full text-sm font-medium ${getStatusColor(project.status)}`}>
                    {getStatusText(project.status)}
                  </span>
                  {project.current_stage && (
                    <span className="text-slate-600">
                      当前阶段：{project.current_stage === 'stage1' ? '阶段1：访谈准备' : '阶段2：产出生成'}
                    </span>
                  )}
                </div>
              </div>
              <div className="text-right">
                <div className="text-3xl font-bold gradient-text mb-1">{progress.progress}%</div>
                <div className="text-sm text-slate-600">完成进度</div>
              </div>
            </div>

            <div className="grid md:grid-cols-2 gap-6">
              <div>
                <div className="text-sm text-slate-600 mb-1">行业关键词</div>
                <div className="text-slate-900 font-medium">{project.industry_keyword}</div>
              </div>
              {project.final_topic && (
                <div>
                  <div className="text-sm text-slate-600 mb-1">选题</div>
                  <div className="text-slate-900 font-medium">{project.final_topic}</div>
                </div>
              )}
              {project.client_email && (
                <div>
                  <div className="text-sm text-slate-600 mb-1">客户邮箱</div>
                  <div className="text-slate-900 font-medium">{project.client_email}</div>
                </div>
              )}
              <div>
                <div className="text-sm text-slate-600 mb-1">创建时间</div>
                <div className="text-slate-900 font-medium">{formatDate(project.created_at)}</div>
              </div>
            </div>
          </div>

          {/* 节点执行进度 */}
          <div className="grid md:grid-cols-2 gap-6">
            {/* 阶段1：访谈准备 */}
            <div className="bg-white rounded-xl p-6 shadow-sm">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-semibold text-slate-900">阶段1：访谈准备</h2>
                <div className="text-sm text-slate-600">
                  {stage1Nodes.filter(n => n.status === 'completed').length}/{stage1Nodes.length} 完成
                </div>
              </div>
              <div className="space-y-3">
                {stage1Nodes.map(node => (
                  <div
                    key={node.id}
                    className="flex items-center justify-between p-3 bg-slate-50 rounded-lg"
                  >
                    <div className="flex items-center space-x-3">
                      {node.status === 'completed' && <CheckCircle2 className="w-5 h-5 text-green-500" />}
                      {node.status === 'in_progress' && <Clock className="w-5 h-5 text-blue-500 animate-pulse" />}
                      {node.status === 'failed' && <AlertCircle className="w-5 h-5 text-red-500" />}
                      {node.status === 'pending' && <Clock className="w-5 h-5 text-slate-400" />}
                      <span className="text-slate-900 font-medium">{node.node_name}</span>
                    </div>
                    <span className={`px-3 py-1 rounded-full text-xs font-medium ${getNodeStatusColor(node.status)}`}>
                      {getNodeStatusText(node.status)}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* 阶段2：产出生成 */}
            <div className="bg-white rounded-xl p-6 shadow-sm">
              <div className="flex items-center justify-between mb-4">
                <h2 className="text-xl font-semibold text-slate-900">阶段2：产出生成</h2>
                <div className="text-sm text-slate-600">
                  {stage2Nodes.filter(n => n.status === 'completed').length}/{stage2Nodes.length} 完成
                </div>
              </div>
              <div className="space-y-3">
                {stage2Nodes.map(node => (
                  <div
                    key={node.id}
                    className="flex items-center justify-between p-3 bg-slate-50 rounded-lg"
                  >
                    <div className="flex items-center space-x-3">
                      {node.status === 'completed' && <CheckCircle2 className="w-5 h-5 text-green-500" />}
                      {node.status === 'in_progress' && <Clock className="w-5 h-5 text-blue-500 animate-pulse" />}
                      {node.status === 'failed' && <AlertCircle className="w-5 h-5 text-red-500" />}
                      {node.status === 'pending' && <Clock className="w-5 h-5 text-slate-400" />}
                      <span className="text-slate-900 font-medium">{node.node_name}</span>
                    </div>
                    <span className={`px-3 py-1 rounded-full text-xs font-medium ${getNodeStatusColor(node.status)}`}>
                      {getNodeStatusText(node.status)}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}
