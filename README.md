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

| Incident                                          | Area       | Summary                                                                     |
| ------------------------------------------------- | ---------- | --------------------------------------------------------------------------- |
| [Incident 01](docs/incident-01-security-group.md) | Networking | App unreachable due to missing security group rule |
| [Incident 02](docs/incident-02-service-stopped.md) | Service Management | App unreachable because the systemd service was stopped |
| [Incident 03](docs/incident-03-missing-dependency.md) | Python Runtime | Flask service failed because a required Python package was missing |