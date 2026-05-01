# Incident 01: Website Unreachable Due to Security Group

## Summary

The Flask application was running successfully on an EC2 instance, but the service was unreachable from my local machine.

## Environment

- AWS EC2
- Amazon Linux 2023
- Python Flask
- systemd
- Security Group inbound rules
- Port: 5000

## Symptoms

From my local machine, the health endpoint failed:

```bash
curl http://54.183.179.27:5000/health
```

The request timed out.

## Initial Checks

I SSHed into the EC2 instance and checked whether the application was running:

```bash
sudo systemctl status aws-troubleshooting-lab
```

I also tested the app locally from inside the EC2 instance:

```bash
curl http://localhost:5000/health
```

The local request succeeded, which showed that the Flask app itself was running.

## Root Cause

The EC2 security group did not allow inbound TCP traffic on port 5000 from my local IP address.

The application was working, but traffic could not reach the instance from outside AWS.

## Fix

I updated the EC2 security group inbound rules to allow traffic to the Flask app on port 5000.

Custom TCP | TCP | 5000 | 0.0.0.0/0

note: I used `0.0.0.0/0` because my IP changes when using a VPN. In a production environment, I would avoid opening this port publicly and would restrict access to known IP ranges.

## Verification

After updating the security group, I tested the endpoint again from my local machine:

```bash
curl http://54.183.179.27:5000/health
```

The endpoint returned a successful JSON response:

```json
{
  "status": "ok"
}
```

## What I Learned

The app was running correctly on the instance, but external traffic could not reach it because the security group was blocking the port. This was a good reminder to check both the service itself and the AWS security groups when debugging connectivity issues.