# Git Large File Storage (LFS) Setup and Verification

This section demonstrates how **Git LFS (Large File Storage)** was configured in the repository to handle large binary files efficiently.

---

# a. Create a New Branch `lfs`

A new branch named **`lfs`** was created and checked out.

```bash id="p9e8q7"
git branch lfs
git checkout lfs
```

---

# b. Verify if Git LFS is Installed

The following command was executed to verify whether **Git LFS is installed and configured** in the system.

```bash id="9n5jcf"
git lfs status
```

### Output

```id="ldv5u5"
(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git lfs status
On branch lfs

Objects to be committed:

Objects not staged for commit:
```

Since the command executed successfully, it confirms that **Git LFS is already installed and available in the environment**.

---

# c. Configure Git LFS to Track Large Files

Git LFS was configured to track **`.zip` files**, which are typically large binary files.

```bash id="y4p0p3"
git lfs track "*.zip"
```

### Output

```id="hjsr3f"
Tracking "*.zip"
```

This command creates or updates the **`.gitattributes`** file to define LFS tracking rules.

---

# d. Add and Commit the `.gitattributes` File

After configuring LFS tracking, the `.gitattributes` file was added and committed.

```bash id="fa0n1s"
git add .gitattributes
git commit -m "Configure Git LFS tracking"
```

### Output

```id="6wjrjg"
[lfs c2f0ba4] Configure Git LFS tracking
1 file changed, 1 insertion(+)
create mode 100644 .gitattributes
```

---

# e. Add a Large File to the Repository

A large file named **`Bitwarden-Portable-2026.1.0.zip`** (greater than **200 MB**) was added to the repository.

```bash id="1bb0dr"
git add Bitwarden-Portable-2026.1.0.zip
git commit -m "Add large binary file using Git LFS"
```

### Output

```id="r8ixqt"
[lfs a758743] Add large binary file using Git LFS
1 file changed, 3 insertions(+)
create mode 100644 Bitwarden-Portable-2026.1.0.zip
```

Because `.zip` files were configured in Git LFS tracking, Git stored the file using **LFS pointers instead of committing the entire binary into Git history**.

---

# f. Push the Branch to GitHub

The **`lfs`** branch was pushed to the remote repository.

```bash id="3rjqhi"
git push origin lfs
```

### Output

```id="fl2r4q"
Uploading LFS objects: 100% (1/1), 303 MB | 10 MB/s, done.
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 826 bytes | 206.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)

remote: Resolving deltas: 100% (1/1), done.
remote:
remote: Create a pull request for 'lfs' on GitHub by visiting:
remote: https://github.com/tb-repo/git_assignment_HeroVired/pull/new/lfs
```

This confirms that the **large file was uploaded using Git LFS instead of standard Git objects**.

---

# g. Verify Git LFS Tracking

Finally, Git LFS tracking was verified using the following command:

```bash id="v11a5b"
git lfs ls-files
```

### Output

```id="x8d23d"
948387e847 * Bitwarden-Portable-2026.1.0.zip
```

This confirms that the large file **`Bitwarden-Portable-2026.1.0.zip`** is successfully tracked using **Git LFS**.

---

# Summary

The following steps were successfully completed:

1. Created a new **`lfs` branch**
2. Verified **Git LFS installation**
3. Configured LFS to track **`.zip` files**
4. Added and committed **`.gitattributes`**
5. Added a **large binary file (>200MB)**
6. Pushed the file to GitHub using **Git LFS**
7. Verified the file using **`git lfs ls-files`**

This confirms that the repository is correctly configured to handle **large binary files efficiently using Git LFS**.

 
<img width="940" height="488" alt="image" src="https://github.com/user-attachments/assets/97e8c8ae-e004-4613-95a2-9e128fa9ced0" />

<img width="940" height="315" alt="image" src="https://github.com/user-attachments/assets/11dbb2da-1378-448d-903d-50a140df94c2" />

