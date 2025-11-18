# Deploying Zyppys Dashboard to Vercel

This guide will help you deploy the Zyppys Luxury Car Rental Dashboard to Vercel for free hosting.

## Prerequisites

1. A GitHub account (already have the code pushed)
2. A Vercel account (free) - Sign up at https://vercel.com

## Deployment Methods

### Method 1: Deploy via Vercel Dashboard (Recommended - Easiest)

1. **Sign up/Login to Vercel:**
   - Go to https://vercel.com
   - Click "Sign Up" or "Login"
   - Choose "Continue with GitHub"
   - Authorize Vercel to access your GitHub repositories

2. **Import Your Project:**
   - Click "Add New..." → "Project"
   - Find and select your repository: `adspire93/tarriffs`
   - Click "Import"

3. **Configure Project:**
   - **Framework Preset:** Select "Other" (it's a static site)
   - **Root Directory:** Leave as is (root)
   - **Build Command:** Leave empty or use: `echo "No build required"`
   - **Output Directory:** `public`
   - Click "Deploy"

4. **Wait for Deployment:**
   - Vercel will automatically deploy your site
   - Takes about 30-60 seconds
   - You'll get a URL like: `https://zyppys-luxury-dashboard.vercel.app`

5. **Done!**
   - Your dashboard is now live
   - Share the URL with anyone
   - Auto-deploys on every git push

### Method 2: Deploy via Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   cd /home/user/tarriffs
   vercel
   ```

4. **Follow Prompts:**
   - Set up and deploy? Yes
   - Which scope? Select your account
   - Link to existing project? No
   - Project name? `zyppys-luxury-dashboard`
   - Directory? `./` (current directory)
   - Override settings? No

5. **Production Deployment:**
   ```bash
   vercel --prod
   ```

## Configuration Files

The following files have been created for Vercel deployment:

### `vercel.json`
```json
{
  "version": 2,
  "name": "zyppys-luxury-dashboard",
  "buildCommand": "echo 'No build required'",
  "outputDirectory": "public",
  "cleanUrls": true,
  "trailingSlash": false
}
```

### `package.json`
Contains project metadata for Vercel.

### `.vercelignore`
Excludes unnecessary files from deployment (Python scripts, Excel files, etc.)

## Project Structure for Vercel

```
tarriffs/
├── public/              # Deployed folder
│   ├── index.html      # Main dashboard
│   ├── *.html          # All segment pages
│   ├── css/
│   ├── js/
│   ├── images/         # 62 car images
│   ├── data.json
│   └── image_mapping.json
├── dashboard/          # Original folder (kept as backup)
├── vercel.json         # Vercel configuration
├── package.json        # Project metadata
└── .vercelignore       # Ignore rules
```

## Custom Domain (Optional)

1. **In Vercel Dashboard:**
   - Go to your project
   - Click "Settings" → "Domains"
   - Add your custom domain
   - Follow DNS configuration instructions

2. **Example Domains:**
   - `zyppys-dashboard.com`
   - `tariffs.zyppys.com`
   - Any domain you own

## Environment Variables (If Needed)

If you need to add any environment variables:
1. Go to Project Settings → Environment Variables
2. Add key-value pairs
3. Redeploy

## Continuous Deployment

- Every push to the branch `claude/create-zyppys-dashboard-01642Nx16AS2ZsLxMVxPwT5W` will auto-deploy
- You can change the production branch in Vercel settings
- Preview deployments for pull requests

## Monitoring & Analytics

Vercel provides:
- **Analytics:** View traffic and performance
- **Logs:** Check deployment logs
- **Speed Insights:** Performance metrics
- All available in the Vercel dashboard

## Troubleshooting

### Issue: 404 Errors
- **Solution:** Check that `outputDirectory` is set to `public`
- Verify files exist in the public folder

### Issue: Images Not Loading
- **Solution:** Ensure the `public/images/` folder has all 62 images
- Check browser console for errors

### Issue: JavaScript Not Working
- **Solution:** Verify `public/js/app.js` exists
- Check that paths are relative (not absolute)

### Issue: Deployment Failed
- **Solution:** Check Vercel deployment logs
- Ensure vercel.json is valid JSON
- Try redeploying

## Testing Locally Before Deploy

```bash
# Option 1: Simple HTTP server
cd public
python3 -m http.server 8080
# Visit http://localhost:8080

# Option 2: Using Vercel CLI (exact production replica)
vercel dev
# Visit http://localhost:3000
```

## Cost

- **Free Tier Includes:**
  - Unlimited deployments
  - 100 GB bandwidth/month
  - Automatic SSL certificates
  - Global CDN
  - Perfect for this dashboard!

## Support

- Vercel Documentation: https://vercel.com/docs
- Vercel Community: https://github.com/vercel/vercel/discussions
- Status: https://vercel-status.com

## Your Deployed Dashboard

Once deployed, you'll get:
- **Production URL:** `https://your-project.vercel.app`
- **Preview URLs:** For each commit/PR
- **Automatic HTTPS:** SSL included
- **Global CDN:** Fast worldwide access
- **Auto-deployments:** On every git push

## Next Steps After Deployment

1. **Share the URL** with your team
2. **Set up custom domain** (optional)
3. **Monitor analytics** in Vercel dashboard
4. **Update content** by pushing to git (auto-redeploys)

---

**Ready to deploy!** Just follow Method 1 above - takes less than 2 minutes! 🚀
