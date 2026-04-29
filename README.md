# AWS Cloud Troubleshooting Lab

A hands-on AWS troubleshooting project using EC2, Linux, Python Flask, security groups, systemd, and service logs.

## Architecture

Local machine -> EC2 public IPv4 -> Security Group TCP 5000 -> Flask app

## Endpoints

- `/` - basic homepage
- `/health` - service health check
- `/debug` - app metadata
- `/error` - intentional error endpoint for troubleshooting practice

## Technologies

- AWS EC2
- Amazon Linux 2023
- Security Groups
- Python Flask
- systemd
- Linux CLI
- curl
- journalctl

## Troubleshooting Scenarios

1. Website unreachable due to missing security group rule
2. Flask service stopped or failed
3. Application error visible in logs
4. SSH access issue
5. Port mismatch between app and security group