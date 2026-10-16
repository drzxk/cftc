import json, os

secret = [l.split('=',1)[1].strip() for l in open('/root/.secrets/cloudflare/cftc-webhook-secret') if l.startswith('webhook_secret=')][0]
bot_token = open('/home/admin/tg').read().strip()
password = [l.split('=',1)[1].strip() for l in open('/root/.secrets/cloudflare/imgbed-secrets.env') if l.startswith('PASSWORD=')][0]

meta = {
    "main_module": "worker.js",
    "bindings": [
        {"type": "d1", "name": "DATABASE", "id": "aab9b3f2-90c1-4a4a-8647-16bc8131430f"},
        {"type": "plain_text", "name": "DOMAIN", "text": "img.ikyle.eu.org"},
        {"type": "secret_text", "name": "TG_BOT_TOKEN", "text": bot_token},
        {"type": "plain_text", "name": "TG_STORAGE_CHAT_ID", "text": "-5268332278"},
        {"type": "plain_text", "name": "TG_CHAT_ID", "text": "6451351153"},
        {"type": "secret_text", "name": "TG_WEBHOOK_SECRET", "text": secret},
        {"type": "plain_text", "name": "ENABLE_AUTH", "text": "true"},
        {"type": "secret_text", "name": "USERNAME", "text": "kyle"},
        {"type": "secret_text", "name": "PASSWORD", "text": password},
        {"type": "plain_text", "name": "MAX_SIZE_MB", "text": "20"},
    ],
    "compatibility_date": "2024-09-01",
}
open('/tmp/metadata.json', 'w').write(json.dumps(meta, indent=2))
os.chmod('/tmp/metadata.json', 0o600)  # 内含 TG bot token / webhook secret / 面板密码，勿留 644
print("metadata rebuilt, bindings:", [b["name"] for b in meta["bindings"]])
