# Production Hardening Backlog

## ECS Networking

Current dev design:
- ALB in public subnets
- ECS tasks in public subnets
- ECS security group only allows inbound traffic from ALB security group
- assign_public_ip = true

Production target:
- ALB remains in public subnets
- ECS tasks move to private subnets
- assign_public_ip = false
- ECS outbound access through NAT Gateway or VPC endpoints
- Consider VPC endpoints for ECR, CloudWatch Logs, Secrets Manager, and SSM
