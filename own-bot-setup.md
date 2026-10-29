# 🤖 AzfarAi Bot Setup Guide
---

## Step 1: Create Your GitHub App (If not created already)

1. Open GitHub and go to: **[Settings → Developer Settings → GitHub Apps](https://github.com/settings/apps)**.
2. Click **New GitHub App**.
3. Fill in the basic info:
   - **GitHub App name:** `AzfarAi`
   - **Homepage URL:** `https://github.com/mdazfar2/Ezyshop`
   - **Description:** *(Paste your custom markdown description)*
   - **Webhook:** **Uncheck** "Active" (webhooks are not needed).
4. Under **Permissions & events** → **Repository permissions**, set:
   - **Issues:** `Read and write`
   - **Pull requests:** `Read and write`
   - **Contents:** `Read and write` *(needed if AzfarAi pushes automated commits like README updates)*
5. Under **Where can this GitHub App be installed?**, select:
   - **Any account** or **Only on this account**.
6. Click **Create GitHub App**.
7. In the **Display information** section, upload your bot's **Profile Picture / Logo**.

---

## Step 2: Install the App on Your Repositories

1. On the left sidebar of your GitHub App settings, click **Install App**.
2. Click the green **Install** button next to your account.
3. Select **All repositories** (or choose specific repositories like `Ezyshop`).
4. Click **Install**.

---

## Step 3: Get Your App ID & Private Key (.pem file)

### A. Get the App ID:
1. In your GitHub App page, click **General** in the left sidebar.
2. Look near the top for **App ID** (a number like `1234567`).
3. Copy this number.

### B. Download the `.pem` Private Key:
1. In the left sidebar, click **Credentials** (with the 🔑 key icon).
2. At the top, click on the **Key pairs** tab (right next to *Client secrets*).
3. Click the green button: **Generate a key pair** (or **Generate private key**).
4. A file ending in `.pem` (e.g., `azfarai.2026-10-29.private-key.pem`) will automatically download to your **Downloads** folder.

---

## Step 4: Add the Secrets to Your Repository

1. Open your repository: **[https://github.com/mdazfar2/Ezyshop](https://github.com/mdazfar2/Ezyshop)**.
2. Go to **Settings** → **Secrets and variables** → **Actions**.
3. Add the **App ID**:
   - Click **New repository secret**.
   - **Name:** `AZFARAI_APP_ID`
   - **Secret:** *(Paste your numeric App ID)*
   - Click **Add secret**.
4. Add the **Private Key**:
   - Open your downloaded `.pem` file using **Notepad** or **VS Code**.
   - Copy **everything** inside (including `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----`).
   - In GitHub Secrets, click **New repository secret**.
   - **Name:** `AZFARAI_PRIVATE_KEY`
   - **Secret:** *(Paste the entire contents of the `.pem` file)*
   - Click **Add secret**.

---

## Step 5: How the Workflow Uses AzfarAi

In `.github/workflows/greetings.yml`, the workflow generates a temporary token for AzfarAi and greets users:

```yaml
- name: Generate AzfarAi Bot Token
  id: azfarai-token
  if: env.AZFARAI_APP_ID != '' && env.AZFARAI_PRIVATE_KEY != ''
  uses: actions/create-github-app-token@v1
  with:
    app-id: ${{ secrets.AZFARAI_APP_ID }}
    private-key: ${{ secrets.AZFARAI_PRIVATE_KEY }}

- name: Community Welcome Action
  uses: EddieHubCommunity/gh-action-community/src/welcome@main
  with:
    github-token: ${{ steps.azfarai-token.outputs.token || secrets.GITHUB_TOKEN }}
    issue-message: "Hello ${{ github.actor }}! Thanks for opening an issue in Ezyshop! 🚀"
    pr-message: "Thank you, ${{ github.actor }}, for your contribution! 🎉"
```

> **Note:** If `AZFARAI_APP_ID` or `AZFARAI_PRIVATE_KEY` are ever missing, the workflow automatically falls back to `GITHUB_TOKEN` so your workflows will never crash.

---

## Step 6: Using AzfarAi on Other Repositories

Because you chose **"All repositories"** during installation:
1. Open any other repository you own.
2. Add the same 2 repository secrets (`AZFARAI_APP_ID` and `AZFARAI_PRIVATE_KEY`).
3. Add the workflow step above to that repo's `.github/workflows/`.
4. **AzfarAi** will immediately work on that repository too!

---

## 🧪 Testing Your Bot

1. Open a test issue or pull request in the repository.
2. Within seconds, **AzfarAi [Bot]** will reply with its custom name and profile avatar!

