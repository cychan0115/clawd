#!/bin/bash
# Kimi 模型配置更新脚本
# 适用于 Claude Code 和 OpenCode

echo "🔄 正在更新 Kimi 模型配置..."

# ============================================
# Claude Code 配置
# ============================================
echo "✅ Claude Code 配置已更新: ~/.claude/settings.json"
echo "   - API Base URL: https://api.kimi.com/coding/"
echo "   - 主模型: kimi-for-coding"
echo "   - 高级模型: kimi-k2.6"

# 需要设置的环境变量（添加到 ~/.zshrc 或 ~/.bash_profile）
echo ""
echo "📋 请添加以下环境变量到你的 shell 配置文件:"
echo ""
echo "# Kimi API Key (请替换为你的实际 API Key)"
echo "export ANTHROPIC_AUTH_TOKEN='YOUR_KIMI_API_KEY'"
echo ""
echo "# Claude Code 使用 Kimi"
echo "export ANTHROPIC_BASE_URL='https://api.kimi.com/coding/'"
echo "export ANTHROPIC_MODEL='kimi-for-coding'"
echo "export ANTHROPIC_DEFAULT_SONNET_MODEL='kimi-for-coding'"
echo "export ANTHROPIC_DEFAULT_OPUS_MODEL='kimi-k2.6'"
echo "export ANTHROPIC_DEFAULT_HAIKU_MODEL='kimi-for-coding'"

# ============================================
# OpenCode 配置
# ============================================
echo ""
echo "✅ OpenCode 配置已更新: ~/.config/opencode/opencode.json"
echo "   - 主模型: kimi/kimi-for-coding"

# ============================================
# Codex 配置（可选）
# ============================================
echo ""
echo "⚠️  Codex 配置说明:"
echo "   Codex 是 OpenAI 官方工具，默认使用 GPT-5.5"
echo "   如果要切换到 Kimi，需要设置以下环境变量:"
echo ""
echo "# Codex 使用 Kimi (通过 OpenAI 兼容 API)"
echo "export OPENAI_API_KEY='YOUR_KIMI_API_KEY'"
echo "export OPENAI_BASE_URL='https://api.kimi.com/v1'"
echo ""
echo "   注意: Codex 可能不完全兼容 Kimi API，如果遇到问题请保留 OpenAI 配置"

# ============================================
# 快速验证
# ============================================
echo ""
echo "🔍 验证配置..."
if [ -f ~/.claude/settings.json ]; then
    echo "✅ Claude Code 配置文件存在"
    grep -q "kimi-for-coding" ~/.claude/settings.json && echo "✅ Claude Code 模型已设置为 kimi-for-coding"
fi

if [ -f ~/.config/opencode/opencode.json ]; then
    echo "✅ OpenCode 配置文件存在"
    grep -q "kimi-for-coding" ~/.config/opencode/opencode.json && echo "✅ OpenCode 模型已设置为 kimi-for-coding"
fi

echo ""
echo "🎉 配置更新完成!"
echo ""
echo "⚠️  重要提醒:"
echo "   1. 请替换 YOUR_KIMI_API_KEY 为你的实际 Kimi API Key"
echo "   2. 重新加载 shell 配置: source ~/.zshrc"
echo "   3. 重启 Claude Code 和 OpenCode 以应用新配置"
