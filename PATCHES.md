# 本 fork 的改动（相对上游 iawooo/cftc）

上游 2025-04-17 后停更。本 fork 只保留一处安全加固，其余与上游完全一致。

## 唯一改动：Webhook secret 校验

- `handleTelegramWebhook` 校验 `X-Telegram-Bot-Api-Secret-Token` header，与 `TG_WEBHOOK_SECRET` 环境变量比对，不符返回 403
- `setWebhook` 时携带 `secret_token`，由 worker 启动时自动调用
- 目的：`/webhook` 是公开端点，无校验时任何人知道 URL 即可伪造 Telegram 更新（冒充白名单内的 uid），往存储群写文件 / 触发 bot 消息

配置变量：`TG_WEBHOOK_SECRET`（未设置则退化为上游行为，不校验）。其余变量与上游 README 一致。

## 已回滚的改动（2026-10-14）

以下补丁曾加入后判定无效并回滚，原因记录在此以免重复尝试：

- **sendDocument 上传 / 原图上传开关**：无效。图片压缩发生在用户 TG 客户端发送时（以「照片」方式发送即在客户端压成 ~1280px），bot 收到时已是压缩字节；bot 侧无论用 sendPhoto 还是 sendDocument 转存，存下的都是同一份压缩数据。唯一无损路径是用户在客户端选「以文件方式发送」。
- **默认存储 telegram**：上游默认 r2，未绑 R2 时行为异常；本库已手动将 `user_settings.storage_type` 设为 telegram，代码层回滚无实际影响。
