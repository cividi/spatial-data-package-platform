# Testing

## Setup

- [ ] Clone this repository and follow the instructions from the Readme
  - [ ] Initialize docker containers
  - [ ] Setup django admin user
  - [ ] Import default list of Gemeinden

## Create a snapshot

- [ ] Go to localhost:8081/gmanage
- [ ] Login with admin user
- [ ] Create a snapshot
- [ ] Set the snapshot to `PUBLIC` and assign a Gemeinde, name and topic
- [ ] For `Data` paste the JSON generated in the [sample project](https://github.com/cividitech/gemeindescan-package-builder) or update it with your own data
- [ ] Upload a screenshot
- [ ] Visit the generated link for the snapshot
- [ ] Verify the map and a legend is loading

## Create a workspace

- [ ] In the Django backend, create new workspace
- [ ] Set a title and description
- [ ] Add the existing snapshot
- [ ] Create a new snapshot exclusive to the workspace by clicking on the green plus icon next to the `Chosen snapshots` list
- [ ] Set this one to `NOT_LISTED` permissions, choose a title, topic, Gemeinde and paste the sample project JSON into `data`
- [ ] Upload a screenshot
- [ ] Save the snapshot and workspace
- [ ] Open the workspace URL

## Verify

- [ ] Snapshot permissions:
  - One snapshot should give your chosen Gemeinde a dot next to it's name in the search indicating existing data and be listed under the respective Gemeinde
  - The other should only appear inside the assigned workspace(s)
- [ ] Update the public snapshot and set the `is_showcase` flag
  - The snapshot should now be listed as "Andere Fallbeispiele" on all Gemeinden except the assigned one and workspaces