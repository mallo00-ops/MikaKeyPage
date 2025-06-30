import hashlib, datetime, os

# Get secret from environment
secret = os.getenv("MIKA_SECRET")
if not secret:
    raise Exception("MIKA_SECRET is not set!")

# Generate day-based hash
days = int(datetime.datetime.utcnow().timestamp() // 86400)
base = secret + str(days)
hash_val = hashlib.sha256(base.encode()).hexdigest()
num = int(hash_val[:8], 16)
key = f"Mika-{num % 10000:04d}"

# Write key to file
with open("todaykey.txt", "w") as f:
    f.write(key)
    
