from coze_coding_dev_sdk.database import Base

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Double, Integer, Numeric, PrimaryKeyConstraint, String, Text, ForeignKey, Index, JSON, func, Table
from sqlalchemy.dialects.postgresql import OID
from typing import Optional
import datetime

from sqlalchemy.orm import Mapped, mapped_column


class HealthCheck(Base):
    __tablename__ = 'health_check'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='health_check_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), server_default=func.now())


class Project(Base):
    """项目表：存储智库研究项目信息"""
    __tablename__ = 'projects'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='projects_pkey'),
        Index('ix_projects_status', 'status'),
        Index('ix_projects_current_stage', 'current_stage'),
        Index('ix_projects_created_at', 'created_at'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, comment="项目名称")
    industry_keyword: Mapped[str] = mapped_column(String(255), nullable=False, comment="行业关键词")
    final_topic: Mapped[Optional[str]] = mapped_column(Text, nullable=True, comment="最终确定的选题")
    client_email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True, comment="客户邮箱地址")
    
    # 项目状态管理
    status: Mapped[str] = mapped_column(
        String(50), 
        nullable=False, 
        server_default='pending',
        comment="项目状态：pending(待启动), stage1_in_progress(阶段1进行中), stage1_completed(阶段1完成), stage2_in_progress(阶段2进行中), stage2_completed(阶段2完成), cancelled(已取消)"
    )
    current_stage: Mapped[Optional[str]] = mapped_column(
        String(20), 
        nullable=True,
        comment="当前阶段：stage1(访谈准备), stage2(产出生成)"
    )
    
    # 时间戳
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True), server_default=func.now(), nullable=False, comment="创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), onupdate=func.now(), nullable=True, comment="更新时间")
    completed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), nullable=True, comment="完成时间")
    
    # 附加信息
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True, comment="项目附加信息（JSON格式）")


class ProjectNodeExecution(Base):
    """节点执行记录表：追踪项目各节点的执行状态"""
    __tablename__ = 'project_node_executions'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='project_node_executions_pkey'),
        Index('ix_project_node_executions_project_id', 'project_id'),
        Index('ix_project_node_executions_node_name', 'node_name'),
        Index('ix_project_node_executions_status', 'status'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey('projects.id'), nullable=False, comment="项目ID")
    node_name: Mapped[str] = mapped_column(String(100), nullable=False, comment="节点名称")
    
    # 节点执行状态
    status: Mapped[str] = mapped_column(
        String(50), 
        nullable=False, 
        server_default='pending',
        comment="节点状态：pending(待执行), in_progress(执行中), completed(已完成), failed(失败), skipped(跳过)"
    )
    
    # 时间戳
    started_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), nullable=True, comment="开始执行时间")
    completed_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), nullable=True, comment="完成时间")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True), server_default=func.now(), nullable=False, comment="记录创建时间")
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True), onupdate=func.now(), nullable=True, comment="记录更新时间")
    
    # 错误信息
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True, comment="错误信息（如果执行失败）")
    
    # 节点输出（JSON格式，存储节点执行结果）
    output_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True, comment="节点输出结果（JSON格式）")


t_pg_stat_statements = Table(
    'pg_stat_statements', Base.metadata,
    Column('userid', OID),
    Column('dbid', OID),
    Column('toplevel', Boolean),
    Column('queryid', BigInteger),
    Column('query', Text),
    Column('plans', BigInteger),
    Column('total_plan_time', Double(53)),
    Column('min_plan_time', Double(53)),
    Column('max_plan_time', Double(53)),
    Column('mean_plan_time', Double(53)),
    Column('stddev_plan_time', Double(53)),
    Column('calls', BigInteger),
    Column('total_exec_time', Double(53)),
    Column('min_exec_time', Double(53)),
    Column('max_exec_time', Double(53)),
    Column('mean_exec_time', Double(53)),
    Column('stddev_exec_time', Double(53)),
    Column('rows', BigInteger),
    Column('shared_blks_hit', BigInteger),
    Column('shared_blks_read', BigInteger),
    Column('shared_blks_dirtied', BigInteger),
    Column('shared_blks_written', BigInteger),
    Column('local_blks_hit', BigInteger),
    Column('local_blks_read', BigInteger),
    Column('local_blks_dirtied', BigInteger),
    Column('local_blks_written', BigInteger),
    Column('temp_blks_read', BigInteger),
    Column('temp_blks_written', BigInteger),
    Column('shared_blk_read_time', Double(53)),
    Column('shared_blk_write_time', Double(53)),
    Column('local_blk_read_time', Double(53)),
    Column('local_blk_write_time', Double(53)),
    Column('temp_blk_read_time', Double(53)),
    Column('temp_blk_write_time', Double(53)),
    Column('wal_records', BigInteger),
    Column('wal_fpi', BigInteger),
    Column('wal_bytes', Numeric),
    Column('jit_functions', BigInteger),
    Column('jit_generation_time', Double(53)),
    Column('jit_inlining_count', BigInteger),
    Column('jit_inlining_time', Double(53)),
    Column('jit_optimization_count', BigInteger),
    Column('jit_optimization_time', Double(53)),
    Column('jit_emission_count', BigInteger),
    Column('jit_emission_time', Double(53)),
    Column('jit_deform_count', BigInteger),
    Column('jit_deform_time', Double(53)),
    Column('stats_since', DateTime(True)),
    Column('minmax_stats_since', DateTime(True))
)


t_pg_stat_statements_info = Table(
    'pg_stat_statements_info', Base.metadata,
    Column('dealloc', BigInteger),
    Column('stats_reset', DateTime(True))
)
