# shipyard-demo

A tiny web service used to demonstrate [Shipyard](https://github.com/Shrinet82/shipyard): pull requests,
CI, merges and deploys driven from chat. The open pull requests are deliberate test cases:

| PR | What it exercises |
|---|---|
| Add a health endpoint | a normal change, CI green |
| Install dependencies from requirements.txt | CI passes but the Docker build fails |
| Bump the version footer | a clean merge and deploy |
| Add footer check | a failing test, merge refused |
| Reword the greeting | conflicts with main, merge refused |

CI runs on every pull request and on pushes to main.

<!-- merge path test 1793886702 -->
<!-- badges 1793900419 -->
