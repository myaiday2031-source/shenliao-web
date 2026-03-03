"""
热点扫描节点：使用web-search技能搜索行业热点
"""
from typing import Dict, List
from coze_coding_dev_sdk import SearchClient
from coze_coding_utils.runtime_ctx.context import Context, new_context
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from graphs.state import HotspotScanInput, HotspotScanOutput


def hotspot_scan_node(state: HotspotScanInput, config: RunnableConfig, runtime: Runtime[Context]) -> HotspotScanOutput:
    """
    title: 热点扫描
    desc: 使用网络搜索功能，扫描指定行业的最新热点、技术难点、政策关注点等信息
    integrations: web-search
    """
    ctx = runtime.context
    
    try:
        # 初始化搜索客户端
        client = SearchClient(ctx=ctx)
        
        # 执行网络搜索，获取最新热点信息
        query = f"{state.industry_keyword} 最新热点 技术趋势 行业动态"
        response = client.web_search_with_summary(query=query, count=10)
        
        # 提取搜索结果
        search_details = []
        if response.web_items:
            for item in response.web_items:
                search_details.append({
                    "title": item.title,
                    "url": item.url,
                    "site_name": item.site_name,
                    "snippet": item.snippet,
                    "summary": item.summary if hasattr(item, 'summary') else item.snippet
                })
        
        # 整理搜索结果摘要
        search_summary = response.summary if response.summary else "未找到AI生成的摘要"
        
        # 如果没有AI摘要，手动生成一个
        if not search_summary or search_summary == "未找到AI生成的摘要":
            summaries = [f"- {item['title']}: {item['summary'][:100]}" for item in search_details[:5]]
            search_summary = f"找到 {len(search_details)} 条相关结果：\n" + "\n".join(summaries)
        
        return HotspotScanOutput(
            search_results=search_summary,
            search_details=search_details
        )
        
    except Exception as e:
        raise Exception(f"热点扫描失败: {str(e)}")
