### If your git push ask for your token-

```bash
git remote set-url origin https://<your-token-paste-here>@github.com/mdazfar2/repository
```
<br/>

## Undo your Previous commits from your github repo
```bash
git reset --hard HEAD~1
```

## 🎮 Push Pull Game 


### If you need to pull a specific file from your GitHub repository.

```bash
git remote add -f origin https://github.com/mdazfar2/Azure-WebApp-Github-Actions
```
```bash
git config core.sparseCheckout true
```
```bash
git sparse-checkout set <src/assets>
```

>`src/assets` instead of this you have to use another file path which you want to copy

<br/>

### If you need to bring the entire code from any repository

```bash
git sparse-checkout disable
```
>Every code will come

<br/>

### Now, if you want all of that code to revert and the code that you entered earlier to remain the same, use this command.

```bash
 git sparse-checkout init
 ```

## Merging from one to another repository
```bash
git remote set-url origin https://github.com/ravikant-85/react-app
```
```bash
git merge origin/main  --allow-unrelated-histories
```

