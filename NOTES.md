## Question 1 - What is worth its own commit?

### Category A: High-value commit boundaries

For this project, I think a change is worth its own commit when it adds something meaningful to the Team Directory or changes how the program works. For example, adding the main program, adding the team data, connecting the data to the program, and later adding a search feature are changes I would commit separately. I would do this because each commit would then have a clear purpose. If something goes wrong, it would also be easier to find the change that caused the problem or go back to an earlier version without affecting unrelated work.

### Category B: Changes NOT worth a separate commit

I would not create a separate commit for every small correction I make while working. A small spelling mistake, a whitespace correction, or removing a temporary print statement I used while testing can normally be included with the change I am already working on. Separating every small correction would give me more commits, but it would not necessarily make the history better. Instead, it could make the Git log harder to read because small corrections would be mixed with the changes that actually affected the project.

### Category C: .gitignore scope

For this project, I will use `.gitignore` to exclude the `.env` file, log files, and Python's `__pycache__/` directory. I do not want the `.env` file in the repository because files like this can contain information that should remain private, such as passwords or API keys. Log files and `__pycache__` are generated while the program is being used and do not need to be part of the source code. It is important that I set up `.gitignore` before these files are created or committed. If something sensitive was committed first and removed later, it could still remain in the previous Git history. Cleaning that history afterwards could also cause problems for teammates who already have a copy of the repository.

## Question 2 - Choosing merge vs. rebase

A merge keeps the history of both branches and shows that the work was developed separately before being brought together. This is useful when I want the Git history to show how the work actually happened. The disadvantage is that it can make the history less linear because a merge commit may be added when the branches have both changed.

A rebase works differently because it moves my branch commits so that they appear after the latest commit on the branch I am rebasing onto. This gives me a cleaner and more linear history, but it no longer preserves the exact way the branches originally separated because the commits on my branch are rewritten.

For the intentional conflict in this project, I will use a merge. I chose this because I want the history to clearly show that the two branches had different changes and were later brought together when I resolved the conflict.

## Question 3 - Remote operations inventory

In this project, the main Git commands that will communicate with GitHub are `git push`, `git push -u origin <branch-name>`, `git pull --rebase origin main`, and the command used to delete a remote branch, `git push origin --delete <branch-name>`. I will also use `git push -u origin main` for the first push of the main branch. The `-u` option sets the upstream branch so that future pushes and pulls can use the connection between my local branch and the branch on GitHub.

When I use `git push`, my local commits are sent to the remote repository. If the push is successful, GitHub should show the new commits and updated files. When I push a new feature branch using `git push -u origin <branch-name>`, the branch and its commits are sent to GitHub and the local branch is connected to the remote branch for future pushes. When I use `git pull --rebase origin main`, Git retrieves changes from the remote main branch and then reapplies my local commits on top of those changes. This will be useful later in the assignment when I intentionally create a situation where GitHub has a commit that my local repository does not have.

At the end of the branch workflow, I will use `git push origin --delete <branch-name>` to remove a branch from GitHub after it has been merged and is no longer needed. This changes GitHub by removing the remote branch, while the commits that were already merged into main remain in the repository history.

A successful push cannot prove that everything in my local project is correct. For example, GitHub accepting my push does not automatically prove that the program works correctly or that I followed a good commit structure. It also cannot prove that an ignored file such as `.env` exists locally because `.gitignore` prevents Git from tracking and pushing it. This means I still need to use local commands such as `git status`, `git diff`, and `git log` to check my work instead of assuming that a successful push means everything is correct.

## Question 4 - Commit message as specification

a. `fixed stuff`
This message is too vague and does not explain what was fixed or why the
change was made. A better message would be:
`Fix team member search to return matching results`


b. `Update index.js`
This message only tells me which file was changed and does not explain the
purpose of the change. A better message would be:
`Add team member search functionality`


c. `WIP`
This message is non-descriptive because it only says that the work is still
in progress. It does not tell a teammate what actually changed. A better
message would be:
`Add initial team directory display`


d. `Add email format validation so invalid addresses cannot be submitted`
This is already a good behaviour-focused commit message. It uses imperative
mood and clearly explains both the change and its purpose, so I would keep
this message as it is.


e. `asdasd`
This message does not describe the change at all. Someone reading the Git
history would not know what was added or changed. A better message would be:
`Add sample team member data`


f. `Changed line 47 of notes.md`
This focuses on where the change was made instead of explaining why it was
made. A better message would be:
`Clarify merge and rebase decision in project notes`

## Part 3 - Diff observations

### Diff observation 1

Before staging the change to `main.py`, I ran `git diff`. It showed that I had added the JSON import and the code that opens and reads `team.json`. This helped me see exactly what had changed before I staged the file.

### Diff observation 2

Before staging the next change to `main.py`, I ran `git diff` again. It showed the new loop that goes through the team member data and displays each member's name and role. This helped me confirm that only the display behaviour had changed before I staged it.

## Feature branch merge

I developed the team member search feature on the `feature/search-member` branch using two separate commits. When I merged the branch into `main`, Git performed a fast-forward merge. I knew it was a fast-forward because Git displayed `Fast-forward` in the merge output, and `main` had not received any separate commits since the feature branch was created.

## Merge conflict resolution

I created a real merge conflict by changing the same project status line in `README.md` differently on `main` and `conflict/readme-status`. Git could not decide which version to keep, so it marked the file as conflicted. I resolved it by removing the conflict markers and replacing the two competing versions with one final status line that represented the merged result. After checking the file, I staged `README.md` to mark the conflict as resolved.

