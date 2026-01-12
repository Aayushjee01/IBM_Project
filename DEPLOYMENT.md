# Deployment Guide

## ⚠️ Important: Vercel Compatibility

**Vercel is NOT suitable for Streamlit applications.** Vercel is designed for:
- Frontend frameworks (Next.js, React, Vue, etc.)
- Serverless functions (Node.js, Python functions)
- Static websites

Streamlit applications require:
- A persistent Python runtime environment
- Long-running processes
- WebSocket connections

## ✅ Recommended Deployment Options

### Option 1: Streamlit Cloud (Recommended - Easiest & Free)

**Best for:** Quick deployment, free hosting, perfect for Streamlit apps

**Steps:**

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `career_recommendation_system.py`
   - Click "Deploy"

**Advantages:**
- ✅ Free tier available
- ✅ Automatic deployments on git push
- ✅ Built specifically for Streamlit
- ✅ Easy setup (no configuration needed)
- ✅ Custom subdomain

**Limitations:**
- Free tier: Public repos only
- Resource limits on free tier

---

### Option 2: Railway (Recommended - Easy & Flexible)

**Best for:** Private repos, more control, reasonable pricing

**Steps:**

1. **Install Railway CLI** (optional, can use web interface)
   ```bash
   npm i -g @railway/cli
   railway login
   ```

2. **Create railway.json configuration:**
   ```json
   {
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "streamlit run career_recommendation_system.py --server.port $PORT",
       "restartPolicyType": "ON_FAILURE",
       "restartPolicyMaxRetries": 10
     }
   }
   ```

3. **Create Procfile:**
   ```
   web: streamlit run career_recommendation_system.py --server.port $PORT --server.address 0.0.0.0
   ```

4. **Deploy:**
   - Go to https://railway.app/
   - Click "New Project"
   - Connect GitHub repository
   - Railway auto-detects Python and installs dependencies
   - Set PORT environment variable if needed

**Advantages:**
- ✅ $5/month starter plan (good free credits)
- ✅ Supports private repos
- ✅ Auto-deployment from GitHub
- ✅ Custom domains
- ✅ Environment variables support

---

### Option 3: Render

**Best for:** Simple deployment, good free tier

**Steps:**

1. **Create render.yaml:**
   ```yaml
   services:
     - type: web
       name: career-recommendation-system
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: streamlit run career_recommendation_system.py --server.port $PORT --server.address 0.0.0.0
   ```

2. **Deploy:**
   - Go to https://render.com/
   - Connect GitHub repository
   - Create new Web Service
   - Render auto-detects configuration
   - Deploy

**Advantages:**
- ✅ Free tier available
- ✅ Easy setup
- ✅ Auto-deployment

**Limitations:**
- Free tier spins down after inactivity
- Limited resources on free tier

---

### Option 4: Heroku

**Best for:** Established platform, reliable

**Steps:**

1. **Create Procfile:**
   ```
   web: streamlit run career_recommendation_system.py --server.port $PORT --server.address 0.0.0.0
   ```

2. **Create runtime.txt (optional):**
   ```
   python-3.11.0
   ```

3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

**Advantages:**
- ✅ Established platform
- ✅ Good documentation
- ✅ Add-ons ecosystem

**Limitations:**
- Paid plans only (no free tier)
- More expensive than alternatives

---

### Option 5: Docker + Any Cloud Provider

**Best for:** Maximum flexibility, production deployments

**Steps:**

1. **Create Dockerfile:**
   ```dockerfile
   FROM python:3.11-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 8501

   HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

   ENTRYPOINT ["streamlit", "run", "career_recommendation_system.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and deploy to:**
   - AWS (ECS, EKS, EC2)
   - Google Cloud (Cloud Run, GKE)
   - Azure (Container Instances, AKS)
   - DigitalOcean App Platform
   - Fly.io

---

## 🚀 Quick Start: Streamlit Cloud (Recommended)

Since this is the easiest option, here's a step-by-step guide:

### Step 1: Prepare Your Repository

Make sure your project structure looks like this:
```
your-repo/
├── career_recommendation_system.py
├── requirements.txt
└── README.md
```

### Step 2: Push to GitHub

```bash
# Initialize git (if not already)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/your-repo.git

# Push
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Streamlit Cloud

1. Visit https://share.streamlit.io/
2. Click "Sign in" (use GitHub account)
3. Click "New app"
4. Fill in:
   - **Repository**: Select your GitHub repo
   - **Branch**: `main` (or `master`)
   - **Main file path**: `career_recommendation_system.py`
5. Click "Deploy"
6. Wait 2-3 minutes for deployment
7. Your app will be live at: `https://your-app-name.streamlit.app`

### Step 4: Update App Settings (Optional)

- Go to "Settings" in Streamlit Cloud
- Configure:
  - App title
  - Secrets (environment variables if needed)
  - Advanced settings

---

## 📝 Pre-Deployment Checklist

Before deploying, ensure:

- ✅ All dependencies are in `requirements.txt`
- ✅ Code runs locally without errors
- ✅ No hardcoded secrets or API keys
- ✅ Unused imports removed
- ✅ README.md is updated
- ✅ Git repository is set up
- ✅ Code is committed and pushed

---

## 🔧 Troubleshooting Deployment

### Issue: App crashes on startup
**Solution:** Check requirements.txt versions, ensure all imports are available

### Issue: Port binding errors
**Solution:** Make sure to use `--server.address 0.0.0.0` in start command

### Issue: Dependencies not installing
**Solution:** Verify requirements.txt syntax, check Python version compatibility

### Issue: Memory errors
**Solution:** Optimize code, reduce data loading, use caching

---

## 🌐 Custom Domain Setup

### Streamlit Cloud
- Go to app settings
- Click "Manage app"
- Add custom domain in settings

### Railway/Render
- Add domain in project settings
- Configure DNS records as instructed

---

## 💰 Cost Comparison

| Platform | Free Tier | Paid Tier | Best For |
|----------|-----------|-----------|----------|
| **Streamlit Cloud** | ✅ Yes (public repos) | N/A | Quick demos, public projects |
| **Railway** | ✅ $5 credit/month | $5+/month | Private repos, flexibility |
| **Render** | ✅ Yes (with limits) | $7+/month | Simple deployments |
| **Heroku** | ❌ No | $7+/month | Established workflows |
| **AWS/GCP/Azure** | ❌ No | Pay-as-you-go | Production, enterprise |

---

## 🎯 Recommendation

**For your project, I recommend Streamlit Cloud because:**
1. ✅ Free for public repositories
2. ✅ Zero configuration needed
3. ✅ Built specifically for Streamlit
4. ✅ Automatic deployments
5. ✅ Perfect for demos and presentations

**If you need private repositories or more control, use Railway.**

---

## 📚 Additional Resources

- Streamlit Cloud Docs: https://docs.streamlit.io/streamlit-community-cloud
- Railway Docs: https://docs.railway.app/
- Render Docs: https://render.com/docs
- Streamlit Deployment Guide: https://docs.streamlit.io/deploy

---

## ❓ FAQ

**Q: Can I deploy to Vercel?**  
A: No, Vercel doesn't support Streamlit applications. Use Streamlit Cloud, Railway, or Render instead.

**Q: Is the app ready to deploy?**  
A: Yes! The code is ready. Just push to GitHub and deploy to Streamlit Cloud.

**Q: Do I need to change the code for deployment?**  
A: No changes needed for Streamlit Cloud. Other platforms may require a Procfile or configuration file.

**Q: Can I use a custom domain?**  
A: Yes, most platforms support custom domains (some may require paid plans).

**Q: Is it free?**  
A: Streamlit Cloud is free for public repositories. Railway and Render have free tiers with limitations.