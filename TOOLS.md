# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## System Hourly Inspection (cron 独立任务)

- **路径**: `/Users/3pigcn/clawd/skills/system-hourly-inspection/system_hourly_inspection.py`
- **调度**: 每小时执行（cron ID: `078443c8-c048-4e69-8dab-eb99c185567b`）
- **职责**: K8S日志检查 + 主机资源检查 + HTTP端点检查
- **异常通知**: 自动发邮件至 `13926262295@139.com`
- **注意**: 此任务为独立 cron 脚本，**无需 agent 介入处理**。Heartbeat 中无需重复做系统资源/HTTP巡检。

## Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

## SSH

- home-server → 192.168.1.100, user: admin

## TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Related

- [Agent workspace](/concepts/agent-workspace)
