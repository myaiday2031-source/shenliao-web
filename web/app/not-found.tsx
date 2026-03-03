import Link from 'next/link'
import { Home, ArrowLeft } from 'lucide-react'

export default function NotFound() {
  return (
    <div className="min-h-screen bg-slate-50 flex items-center justify-center px-6">
      <div className="text-center">
        <div className="w-24 h-24 gradient-bg rounded-full flex items-center justify-center mx-auto mb-6">
          <span className="text-5xl font-bold text-white">404</span>
        </div>
        <h1 className="text-3xl font-bold text-slate-900 mb-2">页面不存在</h1>
        <p className="text-slate-600 mb-8">抱歉，您访问的页面不存在</p>
        <div className="flex items-center justify-center space-x-4">
          <Link
            href="/"
            className="gradient-bg text-white px-6 py-3 rounded-lg font-medium hover:opacity-90 transition-opacity flex items-center space-x-2"
          >
            <Home className="w-5 h-5" />
            <span>返回首页</span>
          </Link>
          <Link
            href="/projects"
            className="bg-white text-slate-700 px-6 py-3 rounded-lg font-medium border border-slate-200 hover:border-slate-300 transition-colors flex items-center space-x-2"
          >
            <ArrowLeft className="w-5 h-5" />
            <span>返回项目列表</span>
          </Link>
        </div>
      </div>
    </div>
  )
}
