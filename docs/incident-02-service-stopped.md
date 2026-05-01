# Troubleshooting Scenario 02: Flask Service Stopped

## Scenario Type
Simulated lab incident

## Goal
Practice diagnosing an application outage where the EC2 instance is working, but the Flask application service is not running.

## Environment
- AWS EC2
- Amazon Linux
- Flask
- systemd
- curl
- journalctl

## Failure Introduced
I intentionally stopped the Flask app's systemd service:

```bash
sudo systemctl stop aws-troubleshooting-lab
```

## Symptoms
The EC2 instance was still reachable through SSH, but the application health endpoint stopped responding.

From my local machine:

```bash
curl http://54.183.179.27:5000/health
```

The request failed because nothing was listening on the application port.

## Diagnosis
First, I confirmed that the EC2 instance itself was reachable by connecting over SSH:

```bash
ssh -i <MY_KEY>.pem ec2-user@54.183.179.27
```

Then I checked the application locally from inside the EC2 instance:

```bash
curl http://localhost:5000/health
```

The local request failed, which showed the issue was likely on the instance rather than the external network path.

Next, I checked the systemd service status:

```bash
sudo systemctl status aws-troubleshooting-lab
```

The service status showed that the Flask application was stopped.

## Root Cause
The Flask application process was not running because the systemd service had been stopped.

## Fix
I restarted the application service:

```bash
sudo systemctl start aws-troubleshooting-lab
```

I also confirmed that the service was active:

```bash
sudo systemctl status aws-troubleshooting-lab
```

## Verification
From inside the EC2 instance:

```bash
curl http://localhost:5000/health
```

From my local machine:

```bash
curl http://54.183.179.27:5000/health
```

Both requests returned a successful health check response.

## What I Learned
A working EC2 instance does not guarantee that the application is running. When troubleshooting an outage, I should check both infrastructure reachability and overall health of service. systemd status and local curl tests help isolate whether the failure is caused by the application process or the EC2 instance.