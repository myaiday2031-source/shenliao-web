// API 响应类型定义
export interface Project {
  id: number
  name: string
  industry_keyword: string
  final_topic?: string
  client_email?: string
  status: 'pending' | 'stage1_in_progress' | 'stage1_completed' | 'stage2_in_progress' | 'stage2_completed' | 'cancelled'
  current_stage?: string
  created_at: string
  updated_at: string
  completed_at?: string
  metadata_json?: any
}

export interface NodeExecution {
  id: number
  project_id: number
  node_name: string
  status: 'pending' | 'in_progress' | 'completed' | 'failed' | 'skipped'
  started_at?: string
  completed_at?: string
  error_message?: string
  output_json?: any
  created_at: string
  updated_at: string
}

export interface ProjectProgress {
  project: Project
  nodes: NodeExecution[]
  progress: number
}

export interface ApiResponse<T> {
  success: boolean
  data?: T
  error?: string
}

// API 基础 URL
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

// 通用请求函数
async function request<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<ApiResponse<T>> {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const data = await response.json()
    return { success: true, data }
  } catch (error) {
    console.error('API request error:', error)
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error'
    }
  }
}

// 项目相关 API
export const projectApi = {
  // 创建项目
  create: (params: {
    name: string
    industry_keyword: string
    client_email?: string
  }) =>
    request<Project>('POST', '/api/projects/create', {
      method: 'POST',
      body: JSON.stringify(params),
    }),

  // 获取项目列表
  list: (params?: {
    status?: string
    limit?: number
    offset?: number
  }) => {
    const query = new URLSearchParams()
    if (params?.status) query.append('status', params.status)
    if (params?.limit) query.append('limit', params.limit.toString())
    if (params?.offset) query.append('offset', params.offset.toString())
    return request<Project[]>('GET', `/api/projects/list?${query.toString()}`)
  },

  // 获取单个项目
  get: (id: number) =>
    request<Project>('GET', `/api/projects/${id}`),

  // 更新项目状态
  updateStatus: (id: number, params: {
    status?: string
    current_stage?: string
    final_topic?: string
  }) =>
    request<Project>('PUT', `/api/projects/${id}/status`, {
      method: 'PUT',
      body: JSON.stringify(params),
    }),

  // 取消项目
  cancel: (id: number) =>
    request<Project>('PUT', `/api/projects/${id}/cancel`, {
      method: 'PUT',
    }),

  // 获取项目进度
  getProgress: (id: number) =>
    request<ProjectProgress>('GET', `/api/projects/${id}/progress`),
}

// 节点执行相关 API
export const nodeExecutionApi = {
  // 记录节点执行
  record: (projectId: number, params: {
    node_name: string
    status: 'pending' | 'in_progress' | 'completed' | 'failed' | 'skipped'
    error_message?: string
    output_json?: any
  }) =>
    request<NodeExecution>('POST', `/api/projects/${projectId}/nodes`, {
      method: 'POST',
      body: JSON.stringify(params),
    }),

  // 获取项目节点执行记录
  list: (projectId: number) =>
    request<NodeExecution[]>('GET', `/api/projects/${projectId}/nodes`),
}
