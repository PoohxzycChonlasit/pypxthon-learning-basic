# 04 — AI Delegation, Code Review and Verification

AI coding tool ช่วยทำงานย่อยได้ แต่ไม่ควรเป็นผู้กำหนด requirements หรือ
ตัดสินว่าระบบปลอดภัย เริ่มจากการคิดและเขียน pseudocode เอง แล้วมอบหมายงาน
ที่มีขอบเขตและเกณฑ์รับงานชัดเจน

## Type along: bounded task brief

```python
task = {
    "goal": "validate one offline paper event",
    "must_not": ["network access", "live orders"],
    "tests": ["valid event", "invalid quantity", "unchanged state on rejection"],
}
print(task["goal"], len(task["tests"]))
```

## Delegation template

```text
Goal: [one observable behavior]
Files you may change: [explicit paths]
Input/output contract: [types, fields, errors]
Constraints: [offline-only, no packages, preserve existing files]
Acceptance cases: [independent expected outcomes]
Return: implementation summary, changed files, tests run, known limitations
```

ก่อนรับงาน ตรวจ diff และถามว่าโค้ดทำตาม contract หรือไม่ ตรวจ input ผิดรูป
แบบและกรณีขอบ รัน tests ที่เกี่ยวข้อง และตรวจว่าไม่มีไฟล์นอกขอบเขตถูกแก้
อย่าถือว่าคำตอบจาก AI หรือการที่ tests ผ่านพิสูจน์ edge หรือความปลอดภัยได้

ใช้ workflow นี้กับ [Offline Quant Research Engine](../exercises/offline-quant-research-engine.md)
และ [Offline Paper Trading Bot](../exercises/offline-paper-trading-bot.md)
