##Day 1
**Did:** Set up SiteWatch folder structure, resolved GitHub auth error (personal access tokens are used instead of password), pushed my first commit
**Broke/Confused:** GitHub rejected my password, realized they deprecated password and tokens are used for auth instead (took me 20 mins to figure out)
**Clicked:** git add -> commit -> push is like: select changes -> save snapshot -> upload snapshot. It does not upload all the code only the changes made
Also the username we give in git config is just to tell Git who made the change, its not relevant to the actual username in the GitHub account but the email provided should match the account id. --global means from now on we dont have to specify these details for any project it will automatically be applied
**Bigger picture:** Every real company's codebase works exactly like this, that is every push code has same three commands under the hood (add, commit, push)
**Next Day Task:** Write the first version of checker.py- just the part that pings one URL and prints UP or DOWN

##Day 2
**Did:** Wrote checker.py code
**Broke/Confused:** (i)from datetime import datetime confused me, it simply means import datetime class from datetime module. It is done to avoid repeatedly write datetime.datetime()
(ii)on adding irctc site, it showed "DOWN" even though it was "UP" in my browser. It was beacuse this site is aggresively protected and blocks all the requests which does not come from real browser as bots keep trying to buy the tatkal tickets
(iii)https://httpstat.us/200 is always supposed to be "UP" but it was showing "DOWN", analyzing it I realized the site was actually down, so my checker is actually correctly doing its job
**Clicked:** What happens if there are sites which are "UP" but is being shown as "DOWN"- so i updated requests.status_code to be <500 instead of fixed value- 200, and added headers "User-Agent": "Mozilla/5.0" so that it looks like request is coming from an actual browser (irctc still remained undefeated and showed DOWN)
**Bigger picture:** checker.py is the core of SiteWatch with a simple job of pinging URLS and returning UP or DOWN. The complex infrastructure(Redis, Docker, EC2, GitHub Actions) will be built around it.
**Next Day Task:** Connect checker.py to Redis

##Day 
**Did:**
**Broke/Confused:**
**Clicked:**
**Bigger picture:**
**Next Day Task:**
