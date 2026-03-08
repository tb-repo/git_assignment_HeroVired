a. Created a new branch named lfs

git branch lfs

git checkout lfs

b. Check if GIT LFS is already installed for managing large files:

(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git lfs status
On branch lfs

Objects to be committed:


Objects not staged for commit:

Since the above command executed successfully, it confirms LFS is already installed.

c. Configured Git LFS to track large binary files

(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git lfs track "*.zip"
Tracking "*.zip"

d. Added the .gitattributes file

(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git add .gitattributes

(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git commit -m "Configure Git LFS tracking"
[lfs c2f0ba4] Configure Git LFS tracking
 1 file changed, 1 insertion(+)
 create mode 100644 .gitattributes

e. Added a large file Bitwarden-Portable-2026.1.0.zip (>200MB) to the repository

(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git add Bitwarden-Portable-2026.1.0.zip

(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git commit -m "Add large binary file using Git LFS"
[lfs a758743] Add large binary file using Git LFS
 1 file changed, 3 insertions(+)
 create mode 100644 Bitwarden-Portable-2026.1.0.zip

f. Pushed the branch to GitHub

(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git push origin lfs
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
remote:      https://github.com/tb-repo/git_assignment_HeroVired/pull/new/lfs
remote:
To github.com:tb-repo/git_assignment_HeroVired.git
 * [new branch]      lfs -> lfs

g. Verified LFS tracking

(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git lfs ls-files
948387e847 * Bitwarden-Portable-2026.1.0.zip