# prompt-api-troubleshooter

> Diagnose and fix common AI API errors (auth, rate limits, timeouts)
> Phase 0 · Lesson 4

---

## Common errors and fixes

| HTTP Code | Error | Cause | Fix |
|-----------|-------|-------|-----|
| **401** | Unauthorized | API key wrong or missing | Check env var set + key valid |
| **403** | Forbidden | Key lacks permission for endpoint/model | Check account access / model availability |
| **429** | Too Many Requests | Rate limited | Wait and retry, reduce request frequency |
| **400** | Bad Request | Request body malformed | Check required fields, model name, message format |
| **500/502/503** | Server Error | Server-side issue | Wait a minute and retry |
| **Timeout** | Timeout | Request took too long | Reduce `max_tokens` or use streaming |
| **Connection refused** | Network | Wrong base URL or network issue | Check the endpoint URL |

---

## Diagnostic steps

1. **Is the API key set?**
   ```bash
   echo $DEEPSEEK_API_KEY | head -c 10
   ```

2. **Is the key valid?** Try a minimal request.

3. **Is the request format correct?** Compare to the docs.

4. **Is there a network issue?**
   ```bash
   curl -I https://api.deepseek.com
   ```
