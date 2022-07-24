# Everything is a hash

Git refers to all commits by their **SHA-1 hashes**. So each commit has a unique SHA-1 hash value.

> To see historical git commits, use `git log`. More specifically, `git log -n --oneline` to show `n` results in one-line format. This will return the shortened hash value. To see the full hash value, use `git rev-parse **shortened git hash**`. The `git rev-parse` will return the full hash value of the corresponding commit.

> To see the committed object file. `git cat-file -p **shortened git hash**`. This will return the **tree**, **parent**, **author**, **comitter**. The `-p` option here tells Git to figure out what type of object it's dealing with and to provide appropriately formatted output.

> To see the tree object, just use `git cat-file -p **tree hash**`. The tree object is a pointer to another object that holds the collection of files for this commit. By outputing the tree object using `git cat-file -p **tree hash**`, we can precisely get a compressed representation of the file structure inside the repository.

## Key points

- Git uses **SHA-1** hash to create references to commits, trees and blobs.
- A commit object stores the metadata about a commit, such as the parent, the author, timestamps and references to the file tree of this commit.
- A tree object is a collection of references to either child trees or blob objects.
- Blob objects are compressed collection of files; usually, the set of files in a particular directory inside the tree.
- git rev-parse, will translate a short hash into a long hash
- git cat-file, among other things, will show you the pertinent metadata about an object.

# Merge conflicts

For simple text files, Git uses an approach known as the **longest common subsequence algorithm** to perform merges and to detect merge conflicts. Git finds the longest set of lines in common between your changed file and the common ancestor. It then finds the longest set of lines in common between your teammate's changed file and its common ancestor.

> To rollback and start over, `git reset --hard HEAD`. This reverts your working env back to match HEAD, which, in this case, is the latest commit of your current branch.

For merge conflicts, my idea is always update the current branch before merging anything. Make sure the currnet branch is updated and no conflicts is required to resolve. If conflicts have to be resolved, do that via a GUI.

# Stash

**Commit** is the atomic level of Git, there's nothing below it. We can not do anything outside a commit, and we should limit ourselves build a working, documented commit each and everytime we want to push our work to the repository. But we can not always work to the level of a commit. Development is messy and unpredicable; we may go down a few parallel rabbit holes, chasing different possiblities, before finding the right solution for a bug. Or quite commonly, we may be building our next feature for the app when, suddenly, we need to switch over to a bugfix branch and get a hotfix.
Therefore, for the unfinished work and the uncompilable code that isn't quite ready to be commited, but we don't want to lose -> `git stash`.

## Retriving stashes

> Try `git checkout -`
