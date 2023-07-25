# Initializing a Git repository locally

## Steps

### Open terminal (VS code or git bash).

### Navigate to the root directory of your project.

### Initialize the local directory as a Git repository

By default, the initial branch is called main.

If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using -b.

```bash
$ git init -b main |
```

### Initialize the local directory as a Git repository

By default, the initial branch is called main.

If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using -b.

```bash
$ git init -b main
```

### Add the files in your new local repository.

This stages them for the first commit.

If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using -b.

```bash
$ git add .
```

Note: Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.

### Commit the files that you've staged in your local repository.

By default, the initial branch is called main.

If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using -b.

```bash
$ git commit -m "First commit"
```

Note: Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.

### Create a github repo on github.com.

Follow the instructions after creating a github repo for pushing existing repo using command line.
