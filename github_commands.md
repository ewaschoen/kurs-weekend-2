# ==============================================================================

# GIT CHEAT SHEET

# ==============================================================================





# ------------------------------------------------------------------------------

# 1. DAILY WORKFLOW (STANDARD COMMIT & PUSH)

# ------------------------------------------------------------------------------



# Check which files have been modified, created, or deleted

git status



# Stage a specific file for the commit

git add t.py



# Stage all changes in the current directory

git add .



# Save staged changes locally with a descriptive message

git commit -m "your commit message here"



# Send local commits to the remote repository (GitHub)

git push





# ------------------------------------------------------------------------------

# 2. SWITCHING TO SSH (FIX POPUP SIGN-IN)

# ------------------------------------------------------------------------------



# Check existing remote URLs (HTTPS or SSH)

git remote -v



# Change remote repository URL from HTTPS to SSH

git remote set-url origin git@github.com:ewaschoen/kurs-weekend-2.git



# Test SSH connection to GitHub

ssh -T git@github.com





# ------------------------------------------------------------------------------

# 3. BRANCH CLEANUP & MIGRATION WORKFLOW

# ------------------------------------------------------------------------------



# Switch active workspace to the main branch

git checkout main



# Copy and apply the latest commit from master onto main

git cherry-pick master



# Upload updated main branch to remote server

git push origin main



# Delete master branch from the remote server (GitHub)

git push origin -d master



# Force-delete master branch from your local machine

git branch -D master





# ------------------------------------------------------------------------------

# 4. USEFUL INSPECTION & RECOVERY COMMANDS

# ------------------------------------------------------------------------------



# View simplified single-line commit history

git log --oneline



# Undo last commit while keeping modified changes in your workspace

git reset --soft HEAD~1



# Discard all local uncommitted changes in the current directory

git restore .