# GitHub Setup Instructions

## 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click "New repository"
3. Repository name: `interview-questions-project`
4. Description: `AI-powered PDF Interview Question Generator with FastAPI and Streamlit`
5. Set to Public
6. Don't initialize with README (we already have one)
7. Click "Create repository"

## 2. Connect Local Repository to GitHub

```bash
# Add remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/interview-questions-project.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

## 3. Repository Settings

### Enable GitHub Actions
- Go to repository Settings > Actions > General
- Enable "Allow all actions and reusable workflows"

### Add Repository Topics
- Go to repository main page
- Click the gear icon next to "About"
- Add topics: `ai`, `pdf`, `interview-questions`, `fastapi`, `streamlit`, `ollama`, `langchain`

### Add Repository Description
- Description: `AI-powered PDF Interview Question Generator with FastAPI and Streamlit interfaces`

## 4. Optional: Add GitHub Pages

If you want to host documentation:
1. Go to Settings > Pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: / (root)

## 5. Verify Everything Works

1. Check that all files are uploaded
2. Verify .gitignore is working (no sensitive files)
3. Test the installation instructions
4. Check that GitHub Actions run successfully

## 6. Create Release

1. Go to Releases > Create a new release
2. Tag: `v1.0.0`
3. Title: `PDF Interview Question Generator v1.0.0`
4. Description: Use the features from README.md
5. Publish release
