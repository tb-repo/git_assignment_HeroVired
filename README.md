Git Large File Storage (LFS) Setup and Verification
a. Created a New Branch Named lfs
First, a new branch named lfs was created and checked out.
git branch lfs
git checkout lfs
________________________________________
b. Verified if Git LFS is Installed
The following command was executed to check whether Git LFS is already installed and configured.
git lfs status
Output:
(base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git lfs status
On branch lfs

Objects to be committed:

Objects not staged for commit:
Since the command executed successfully, it confirms that Git LFS is already installed.
________________________________________
c. Configured Git LFS to Track Large Binary Files
Git LFS was configured to track .zip files.
git lfs track "*.zip"
Output:
Tracking "*.zip"
________________________________________
d. Added the .gitattributes File
After configuring LFS tracking, the .gitattributes file was added and committed.
git add .gitattributes
git commit -m "Configure Git LFS tracking"
Output:
[lfs c2f0ba4] Configure Git LFS tracking
1 file changed, 1 insertion(+)
create mode 100644 .gitattributes
________________________________________
e. Added a Large File to the Repository
A large file Bitwarden-Portable-2026.1.0.zip (greater than 200 MB) was added to the repository.
git add Bitwarden-Portable-2026.1.0.zip
git commit -m "Add large binary file using Git LFS"
Output:
[lfs a758743] Add large binary file using Git LFS
1 file changed, 3 insertions(+)
create mode 100644 Bitwarden-Portable-2026.1.0.zip
________________________________________
f. Pushed the Branch to GitHub
The lfs branch was pushed to the GitHub repository.
git push origin lfs
Output:
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

To github.com:tb-repo/git_assignment_HeroVired.git
* [new branch] lfs -> lfs
________________________________________
g. Verified Git LFS Tracking
Finally, Git LFS tracking was verified using the following command:
git lfs ls-files
Output:
948387e847 * Bitwarden-Portable-2026.1.0.zip
This confirms that the large file is successfully tracked using Git LFS.
 
<img width="940" height="488" alt="image" src="https://github.com/user-attachments/assets/97e8c8ae-e004-4613-95a2-9e128fa9ced0" />

<img width="940" height="315" alt="image" src="https://github.com/user-attachments/assets/11dbb2da-1378-448d-903d-50a140df94c2" />

