##Day 1
**Did:** Set up SiteWatch folder structure, resolved GitHub auth error (personal access tokens are used instead of password), pushed my first commit
**Broke/Confused:** GitHub rejected my password, realized they deprecated password and tokens are used for auth instead (took me 20 mins to figure out)
**Clicked:** git add -> commit -> push is like: select changes -> save snapshot -> upload snapshot. It does not upload all the code only the changes made
Also the username we give in git config is just to tell Git who made the change, its not relevant to the actual username in the GitHub account but the email provided should match the account id. --global means from now on we dont have to specify these details for any project it will automatically be applied
**Bigger picture:** Every real company's codebase works exactly like this, that is every push code has same three commands under the hood (add, commit, push)
**Next Day Task:** Write the first version of checker.py- just the part that pings one URL and prints UP or DOWN
