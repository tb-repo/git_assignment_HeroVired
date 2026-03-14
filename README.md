# Calculator Plus App & Geometry Calculator

**Git Assignment – HeroVired Batch 16A**

This repository demonstrates Git workflows including:

* Branching (`dev`, `feature/*`)
* Pull Requests and code review
* Git tags for releases
* Git LFS for large files
* Git stash for managing incomplete work

All steps below include the **actual commands and outputs captured during execution**.

---

# Q1 – Calculator Plus Application

## a. Create Repository

Repository named **git_assignment_HeroVired** created in GitHub account **tb-repo**.

---

## b. Clone Repository

```bash
git clone git@github.com:tb-repo/git_assignment_HeroVired.git
```

---

## c. Create and Switch to `dev` Branch

```bash
git branch dev
git checkout dev
```

---

## d. Create `app.py` and Add Calculator Code

```python
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

if __name__ == "__main__":
    calculator = Calculator()
    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
```

---

## e. Run the Code

```bash
(base) PS> python app.py
```

Output:

```
16 + 4 = 20
16 - 4 = 12
16 * 4 = 64
16 / 4 = 4.0
```

---

## f. Commit Version 1

```bash
git add .
git commit -m "Version 1 of calculator plus app"
```

Output:

```
[dev 5e902d7] Version 1 of calculator plus app
3 files changed, 57 insertions(+), 1 deletion(-)
create mode 100644 .vscode/settings.json
create mode 100644 app.py
```

Push to repository:

```bash
git push -u origin dev
```

Output:

```
branch 'dev' set up to track 'origin/dev'
```

---

## g. Merge `dev` into `main` and Create Release v1

```bash
git checkout main
git merge dev
git tag v1.0
git push origin v1.0
```

Output:

```
[new tag] v1.0 -> v1.0
```

---

# Feature Implementation – Square Root

## h. Create Feature Branch

```bash
git checkout main
git branch feature/sqrt
git checkout feature/sqrt
```

---

## i. Add Square Root Feature

```python
def square_root(self, x):
    return math.sqrt(x)
```

Program output:

```
16 + 4 = 20
16 - 4 = 12
16 * 4 = 64
16 / 4 = 4.0
√16 = 4.0
√4 = 2.0
```

---

## j. Commit and Push Feature

```bash
git add .
git commit -m "Added square root feature"
git push origin feature/sqrt
```

Output:

```
Create a pull request for 'feature/sqrt'
https://github.com/tb-repo/git_assignment_HeroVired/pull/new/feature/sqrt
```

---

## k. Fix Critical Bug in `dev` Branch

Switch to dev:

```bash
git checkout dev
```

Updated `divide()` function:

```python
def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

Commit fix:

```bash
git add .
git commit -m "Fix division by zero bug"
git push origin dev
```

Output:

```
[dev b3f3020] Fix division by zero bug
1 file changed, 3 insertions(+), 1 deletion(-)
```

---

## l. Create Pull Request

Pull Request created for **feature/sqrt** with:

**Title**

```
Add square root feature to CalculatorPlus
```

**Description**

```
Please review the feature branch code with the sqrt function added.
```

Reviewer assigned:

```
sanjuwatson-del
```

---

# Q3 – Geometry Calculator using Git Stash

## a. Create `geometry-calculator` Branch

```bash
git branch geometry-calculator
git checkout geometry-calculator
```

Output:

```
Switched to branch 'geometry-calculator'
```

---

## b. Add Base Geometry Calculator Code

```python
import math
class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2
    def calculate_rectangle_area(self, length, width):
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()
```

Commit:

```bash
git add .
git commit -m "Geometry Calculator base code"
```

Output:

```
[geometry-calculator ab53e40] Geometry Calculator base code
1 file changed, 6 insertions(+), 28 deletions(-)
```

---

# Circle Area Feature

## c. Create Feature Branch

```bash
git branch feature/circle-area
git checkout feature/circle-area
```

Add code:

```python
radius = 5
print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")
```

Run program:

```
The area of the circle with radius 5 = 78.53981633974483
```

---

## d. Stash Changes

```bash
git stash
git stash list
```

Output:

```
stash@{0}: WIP on feature/circle-area
```

Working directory check:

```bash
git status
```

```
nothing to commit, working tree clean
```

---

# Rectangle Area Feature

## e. Create Branch

```bash
git branch feature/rectangle-area
git checkout feature/rectangle-area
```

Add code:

```python
length = 10
width = 6
print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length,width)}")
```

---

## f. Stash Rectangle Feature

```bash
git stash
```

Output:

```
Saved working directory and index state WIP on feature/rectangle-area
```

---

# Resume Circle Feature

```bash
git checkout feature/circle-area
git stash pop
```

Commit and push:

```bash
git add .
git commit -m "Add circle area feature"
git push origin feature/circle-area
```

Output:

```
Create a pull request for 'feature/circle-area'
```

---

# Resume Rectangle Feature

```bash
git checkout feature/rectangle-area
git stash pop
```

Commit and push:

```bash
git add .
git commit -m "Add rectangle area feature"
git push origin feature/rectangle-area
```

Output:

```
Create a pull request for 'feature/rectangle-area'
```

---

# Pull Requests

Two Pull Requests created:

| Source Branch          | Target Branch |
| ---------------------- | ------------- |
| feature/circle-area    | dev           |
| feature/rectangle-area | dev           |

After review approval, both branches were merged.
The code when merged from feature branches to dev branch required minor changes to include both calculator together.

<img src="images/Q3_PR_SS1.png">
<img src="images/Q3_PR_SS2.png">
<img src="images/Q3_PR_SS3.png">
<img src="images/Q3_PR_SS4.png">
<img src="images/Q3_PR_SS5.png">
<img src="images/Q3_PR_SS6.png">
<img src="images/Q3_PR_SS7.png">
---

# Final Branch Structure

```
main
 │
 └── dev
      │
      ├── feature/sqrt
      ├── feature/circle-area
      └── feature/rectangle-area
```

---

# Git Concepts Demonstrated

* Git branching strategy
* Feature branches
* Pull Requests and review workflow
* Git stash for incomplete work
* Git tags for release versions
* Git LFS for large files
