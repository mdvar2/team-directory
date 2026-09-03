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

The Git commands I used that communicated with GitHub included `git push`, `git push -u origin main`, `git push -u origin feature/search-member`, `git push -u origin ci/pr-check`, `git pull --rebase origin main`, `git push origin --delete ci/pr-check`, and `git fetch --prune`. I used `git push` to send local commits to GitHub. The `git push -u origin ...` commands were used when publishing a branch for the first time, with `-u` setting its upstream connection so later pushes and pulls could use that relationship. I used `git pull --rebase origin main` during the rejected-push exercise. It retrieved the newer commit from GitHub and replayed my local commit on top of it instead of overwriting the remote work.

I used `git push origin --delete ci/pr-check` to remove the pull-request branch from GitHub after it was no longer needed, and `git fetch --prune` to remove stale remote-tracking references locally. A successful push does not prove that the program is correct, that the commits are well structured, or that ignored files have been handled properly. I still need commands such as `git status`, `git diff`, and `git log` to inspect the repository and verify the work.

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

## Merge vs rebase history

The intentional README conflict produced a merge-shaped history because both branches had separate commits before they were combined with a merge commit. This preserves the point where the branches diverged and came back together.

For the member-count feature, I rebased the branch onto the latest `main` before merging it. Rebase moved the feature commit on top of the newer main commit and gave it a new commit hash. This created a straight-line history and allowed the final merge into `main` to be fast-forwarded.

I would use a merge when preserving the history of separate branches is useful, especially when work from different branches needs to remain visible. I would use rebase for my own feature work when I want to update it with the latest `main` and keep the final history linear.

## Rejected push and recovery

I created a commit directly on GitHub and then made a different local commit without pulling the remote change first. When I tried to push, Git rejected the push with a `fetch first` message because the remote branch contained work that my local branch did not have. I recovered by running `git pull --rebase origin main`, which replayed my local commit on top of the newer remote commit. I used rebase instead of force-push because force-pushing could overwrite work that already existed on GitHub.

## Final reflection

The commits I found most useful were the ones that each represented one complete behaviour, such as loading the team data, displaying members, and adding search. A change I could easily have bundled was the search input and the search logic, but keeping them separate made the feature work easier to understand. I used a merge for the intentional README conflict because I wanted the history to preserve the two separate lines of development and show where they came together. I used rebase for the member-count branch because it was my own feature work and replaying it onto the latest main kept the final history linear. 

The rejected push showed me that a failed push can be Git protecting shared history rather than something being wrong with the repository. Pulling with rebase allowed me to keep the remote change and replay my local commit on top of it without overwriting the work already on GitHub. One thing that surprised me was how clearly the commit graph shows the difference between workflows. The merge produced a visible diamond, while the rebased feature became a straight line even though both approaches ultimately brought the changes into main.

## Assignment 1.2

## Question 1 - Why fork instead of branch?

In Assignment 1.1 I could create branches directly inside my own repository because I owned the repository and had permission to push changes to it. In this assignment I will be contributing to another person's repository, so I should not assume that I have permission to create and push branches directly to their project.

Forking gives me my own copy of their repository on GitHub where I can safely create branches and push my work. I can then open a pull request from my fork back into the original repository. If I only cloned my partner's repository and tried to push a branch directly to it without write permission, GitHub would reject the push.

## Question 2 - PR description: bad vs. good

### Bad PR description

Added role search.

### Better PR description

**What:** Added the ability to search team members by their role.

**Why:** This makes it easier to find people with a particular responsibility without manually reading through every team member.

**How to verify:** Run the Team Directory, choose the role search option, and enter an existing role. Confirm that matching team members are displayed. Also try a role that does not exist and confirm that the program handles it correctly.

The second description is easier to review because it explains what changed, why the change is useful, and gives the reviewer clear steps they can follow to test the feature.

## Question 3 - Triaging review comments

A blocking comment identifies something that should be corrected before the pull request is merged, such as a bug, incorrect behaviour, or a missing case that could cause the feature to fail. A nit or suggestion is an optional improvement, such as naming, formatting, or another small change that would improve the code but should not necessarily prevent the merge. A question asks for clarification about the code or the reason behind a particular decision.

If a reviewer does not label the comment, I will consider whether leaving the issue unchanged could make the feature incorrect, unreliable, or difficult to use. If it could, I will treat it as blocking. If the code still works correctly and the comment is mainly about preference or a small improvement, I will treat it as a suggestion. If the reviewer is asking me to explain something rather than requesting a change, I will treat it as a question.

## Question 4 - When fetch beats pull

One situation where I would deliberately use `git fetch` instead of immediately running `git pull` is after my partner's contribution has been merged into my GitHub repository. I would fetch the remote changes first and compare my local `main` with `origin/main`.

This would let me see exactly what changed on the remote before those changes are integrated into my local branch. In this assignment I would specifically check that my partner's merged contribution appears on `origin/main` while my local `main` still points to its previous commit. After confirming the difference, I could pull the changes into my local branch.

## Assignment 1.2 Reflection

### What I contributed

I contributed an alphabetical sorting feature to my Thato's Team Directory project. I added an option that allows the user to choose whether team members should be displayed alphabetically. I split the work into two commits so that adding the user option and implementing the sorting behaviour were separate changes.

### Review feedback I received

I opened a pull request from my fork into my partner's repository and requested a review. At the time of completing my submission, I was still waiting for my partner to complete the review, so I did not make up review feedback or changes that had not actually happened.

### A review comment I gave

While reviewing a contribution to my repository, I noticed that the role search did not initially handle empty input or leading and trailing spaces properly. I treated this as blocking because valid input with accidental spaces could fail to match the stored role. During the re-review I also found that an unsuccessful search could display the not-found message twice. The contributor corrected the issues using follow-up commits before I approved and merged the pull request.

I also gave an optional suggestion to normalise the role search value once before the loop. I marked this as optional because the existing approach could still work and therefore did not need to block the merge.

### Fetch vs pull in practice

After the partner contribution was merged on GitHub, I deliberately used `git fetch origin` before pulling. My local `main` remained at its existing commit while `origin/main` moved forward to include the merged contribution. Running `git log --oneline main..origin/main` allowed me to inspect the commits that existed remotely but had not yet been integrated locally.

Git then reported that my branch was five commits behind `origin/main`. Only after inspecting those changes did I run `git pull`. The pull fast-forwarded my local branch, and I verified in the Git log that commits authored by the contributor were now part of my local history. This showed me that `fetch` lets me inspect remote changes first, while `pull` retrieves and integrates them into the current branch.




