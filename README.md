# Spinnaker Event listener for Audit Logs
This python service will listen all events that are happening in spinnaker and send logs to AWS CloudwatchLogs

### How to use
- clone the repository

```bash
git clone git@github.com:foss-cafe/spinnaker-event-listener.git
cd spinnaker-event-listener
```

- Build Docker image
```bash
docker build -t spinnaker-event-listener .
```

### If your spinnaker is deployed to kubernetes cluster use use manifest that are in `deploy`
- Update your IAM roles that are attached to EC2 nodes
Use example policy mentioned in `deploy` dir

```bash
kubeclt apply -f deploy/
```
This service will be deployed in `spinnaker` namespace

### If your spinnaker deployed as standalone server
```bash
docker run -d -p 5000:5000 -v $HOME/.aws:~/.aws spinnaker-event-listener
docker ps
```

### Configuring spinnaker
Once your service is deployed, update your hal configs(`ECHO Service`)
- If you are deploying spinnaker using halyard 
Update your hal config `$HOME/.hal/default/profiles` add a new file `echo-local.yml`
```bash 
rest:
  enabled: true
  endpoints:
    - wrap: true
      flatten: false
      url: http://spinnaker-event-lister.spinnaker:5000/api/events # Can work if this deployed via Kubernetes or update the Endpoint
      eventName: spinnaker_events
```
If this step didn't work copy `echo-local.yml` to `/opt/spinnaker/config/` and deploy spinnaker
```bash
hal deploy apply
```