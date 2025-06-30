import hashlib, datetime, os

print("🔐 Starting key generation...")

secret = os.getenv("MIKA_SECRET")
if not secret:
    print("❌ MIKA_SECRET not set!")
    exit(1)

days = int(datetime.datetime.utcnow().timestamp() // 86400)
base = secret + str(days)
hash_val = hashlib.sha256(base.encode()).hexdigest()
num = int(hash_val[:8], 16)
key = f"Mika-{num % 10000:04d}"

print(f"✅ Generated key: {key}")

with open("todaykey.txt", "w") as f:
    f.write(key)

print("💾 Saved to todaykey.txt")
