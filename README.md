# Congty4v2

Project small demo used for Git practice exercises.

Files added for the exercise:

- `src/simple_app.py`  - a tiny calculator module (add, sub, mul, div)
- `tests/test_app.py`  - unit tests using Python's built-in `unittest`
- `.gitignore`         - ignores common Python/IDE artifacts

How to run the tests (PowerShell on Windows):

```powershell
python -m unittest discover -v
```

Git practice exercise suggestions
--------------------------------

Use the following steps / commands in PowerShell to practice git workflows. These are just suggested tasks you can perform as a student assignment.

1. Initialize and make the first commit (if repo not yet initialized):

```powershell
# initialize (only if needed)
# git init
# git remote add origin <your-remote-url>
git status
git add .
git commit -m "Initial files: simple_app, tests, .gitignore"
```

2. Create a branch for a feature or exercise (e.g., implement a new function):

```powershell
git checkout -b feature/add-power
# edit files (e.g., add a new function to src/simple_app.py)
git add -A
git commit -m "Add power(x, y) function"
```

3. Run tests locally, fix bugs, and commit small changes:

```powershell
python -m unittest discover -v
```

4. Push branch and open a Pull Request (if using GitHub/GitLab):

```powershell
git push -u origin feature/add-power
# then create PR on the hosting site
```

5. Practice merge conflicts:

- Create two branches that modify the same line in a file, commit both, then merge and resolve the conflict manually. Commit the resolution.

6. Practice other commands:

- Revert a commit: `git revert <commit>`
- Reset to a previous commit (dangerous): `git reset --hard <commit>`
- Cherry-pick: `git cherry-pick <commit>`
- Tag a release: `git tag -a v1.0 -m "v1.0"` and `git push origin v1.0`

Tips for grading / exercises:

- Ask students to create a branch, implement or fix a change, run tests, push the branch, and open a pull request.
- Ask them to show at least 3 commits with meaningful messages.
- Include a short write-up of conflict resolution when they intentionally create and fix a merge conflict.

If you want, tôi có thể:

- Thêm một bài tập mẫu (issue) với mô tả chi tiết.
- Viết kịch bản kiểm tra (script) để tự động chấm điểm dựa trên các commit/messages.
- Tạo một file `CONTRIBUTING.md` mô tả workflow cần làm cho bài tập.
