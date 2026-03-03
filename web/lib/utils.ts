import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

// 格式化日期
export function formatDate(dateString: string): string {
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  })
}

// 格式化相对时间
export function formatRelativeTime(dateString: string): string {
  const date = new Date(dateString)
  const now = new Date()
  const diffMs = now.getTime() - date.getTime()
  const diffMins = Math.floor(diffMs / 60000)
  const diffHours = Math.floor(diffMs / 3600000)
  const diffDays = Math.floor(diffMs / 86400000)

  if (diffMins < 1) return '刚刚'
  if (diffMins < 60) return `${diffMins}分钟前`
  if (diffHours < 24) return `${diffHours}小时前`
  if (diffDays < 7) return `${diffDays}天前`
  return formatDate(dateString)
}

// 获取状态颜色
export function getStatusColor(status: string): string {
  const colors: Record<string, string> = {
    pending: 'bg-gray-100 text-gray-700',
    stage1_in_progress: 'bg-blue-100 text-blue-700',
    stage1_completed: 'bg-indigo-100 text-indigo-700',
    stage2_in_progress: 'bg-purple-100 text-purple-700',
    stage2_completed: 'bg-green-100 text-green-700',
    cancelled: 'bg-red-100 text-red-700',
  }
  return colors[status] || 'bg-gray-100 text-gray-700'
}

// 获取状态文本
export function getStatusText(status: string): string {
  const texts: Record<string, string> = {
    pending: '待启动',
    stage1_in_progress: '阶段1进行中',
    stage1_completed: '阶段1完成',
    stage2_in_progress: '阶段2进行中',
    stage2_completed: '已完成',
    cancelled: '已取消',
  }
  return texts[status] || status
}

// 获取节点状态颜色
export function getNodeStatusColor(status: string): string {
  const colors: Record<string, string> = {
    pending: 'bg-gray-100 text-gray-600',
    in_progress: 'bg-blue-100 text-blue-700',
    completed: 'bg-green-100 text-green-700',
    failed: 'bg-red-100 text-red-700',
    skipped: 'bg-yellow-100 text-yellow-700',
  }
  return colors[status] || 'bg-gray-100 text-gray-600'
}

// 获取节点状态文本
export function getNodeStatusText(status: string): string {
  const texts: Record<string, string> = {
    pending: '待执行',
    in_progress: '执行中',
    completed: '已完成',
    failed: '失败',
    skipped: '已跳过',
  }
  return texts[status] || status
}
