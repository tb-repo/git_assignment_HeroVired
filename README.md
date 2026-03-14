# Git Assignment – HeroVired Batch 16A

Repository: **git_assignment_HeroVired**

This repository demonstrates multiple Git workflows while building simple Python utilities.
The assignment includes the following tasks:

* **Q1 – Calculator Plus Application (branching, PR, tagging)**
* **Q2 – Git Large File Storage (LFS)**
* **Q3 – Geometry Calculator using Git Stash**

All steps below include the **actual commands and outputs captured during execution**.

---

# Q1 – Calculator Plus Application

## a. Create Repository

Repository named **git_assignment_HeroVired** was created in the GitHub account **tb-repo** and set as a **private repository**.

---

# b. Clone Repository to Local Machine

```bash id="q8i5nd"
git clone git@github.com:tb-repo/git_assignment_HeroVired.git
```

---

# c. Create and Switch to `dev` Branch

```bash id="6du9df"
git branch dev
git checkout dev
```

---

# d. Add Calculator Application Code

```python id="o1d4pi"
import math
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
```

---

# e. Execute Program

```bash id="l3yd83"
(base) PS> python app.py
```

Output:

```id="9n1cjo"
16 + 4 = 20
16 - 4 = 12
16 * 4 = 64
16 / 4 = 4.0
```

---

# f. Commit Version 1

```bash id="z3jpr6"
git add .
git commit -m "Version 1 of calculator plus app"
```

Output:

```id="f29p5m"
[dev 5e902d7] Version 1 of calculator plus app
3 files changed, 57 insertions(+), 1 deletion(-)
create mode 100644 .vscode/settings.json
create mode 100644 app.py
```

Push branch:

```bash id="9m7xt9"
git push -u origin dev
```

Output:

```id="h5ynx3"
branch 'dev' set up to track 'origin/dev'
```

---

# g. Merge `dev` → `main` and Create Release v1

```bash id="ny9c2i"
git checkout main
git merge dev
git tag v1.0
git push origin v1.0
```

Output:

```id="7rq34j"
[new tag] v1.0 -> v1.0
```

---

# h. Create Feature Branch `feature/sqrt`

```bash id="c9w44y"
git checkout main
git branch feature/sqrt
git checkout feature/sqrt
```

---

# i. Implement Square Root Feature

Added:

```python id="ksq8cc"
def square_root(self, x):
    return math.sqrt(x)
```

Output:

```id="5r94k8"
√16 = 4.0
√4 = 2.0
```

---

# j. Commit and Push Feature Branch

```bash id="2s3uwp"
git add .
git commit -m "Added square root feature"
git push origin feature/sqrt
```

Output:

```id="xqklmo"
Create a pull request for 'feature/sqrt'
https://github.com/tb-repo/git_assignment_HeroVired/pull/new/feature/sqrt
```

---

# k. Fix Critical Bug in `dev`

Updated divide function:

```python id="jhswok"
def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

Commit fix:

```bash id="qsvr9r"
git checkout dev
git add .
git commit -m "Fix division by zero bug"
git push origin dev
```

Output:

```id="02cey1"
[dev b3f3020] Fix division by zero bug
1 file changed, 3 insertions(+), 1 deletion(-)
```

---

# l. Create Pull Request

PR created:

Title:

```id="yzpx1m"
Add square root feature to CalculatorPlus
```

Reviewer:

```id="7lgpgb"
sanjuwatson-del
```

After approval:

* `feature/sqrt → dev`
* `dev → main`

---

# m. Create Release Version 2

```bash id="a2vq1p"
git tag v2.0
git push origin v2.0
```

---

# Q2 – Git Large File Storage (LFS)

## a. Create `lfs` Branch

```bash id="me1xg6"
git branch lfs
git checkout lfs
```

---

# b. Verify Git LFS Installation

```bash id="0fgj6i"
git lfs status
```

Output:

```id="6px8q6"
On branch lfs

Objects to be committed:

Objects not staged for commit:
```

This confirms **Git LFS is installed**.

---

# c. Track Large Files

```bash id="eegqye"
git lfs track "*.zip"
```

Output:

```id="vfdibq"
Tracking "*.zip"
```

---

# d. Commit `.gitattributes`

```bash id="p3yd8m"
git add .gitattributes
git commit -m "Configure Git LFS tracking"
```

Output:

```id="3np7v4"
[lfs c2f0ba4] Configure Git LFS tracking
1 file changed, 1 insertion(+)
create mode 100644 .gitattributes
```

---

# e. Add Large Binary File

File added:

```id="ff2vyo"
Bitwarden-Portable-2026.1.0.zip
```

Commit:

```bash id="ibk7f3"
git add Bitwarden-Portable-2026.1.0.zip
git commit -m "Add large binary file using Git LFS"
```

Output:

```id="7v76wh"
[lfs a758743] Add large binary file using Git LFS
1 file changed, 3 insertions(+)
create mode 100644 Bitwarden-Portable-2026.1.0.zip
```

---

# f. Push Branch

```bash id="ck9bnl"
git push origin lfs
```

Output:

```id="awzq9k"
Uploading LFS objects: 100% (1/1), 303 MB | 10 MB/s
```

---

# g. Verify LFS Tracking

```bash id="2b3c6o"
git lfs ls-files
```

Output:

```id="o0g3rq"
948387e847 * Bitwarden-Portable-2026.1.0.zip
```
<img src="images/Q2_LFS_SS1.png">
<img src="images/Q2_LFS_SS2.png">
---

# Q3 – Geometry Calculator using Git Stash

## a. Create Branch

```bash id="0p9o2r"
git branch geometry-calculator
git checkout geometry-calculator
```

Output:

```id="zqfo3o"
Switched to branch 'geometry-calculator'
```

---

# b. Add Base Geometry Code

```python id="dffyql"
import math
class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2
    def calculate_rectangle_area(self, length, width):
        return length * width
```

Commit:

```bash id="hpx2pr"
git add .
git commit -m "Geometry Calculator base code"
```

Output:

```id="p5h1ds"
[geometry-calculator ab53e40] Geometry Calculator base code
1 file changed, 6 insertions(+), 28 deletions(-)
```

---

# Circle Area Feature

```bash id="l9bn7p"
git branch feature/circle-area
git checkout feature/circle-area
```

Run program:

```id="c7qcz3"
The area of the circle with radius 5 = 78.53981633974483
```

Stash changes:

```bash id="3ol1qk"
git stash
git stash list
```

---

# Rectangle Area Feature

```bash id="5x62ox"
git branch feature/rectangle-area
git checkout feature/rectangle-area
```

Stash incomplete work:

```bash id="c8q3ir"
git stash
```

---

# Resume Circle Feature

```bash id="s3g3ra"
git checkout feature/circle-area
git stash pop
```

Commit:

```bash id="mxt2p7"
git commit -m "Add circle area feature"
git push origin feature/circle-area
```

---

# Resume Rectangle Feature

```bash id="s29h4y"
git checkout feature/rectangle-area
git stash pop
```

Commit:

```bash id="aj0g20"
git commit -m "Add rectangle area feature"
git push origin feature/rectangle-area
```

---

# Pull Requests

Two PRs created:

| Source                 | Target |
| ---------------------- | ------ |
| feature/circle-area    | dev    |
| feature/rectangle-area | dev    |

After approval:

* merged to **dev**
* then **dev merged to main**

---

# Final Branch Structure

```id="pfrfif"
main
 │
 └── dev
      │
      ├── feature/sqrt
      ├── feature/circle-area
      ├── feature/rectangle-area
      └── lfs
```

---

# Git Concepts Demonstrated

* Git branching strategy
* Feature branches
* Pull Requests and code reviews
* Git tags and releases
* Git LFS for large files
* Git stash workflow
