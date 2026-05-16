### If your git push ask for your token

```bash
git remote set-url origin https://<your-token-paste-here>@github.com/mdazfar2/repository
```

<br/>

### Clone your private repository in any OS

```bash
git clone https://mdazfar2:<your-token-paste-here>@github.com/mdazfar2/repository.git
```

<br/>

## Undo your Previous commits from your github repo
```bash
git reset --hard HEAD~1
```

or/

```bash
git revert a757860
```
```bash
git push origin main
```


## changes files all remove folder, files everything

  ```bash
   git clean -fdxn
  ```

<br/>

---

## If you want to copy your friend’s project into your own new repository while preserving all commit history, follow the steps below.

- **Manual process** ->
     - First clone your frnds project and open `.git` folder and thenn open `config` file
     - You will get code like this:

```ini
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true

[remote "origin"]
	url = https://github.com/mdazfar2/HelpOps-Hub.git
	fetch = +refs/heads/*:refs/remotes/origin/*

[branch "main"]
	remote = origin
	merge = refs/heads/main
```

In this code, the `url` field contains your friend’s repository URL. Replace it with the link of the new repository that you created, that’s it.

Then open the terminal and run:

```bash
git push -u origin main
```

All the commit history will appear.
