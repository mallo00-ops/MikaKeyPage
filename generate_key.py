import hashlib, datetime, os

# Get secret from GitHub Actions secret
secret = os.getenv("MIKA_SECRET")
if not secret:
    raise Exception("MIKA_SECRET not found!")

days_since_epoch = int(datetime.datetime.utcnow().timestamp() // 86400)
base = secret + str(days_since_epoch)
hash_val = hashlib.sha256(base.encode()).hexdigest()
num = int(hash_val[:8], 16)
key = f"Mika-{num % 10000:04d}"

with open("todaykey.txt", "w") as f:
    f.write(key)
  
