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

export interface CreateProjectParams {
  name: string
  industry_keyword: string
  client_email?: string
}

export interface UpdateProjectStatusParams {
  status?: string
  current_stage?: string
  final_topic?: string
}
