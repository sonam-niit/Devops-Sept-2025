# Blue Green Deployment Stratergy

- Use this for minimum downtime or 0 downtime and for easy rollback
- Here we have 2 identical environments

- Blue - current live/production version
- green - New Updated Version

## How Process Works

1. Blue is live 
    - blue environment which is stable, production env
    - traffic handled by this environment
2. Deploy to green
    - deploy new app to green environment
    - it is not accessed by users yet.
3. Test Green Env:
    - integration test
    - Health check etc
4. Switch Traffic
    - Update Load Banacer /DNS/ingress to route traffics from Blue to Green
    - now green becomes live
5. Monitor
    - monitor logs, metrics and errors
6. Rollback (if needed)
    - if issues -> rollback traffic from green to blue instantly

**Advantages**
- Zero Downtime
- Easy Rollback
- Safe Deployment
- easy testing befor release

**Disadvantages**
- Requires double infra
- High cost
- Database changes needs to handle very carefully

## Canary Deployment

- Stragergy where a new version is released to a small percentage of users first
- if it performs well we can increase traffic gradually.

- Canary means small group of users to detect issues before release.

**How it works**

1. Stable Version is Live 
    - v1- handling 100% traffic
2. Deployed canary version
    - V2 deployed alongwith v1
3. Send small traffic
    - v1 - 95%
    - v2 - 5%
4. Monitor:
    - Error rate, letency, CPU/Memory, Logs
5. gradually increase traffic:
    - 5% -> 25% -> 50% -> 100%
6. Rollback if issues
    - problem occures roll back to v1

## Rolling Deployment

- Rolling deployment is gradually replaces the old version of an application with new version one batch of servers at a time, without dowtime for the entire system.

- its using single environment and update done incrementally.

**How rolling deployment works?**

1. Old version is live
    - v1 is running on 10 servers (10 instances)
2. Deploy new version to a subset
    - update 2 servers to v2(20%)
3. Monitor Subset
    - Health check, metrics, logs
    - makesure there is no error
4. Coninue Rolling
    - update next 2-3 servers -> Monitor
    - Repeat untill all servers run on v2 (100%)
5. Rollback if needed
    - stop deployment
    - revert updated servers to old version