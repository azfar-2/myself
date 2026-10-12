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
```bash
git push --force-with-lease origin main
```

or/
<br/>

```bash
git revert a757860
```
- then press in keyboard `Esc` , and then `shift`+`:`
- then write `wq!`
- and the push your code
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

<br/>
<br/>
<br/>
<br/>

---

## If you want all the file names in a folder to be replaced at once, follow the steps below.

- Open PowerShell and then first navigate to the directory of the folder that contains all the files.
- And suppose all the files have a common name, "azfar," such as azfar94, azfar-73, azfaralam85, azfarypro4, and similar names. If you want to replace "azfar" wherever it appears with "aizz," then use the command below, and the names will be replaced.

```bash
 Get-ChildItem -Filter "*azfar*" | Rename-Item -NewName { $_.Name -replace 'azfar','aizz' }
```
