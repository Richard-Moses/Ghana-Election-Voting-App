# 🐍 Base image: secure and minimal
FROM python:3.10-slim

# 📁 Set working directory
WORKDIR /app

# 📦 Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 📂 Copy application code
COPY . .

# 🔐 Make entry script executable (only if it exists)
RUN [ -f worker.py ] && chmod +x worker.py || echo "worker.py not found, skipping chmod"

# 🌐 Expose app port (adjust if needed)
EXPOSE 5000

# 🚀 Run the app using exec form (no shell parsing issues)
CMD ["python3", "worker.py"]